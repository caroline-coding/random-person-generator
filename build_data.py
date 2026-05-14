#!/usr/bin/env python3
"""Build a ~30k-row sample of 2020-2024 5-Year ACS PUMS for the random-person generator.

Each PUMS row is one anonymized real American with all attributes jointly observed.
We weighted-reservoir-sample 30k rows (weight = PWGTP) so the sample's joint
distributions match the population's by construction. Output: data.json.
"""

import bisect, csv, heapq, io, json, os, random, re, sys, urllib.request, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
PUMS_URL = "https://www2.census.gov/programs-surveys/acs/data/pums/2024/5-Year/csv_pus.zip"
HH_URL = "https://www2.census.gov/programs-surveys/acs/data/pums/2024/5-Year/csv_hus.zip"
DICT_URL = "https://www2.census.gov/programs-surveys/acs/tech_docs/pums/data_dict/PUMS_Data_Dictionary_2020-2024.csv"
# SSA blocks scripted downloads, so we use the Wayback Machine snapshot.
SSA_URL = "https://web.archive.org/web/2025/https://www.ssa.gov/oact/babynames/names.zip"
PUMS_LOCAL = os.path.join(HERE, "pums_2020_2024.zip")
HH_LOCAL = os.path.join(HERE, "pums_hh_2020_2024.zip")
DICT_LOCAL = os.path.join(HERE, "pums_dict_2020_2024.csv")
SSA_LOCAL = os.path.join(HERE, "ssa_names.zip")
SURVEY_YEAR = 2022  # midpoint of 2020-2024 5-year ACS
DATA_JSON = os.path.join(HERE, "data.json")
DATA_JS = os.path.join(HERE, "data.js")
N_TARGET = 30000
HH_COLS = ("TEN", "VALP", "RNTP", "BDSP", "NP")

KEEP_COLS = [
    "SERIALNO", "AGEP", "SEX", "RAC1P", "HISP", "STATE", "PUMA",
    "SCHL", "FOD1P", "MAR", "OCCP", "INDP", "PINCP", "WAGP", "ESR",
    "OC", "RELSHIPP", "PWGTP",
    "MIL", "DIS", "CIT", "NATIVITY", "YOEP", "LANP", "ENG",
]


def download(url, local):
    if os.path.exists(local) and os.path.getsize(local) > 1000:
        sys.stderr.write(f"Cached: {local} ({os.path.getsize(local):,} bytes)\n")
        return
    sys.stderr.write(f"Downloading {url}\n  -> {local}\n")
    with urllib.request.urlopen(url) as resp:
        total = int(resp.headers.get("Content-Length", 0))
        got = 0
        with open(local + ".part", "wb") as f:
            while True:
                chunk = resp.read(1 << 20)
                if not chunk: break
                f.write(chunk); got += len(chunk)
                if total:
                    sys.stderr.write(f"\r  {got/1e9:.2f}/{total/1e9:.2f} GB ({100*got/total:.1f}%)")
                    sys.stderr.flush()
        sys.stderr.write("\n")
        os.rename(local + ".part", local)


def parse_value_labels(dict_path):
    """Return {var: {code: label}} for single-value codes."""
    out = {}
    with open(dict_path, encoding="utf-8") as f:
        for row in csv.reader(f):
            if not row or row[0] != "VAL" or len(row) < 7: continue
            var, _, _, code_min, code_max, label = row[1], row[2], row[3], row[4], row[5], row[6]
            if code_min == code_max:
                out.setdefault(var, {})[code_min] = label
    return out


STATE_FIPS = {
    "01":"Alabama","02":"Alaska","04":"Arizona","05":"Arkansas","06":"California",
    "08":"Colorado","09":"Connecticut","10":"Delaware","11":"District of Columbia",
    "12":"Florida","13":"Georgia","15":"Hawaii","16":"Idaho","17":"Illinois",
    "18":"Indiana","19":"Iowa","20":"Kansas","21":"Kentucky","22":"Louisiana",
    "23":"Maine","24":"Maryland","25":"Massachusetts","26":"Michigan","27":"Minnesota",
    "28":"Mississippi","29":"Missouri","30":"Montana","31":"Nebraska","32":"Nevada",
    "33":"New Hampshire","34":"New Jersey","35":"New Mexico","36":"New York",
    "37":"North Carolina","38":"North Dakota","39":"Ohio","40":"Oklahoma","41":"Oregon",
    "42":"Pennsylvania","44":"Rhode Island","45":"South Carolina","46":"South Dakota",
    "47":"Tennessee","48":"Texas","49":"Utah","50":"Vermont","51":"Virginia",
    "53":"Washington","54":"West Virginia","55":"Wisconsin","56":"Wyoming","72":"Puerto Rico",
}
RACE_MAP = {
    "1":"White","2":"Black or African American",
    "3":"American Indian","4":"Alaska Native","5":"American Indian and Alaska Native",
    "6":"Asian","7":"Native Hawaiian or Pacific Islander",
    "8":"Some other race","9":"Two or more races",
}
MAR_MAP = {"1":"Married","2":"Widowed","3":"Divorced","4":"Separated","5":"Never married"}
ESR_MAP = {
    "1":"Employed","2":"Employed, not at work","3":"Unemployed",
    "4":"Armed forces (at work)","5":"Armed forces (not at work)","6":"Not in labor force",
}

CIT_MAP = {
    "1": "Born in the US",
    "2": "Born in a US territory",
    "3": "Born abroad to US citizen parent(s)",
    "4": "Naturalized US citizen",
    "5": "Not a US citizen",
}
ENG_MAP = {"1":"very well","2":"well","3":"not well","4":"not at all"}
TEN_MAP = {
    "1": "Owns with mortgage",
    "2": "Owns free and clear",
    "3": "Rents",
    "4": "Occupies without paying rent",
}

_GRADE_NAMES = {
    4:"1st grade", 5:"2nd grade", 6:"3rd grade", 7:"4th grade",
    8:"5th grade", 9:"6th grade", 10:"7th grade", 11:"8th grade",
    12:"9th grade", 13:"10th grade", 14:"11th grade", 15:"12th grade",
}
def schl_label(c):
    if not c or c.startswith("b"): return None
    try: n = int(c)
    except ValueError: return None
    if n == 1: return "No schooling completed"
    if n == 2: return "Preschool"
    if n == 3: return "Kindergarten"
    if n in _GRADE_NAMES: return _GRADE_NAMES[n]
    if n == 16: return "High school graduate"
    if n == 17: return "GED or alternative"
    if n in (18, 19): return "Some college, no degree"
    if n == 20: return "Associate's degree"
    if n == 21: return "Bachelor's degree"
    if n == 22: return "Master's degree"
    if n == 23: return "Professional degree"
    if n == 24: return "Doctorate"
    return None

def race_eth(rac1p, hisp):
    if hisp and hisp not in ("01", "1"):
        return "Hispanic or Latino"
    return RACE_MAP.get(rac1p, "Other")

SOC_PREFIX_RE = re.compile(r"^[A-Z]{3}-")
KEEP_LOWER = {"and","or","of","the","in","for","to","with","a","an","at"}
KEEP_UPPER = {"EMT","HVAC","IT","TV","HR","CEO","COO","CFO","CTO","CIO","RN","LPN","K-12","US"}

def clean_occ(label):
    label = SOC_PREFIX_RE.sub("", label).strip()
    parts = re.split(r"(\s+|[/-])", label)
    out = []
    for i, p in enumerate(parts):
        if not p or p.isspace() or p in "/-":
            out.append(p); continue
        pl = p.lower()
        if i > 0 and pl in KEEP_LOWER:
            out.append(pl)
        elif p.upper() in KEEP_UPPER:
            out.append(p.upper())
        else:
            out.append(pl.capitalize())
    return "".join(out)


def load_ssa_names(ssa_zip_path):
    """Returns {(year, "M"|"F"): (names_list, cumulative_weights)}.
    Walking the cumulative weights with bisect gives a frequency-weighted sample."""
    import bisect
    pools = {}
    years = []
    with zipfile.ZipFile(ssa_zip_path) as zf:
        for name in zf.namelist():
            m = re.match(r"yob(\d{4})\.txt$", name)
            if not m: continue
            year = int(m.group(1))
            years.append(year)
            names_m, weights_m, acc_m = [], [], 0
            names_f, weights_f, acc_f = [], [], 0
            with zf.open(name) as f:
                for raw_line in io.TextIOWrapper(f, encoding="utf-8"):
                    parts = raw_line.strip().split(",")
                    if len(parts) != 3: continue
                    n, s, c = parts[0], parts[1], int(parts[2])
                    if s == "M":
                        acc_m += c
                        names_m.append(n); weights_m.append(acc_m)
                    else:
                        acc_f += c
                        names_f.append(n); weights_f.append(acc_f)
            pools[(year, "M")] = (names_m, weights_m)
            pools[(year, "F")] = (names_f, weights_f)
    sys.stderr.write(f"SSA names loaded: years {min(years)}-{max(years)}, {len(pools)} (year,sex) pools\n")
    return pools, min(years), max(years)


def pick_first_name(pools, year_min, year_max, sex_str, age):
    import bisect
    yr = max(year_min, min(year_max, SURVEY_YEAR - age))
    sex = "M" if sex_str == "1" else "F"
    pool = pools.get((yr, sex))
    if not pool or not pool[1]:
        return None
    names, cw = pool
    total = cw[-1]
    r = random.randint(1, total)
    return names[bisect.bisect_left(cw, r)]


def load_hh_housing(hh_zip_path, wanted_serialnos):
    """Stream the household file and pull housing data for the wanted SERIALNOs."""
    out = {}
    with zipfile.ZipFile(hh_zip_path) as zf:
        csv_files = sorted(n for n in zf.namelist() if n.endswith(".csv"))
        sys.stderr.write(f"HH CSVs: {csv_files}\n")
        for name in csv_files:
            sys.stderr.write(f"Scanning {name}...\n")
            with zf.open(name) as f:
                text = io.TextIOWrapper(f, encoding="utf-8", newline="")
                reader = csv.reader(text)
                header = next(reader)
                idx = {h: i for i, h in enumerate(header)}
                sni = idx["SERIALNO"]
                col_idx = {c: idx[c] for c in HH_COLS if c in idx}
                n = 0
                for row in reader:
                    sno = row[sni]
                    if sno in wanted_serialnos:
                        out[sno] = {c: row[i] for c, i in col_idx.items()}
                    n += 1
                    if n % 1_000_000 == 0:
                        sys.stderr.write(f"  {n:,} HH rows scanned; matched {len(out):,}/{len(wanted_serialnos):,}\n")
    sys.stderr.write(f"Matched {len(out):,}/{len(wanted_serialnos):,} households\n")
    return out


def main():
    download(DICT_URL, DICT_LOCAL)
    download(PUMS_URL, PUMS_LOCAL)
    download(HH_URL, HH_LOCAL)
    download(SSA_URL, SSA_LOCAL)
    name_pools, ssa_year_min, ssa_year_max = load_ssa_names(SSA_LOCAL)

    labels = parse_value_labels(DICT_LOCAL)
    occp_labels = {c: clean_occ(l) for c, l in labels.get("OCCP", {}).items()}
    indp_labels = {c: clean_occ(l) for c, l in labels.get("INDP", {}).items()}
    fod_labels = {c: l for c, l in labels.get("FOD1P", {}).items()}
    lanp_labels = {c: l for c, l in labels.get("LANP", {}).items()}

    heap = []  # (key, tie, raw_row + HH context)
    tie = 0
    pwgtp_sum = 0

    MEMBER_COLS = ("AGEP","SEX","RAC1P","HISP","OCCP","ESR","RELSHIPP","PINCP")

    def process_household(hh_rows, idx, keep):
        nonlocal tie
        oci = idx.get("OC")
        wi = idx["PWGTP"]
        pincpi = idx.get("PINCP")
        # Count own children of the householder in this HH (OC=1)
        kids_in_hh = sum(1 for r in hh_rows if (oci is not None and r[oci] == "1"))
        # Total HH income (sum of PINCP)
        hh_income = 0
        if pincpi is not None:
            for r in hh_rows:
                try: hh_income += int(r[pincpi])
                except (ValueError, IndexError): pass
        # Raw member dicts (one per HH person), kept verbatim for later decoding.
        members = [{c: r[idx[c]] for c in MEMBER_COLS if c in idx} for r in hh_rows]
        for k, row in enumerate(hh_rows):
            try: w = int(row[wi])
            except (ValueError, IndexError): continue
            if w <= 0: continue
            u = random.random()
            if u <= 0: continue
            key = u ** (1.0 / w)
            others = [m for j, m in enumerate(members) if j != k]
            if len(heap) < N_TARGET:
                raw = {c: row[i] for c, i in keep}
                raw["__kids_in_hh"] = kids_in_hh
                raw["__hh_income"] = hh_income
                raw["__hh_others"] = others
                heapq.heappush(heap, (key, tie, raw)); tie += 1
            elif key > heap[0][0]:
                raw = {c: row[i] for c, i in keep}
                raw["__kids_in_hh"] = kids_in_hh
                raw["__hh_income"] = hh_income
                raw["__hh_others"] = others
                heapq.heapreplace(heap, (key, tie, raw)); tie += 1

    with zipfile.ZipFile(PUMS_LOCAL) as zf:
        csv_files = sorted([n for n in zf.namelist() if n.endswith(".csv")])
        sys.stderr.write(f"CSVs in zip: {csv_files}\n")
        for csv_name in csv_files:
            sys.stderr.write(f"Processing {csv_name}...\n")
            with zf.open(csv_name) as raw_f:
                text = io.TextIOWrapper(raw_f, encoding="utf-8", newline="")
                reader = csv.reader(text)
                header = next(reader)
                idx = {h: i for i, h in enumerate(header)}
                missing = [c for c in KEEP_COLS if c not in idx]
                if missing:
                    sys.stderr.write(f"  WARNING: missing cols {missing}\n")
                keep = [(c, idx[c]) for c in KEEP_COLS if c in idx]
                wi = idx["PWGTP"]
                sni = idx.get("SERIALNO")
                oci = idx.get("OC")
                n = 0
                current_sno = None
                buf = []
                for row in reader:
                    sno = row[sni] if sni is not None else None
                    if sno != current_sno:
                        if buf:
                            process_household(buf, idx, keep)
                        buf = [row]
                        current_sno = sno
                    else:
                        buf.append(row)
                    try: pwgtp_sum += int(row[wi])
                    except (ValueError, IndexError): pass
                    n += 1
                    if n % 1_000_000 == 0:
                        sys.stderr.write(f"  {n:,} rows read; reservoir {len(heap)}; sum PWGTP {pwgtp_sum/1e6:.1f}M\n")
                if buf:
                    process_household(buf, idx, keep)
                sys.stderr.write(f"  done {csv_name}: {n:,} rows\n")

    sys.stderr.write(f"\nReservoir: {len(heap)} rows. Total PWGTP sum: {pwgtp_sum/1e6:.1f}M\n")
    # Join in housing data from HH file
    wanted = {r["SERIALNO"] for _, _, r in heap if "SERIALNO" in r}
    sys.stderr.write(f"Looking up {len(wanted):,} households in HH file...\n")
    hh_housing = load_hh_housing(HH_LOCAL, wanted)
    sys.stderr.write("Decoding...\n")

    # Dictionary-encode categorical columns for compactness.
    races_dict, states_dict, edu_dict = {}, {}, {}
    mar_dict, occ_dict, emp_dict = {}, {}, {}
    fod_dict, ind_dict, cit_dict = {}, {}, {}
    lang_dict, eng_dict, ten_dict = {}, {}, {}

    def intern(d, v):
        if v is None: return -1
        if v not in d: d[v] = len(d)
        return d[v]

    def decode_member(m):
        try: age = int(m.get("AGEP", ""))
        except ValueError: age = 0
        sex = 1 if m.get("SEX") == "1" else 0
        race = race_eth(m.get("RAC1P", ""), m.get("HISP", ""))
        occ_code = m.get("OCCP", "")
        if occ_code and occ_code != "0000" and not occ_code.startswith("b"):
            occ = occp_labels.get(occ_code)
        else:
            occ = None
        if occ and "Unemployed" in occ and "Never Worked" in occ:
            occ = None
        esr_code = m.get("ESR", "")
        if not esr_code or esr_code.startswith("b"):
            emp = "Under 16" if age < 16 else None
        else:
            emp = ESR_MAP.get(esr_code)
        try: rel = int(m.get("RELSHIPP", "") or 0)
        except ValueError: rel = 0
        try: inc = int(m.get("PINCP", "") or 0)
        except ValueError: inc = 0
        return [
            age, sex,
            intern(races_dict, race),
            intern(occ_dict, occ),
            intern(emp_dict, emp),
            rel, inc,
        ]

    rows = []
    for _, _, r in heap:
        try: age = int(r.get("AGEP", ""))
        except ValueError: continue
        sex = 1 if r.get("SEX") == "1" else 0  # 1=Male, 0=Female
        first_name = pick_first_name(name_pools, ssa_year_min, ssa_year_max, r.get("SEX", ""), age) or ""
        race = race_eth(r.get("RAC1P", ""), r.get("HISP", ""))
        state = STATE_FIPS.get(r.get("STATE", ""), "Unknown")
        edu = schl_label(r.get("SCHL", ""))
        mar = MAR_MAP.get(r.get("MAR", "")) if age >= 15 else None
        occ_code = r.get("OCCP", "")
        if occ_code and occ_code != "0000" and not occ_code.startswith("b"):
            occupation = occp_labels.get(occ_code)
        else:
            occupation = None
        if occupation and "Unemployed" in occupation and "Never Worked" in occupation:
            occupation = None
        esr_code = r.get("ESR", "")
        if not esr_code or esr_code.startswith("b"):
            employment = "Under 16" if age < 16 else None
        else:
            employment = ESR_MAP.get(esr_code)
        try: income = int(r.get("PINCP", "") or 0)
        except ValueError: income = 0
        try: wages = int(r.get("WAGP", "") or 0)
        except ValueError: wages = 0
        try: rel = int(r.get("RELSHIPP", "") or 0)
        except ValueError: rel = 0

        kids_in_hh = r.get("__kids_in_hh", 0)
        # Attribute kids only to householder & spouse (RELSHIPP 20=ref, 21=opp-sex spouse, 23=same-sex spouse)
        if rel in (20, 21, 23):
            own_kids = kids_in_hh
        elif rel in (25, 26, 27, 35):
            own_kids = 0  # they are the child
        else:
            own_kids = -1  # unknown for unmarried partner / other relative / nonrelative / GQ

        hh_income = r.get("__hh_income", 0)
        hh_others = [decode_member(m) for m in r.get("__hh_others", [])]

        # Field of degree (only meaningful for bachelor's+)
        fod_code = r.get("FOD1P", "")
        field_of_degree = fod_labels.get(fod_code) if fod_code and not fod_code.startswith("b") else None

        # Industry (only meaningful if employed / worked recently)
        ind_code = r.get("INDP", "")
        if ind_code and not ind_code.startswith("b") and ind_code != "0000":
            industry = indp_labels.get(ind_code)
        else:
            industry = None

        # Veteran status: any past or current military service
        mil_code = r.get("MIL", "")
        is_veteran = mil_code in ("1", "2")
        is_active_duty = mil_code == "1"

        # Disability flag
        has_disability = r.get("DIS", "") == "1"

        # Citizenship
        cit_code = r.get("CIT", "")
        citizenship = CIT_MAP.get(cit_code)

        # Year of entry (foreign-born / naturalized)
        try: yoep = int(r.get("YOEP", "") or 0)
        except ValueError: yoep = 0

        # Language at home
        lanp_code = r.get("LANP", "")
        if lanp_code and not lanp_code.startswith("b"):
            language = lanp_labels.get(lanp_code)
        else:
            language = None  # English only
        eng_code = r.get("ENG", "")
        english_ability = ENG_MAP.get(eng_code) if eng_code and not eng_code.startswith("b") else None

        # Housing — joined from HH file by SERIALNO
        hh = hh_housing.get(r.get("SERIALNO", ""), {})
        ten_code = hh.get("TEN", "")
        tenure = TEN_MAP.get(ten_code) if ten_code and not ten_code.startswith("b") else None
        try: home_value = int(hh.get("VALP", "") or 0)
        except ValueError: home_value = 0
        try: monthly_rent = int(hh.get("RNTP", "") or 0)
        except ValueError: monthly_rent = 0
        try: bedrooms = int(hh.get("BDSP", "") or 0)
        except ValueError: bedrooms = 0

        rows.append([
            age, sex,
            intern(races_dict, race),
            intern(states_dict, state),
            intern(edu_dict, edu),
            intern(mar_dict, mar),
            intern(occ_dict, occupation),
            intern(emp_dict, employment),
            income, wages, own_kids, rel,
            hh_income, hh_others,
            intern(fod_dict, field_of_degree),
            intern(ind_dict, industry),
            1 if is_veteran else 0,
            1 if is_active_duty else 0,
            1 if has_disability else 0,
            intern(cit_dict, citizenship),
            yoep,
            intern(lang_dict, language),
            intern(eng_dict, english_ability),
            intern(ten_dict, tenure),
            home_value, monthly_rent, bedrooms,
            first_name,
        ])

    def invert(d):
        out = [None] * len(d)
        for v, i in d.items(): out[i] = v
        return out

    payload = {
        "fields": [
            "age","sex","race","state","education","marital","occupation","employment",
            "income","wages","own_kids","relshipp","hh_income","hh_members",
            "field_of_degree","industry","is_veteran","is_active_duty","has_disability",
            "citizenship","year_of_entry","language","english_ability","tenure",
            "home_value","monthly_rent","bedrooms",
            "first_name",
        ],
        "member_fields": ["age","sex","race","occupation","employment","relshipp","income"],
        "races": invert(races_dict),
        "states": invert(states_dict),
        "educations": invert(edu_dict),
        "marital": invert(mar_dict),
        "occupations": invert(occ_dict),
        "employments": invert(emp_dict),
        "fields_of_degree": invert(fod_dict),
        "industries": invert(ind_dict),
        "citizenships": invert(cit_dict),
        "languages": invert(lang_dict),
        "english_abilities": invert(eng_dict),
        "tenures": invert(ten_dict),
        "rows": rows,
    }

    with open(DATA_JSON, "w") as f:
        json.dump(payload, f, separators=(",", ":"))
    with open(DATA_JS, "w") as f:
        f.write("window.PUMS = ")
        json.dump(payload, f, separators=(",", ":"))
        f.write(";\n")
    sys.stderr.write(f"Wrote {DATA_JSON} ({os.path.getsize(DATA_JSON):,} bytes)\n")
    sys.stderr.write(f"Wrote {DATA_JS} ({os.path.getsize(DATA_JS):,} bytes)\n")
    sys.stderr.write(f"  occupations: {len(occ_dict)}, states: {len(states_dict)}, races: {len(races_dict)}\n")


if __name__ == "__main__":
    main()
