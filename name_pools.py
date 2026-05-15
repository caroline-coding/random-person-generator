"""Hand-curated foreign first/last name pools used by build_data.py.

Each entry has 'M' (male first names), 'F' (female first names), and 'L' (last names).
Pools are intentionally short and reach for "recognizably common" rather than
encyclopedic coverage. LANP_TO_LANG maps ACS PUMS language codes to keys here.
"""

LANG_NAMES = {
    # === Original 17 from prior commit ===
    "Spanish": {
        "M": ["Jose","Juan","Carlos","Miguel","Luis","Antonio","Pedro","Javier","Jorge","Manuel","Francisco","Roberto","Diego","Sergio","Eduardo","Alejandro","Ricardo","Fernando","Hector","Daniel","Mateo","Sebastian","Pablo","Andres","Mario","Rafael","Ramon","Esteban","Cristian","Felipe"],
        "F": ["Maria","Ana","Lucia","Carmen","Sofia","Isabel","Rosa","Elena","Patricia","Gloria","Sandra","Mariana","Adriana","Daniela","Camila","Gabriela","Valentina","Diana","Andrea","Veronica","Beatriz","Catalina","Claudia","Cristina","Esperanza","Guadalupe","Luisa","Mercedes","Pilar","Yolanda"],
        "L": ["Garcia","Rodriguez","Martinez","Hernandez","Lopez","Gonzalez","Perez","Sanchez","Ramirez","Torres","Flores","Rivera","Gomez","Diaz","Cruz","Reyes","Morales","Ortiz","Gutierrez","Chavez","Ramos","Ruiz","Alvarez","Mendoza","Vasquez","Castillo","Jimenez","Moreno","Romero","Herrera"],
    },
    "Chinese": {
        "M": ["Wei","Ming","Hao","Jun","Chen","Zhi","Bo","Cheng","Feng","Gang","Hong","Jian","Lei","Liang","Long","Peng","Qiang","Tao","Wen","Xin","Yang","Yi","Yong","Zhen","Kai","Xiao","Bin","Hua"],
        "F": ["Mei","Hui","Lin","Min","Ling","Hua","Yan","Xia","Fang","Li","Na","Ying","Juan","Jing","Hong","Ping","Qing","Wen","Xue","Yu","Yao","Zhen","Shu","Lan","Jie","Xin","Yun"],
        "L": ["Wang","Li","Zhang","Liu","Chen","Yang","Huang","Zhao","Wu","Zhou","Xu","Sun","Ma","Zhu","Hu","Guo","He","Gao","Lin","Luo","Song","Zheng","Xie","Han","Liang"],
    },
    "Tagalog": {
        "M": ["Jose","Juan","Mario","Antonio","Manuel","Eduardo","Ramon","Carlos","Pedro","Felipe","Jaime","Andres","Francisco","Pablo","Roberto","Vicente","Alfredo","Domingo","Reynaldo","Romeo","Rodrigo","Renato"],
        "F": ["Maria","Cristina","Ana","Rosa","Carmen","Teresa","Josefina","Elena","Margarita","Aurora","Imelda","Corazon","Mercedes","Lourdes","Norma","Linda","Eva","Estrella","Pilar","Concepcion"],
        "L": ["Santos","Reyes","Cruz","Bautista","Garcia","Mendoza","Castillo","Dela Cruz","Aquino","Ramos","Gonzales","Aguilar","Marcos","Lim","Tan","Sy","Co","Ang","Rivera","Castro","Domingo","Villanueva","Pascual","Soriano"],
    },
    "Vietnamese": {
        "M": ["An","Bao","Binh","Cuong","Dat","Dung","Duc","Duy","Hai","Hieu","Hoang","Hung","Khoa","Kien","Long","Minh","Nam","Phong","Phuc","Quang","Son","Tan","Thanh","Thinh","Tien","Tuan","Tung","Vinh","Vu"],
        "F": ["An","Anh","Bich","Diem","Diep","Dung","Giang","Ha","Hanh","Hien","Hoa","Hong","Huong","Lan","Linh","Mai","My","Nga","Ngoc","Nhi","Phuong","Quynh","Tam","Thao","Thu","Trang","Trinh","Tuyet","Yen"],
        "L": ["Nguyen","Tran","Le","Pham","Hoang","Phan","Vu","Vo","Dang","Bui","Do","Ho","Ngo","Duong","Ly","Truong","Dinh","Mai","Cao","Dao"],
    },
    "Korean": {
        "M": ["Min-jun","Ji-ho","Seo-jun","Do-yoon","Hyun-woo","Joon-ho","Sung-min","Tae-hyun","Yong-ho","Jin-woo","Sang-min","Min-soo","Jae-hyun","Hyun-jin","Jong-su","Kyung-soo","Dong-hyun","Seung-hyun","Woo-jin","Joon-young"],
        "F": ["So-young","Min-ji","Ji-eun","Hye-jin","Ji-yeon","Eun-ji","Soo-young","Ji-min","Eun-jung","Hae-won","Sun-hee","Hyun-jung","Mi-young","Su-jin","Yu-jin","Hye-won","Mi-na","Soo-jin","Ji-hye","Eun-young"],
        "L": ["Kim","Lee","Park","Choi","Jung","Kang","Cho","Yoon","Jang","Lim","Han","Oh","Seo","Shin","Kwon","Hwang","Ahn","Song","Yoo","Hong"],
    },
    "Arabic": {
        "M": ["Mohammed","Ahmed","Ali","Hassan","Omar","Khaled","Ibrahim","Mahmoud","Mustafa","Abdullah","Yusuf","Hussein","Karim","Amir","Tariq","Samir","Bilal","Faisal","Ziad","Nasser","Walid","Hisham","Rashid"],
        "F": ["Fatima","Aisha","Amina","Mariam","Layla","Noor","Yasmin","Zaynab","Khadija","Salma","Rania","Hala","Lina","Nour","Sara","Dalia","Reem","Farah","Nadia","Huda","Hanan"],
        "L": ["Al-Hassan","Hassan","Ahmed","Ali","Hussein","Mohammed","Ibrahim","Mahmoud","Saleh","Rahman","Aziz","Karim","Said","Mansour","Najjar","Haddad","Khoury","Saab","Khalil","Farah","Nasser","Rashid","Hakim","Aboud"],
    },
    "Russian": {
        "M": ["Ivan","Alexander","Sergei","Dmitri","Vladimir","Andrei","Mikhail","Nikolai","Pavel","Anton","Maxim","Igor","Yuri","Boris","Viktor","Alexei","Konstantin","Roman","Stanislav","Artem","Oleg","Vadim","Yevgeny"],
        "F": ["Anna","Maria","Elena","Olga","Natalia","Tatiana","Irina","Yulia","Ekaterina","Svetlana","Ludmila","Galina","Marina","Sofia","Anastasia","Daria","Vera","Polina","Nadezhda","Valentina","Lyudmila","Oksana"],
        "L": ["Ivanov","Smirnov","Kuznetsov","Popov","Sokolov","Lebedev","Kozlov","Novikov","Morozov","Petrov","Volkov","Solovyov","Vasilyev","Zaitsev","Pavlov","Semenov","Golubev","Vinogradov","Bogdanov","Vorobyev"],
    },
    "Portuguese": {
        "M": ["Joao","Jose","Antonio","Manuel","Francisco","Carlos","Paulo","Pedro","Luis","Marco","Bruno","Andre","Tiago","Rafael","Daniel","Diego","Eduardo","Fernando","Gabriel","Henrique","Ricardo","Joaquim"],
        "F": ["Maria","Ana","Beatriz","Carla","Catarina","Cristina","Daniela","Helena","Isabel","Joana","Lara","Leonor","Mariana","Patricia","Rita","Sandra","Sofia","Teresa","Vanessa","Adriana"],
        "L": ["Silva","Santos","Pereira","Costa","Rodrigues","Martins","Carvalho","Ferreira","Almeida","Lopes","Oliveira","Sousa","Souza","Fernandes","Gomes","Cardoso","Ribeiro","Mendes","Castro","Araujo"],
    },
    "French": {
        "M": ["Jean","Pierre","Michel","Louis","Henri","Marc","Philippe","Antoine","Bernard","Christian","Daniel","Francois","Georges","Jacques","Laurent","Maurice","Olivier","Patrick","Raymond","Stephane","Thierry"],
        "F": ["Marie","Jeanne","Francoise","Catherine","Isabelle","Sylvie","Nicole","Brigitte","Christine","Martine","Sophie","Helene","Anne","Claire","Camille","Celine","Charlotte","Delphine","Emma","Julie"],
        "L": ["Martin","Bernard","Dubois","Thomas","Robert","Petit","Durand","Leroy","Moreau","Simon","Laurent","Lefebvre","Bertrand","Roux","Vincent","Fournier","Girard","Bonnet","Dupont","Lambert"],
    },
    "Haitian": {
        "M": ["Jean","Pierre","Marc","Jacques","Michel","Joseph","Daniel","Frantz","Wilson","Patrick","Edwin","Edner","Yves","Ronald","Reynold","Junior","Wendell","Marcel","Garry","Fritz"],
        "F": ["Marie","Yolette","Nadege","Carmel","Magalie","Ginette","Rose","Therese","Marlene","Sonia","Wideline","Yvonne","Edith","Solange","Suzette","Mireille","Marjorie","Fabiola","Daphnee"],
        "L": ["Pierre","Jean-Baptiste","Saint-Louis","Joseph","Charles","Louis","Antoine","Augustin","Casimir","Cherubin","Cherestal","Civil","Constant","Eustache","Fontaine","Etienne","Francois","Andre","Bernard"],
    },
    "Japanese": {
        "M": ["Hiroshi","Takeshi","Yuki","Akira","Kenji","Daisuke","Hiroki","Kazuki","Kenta","Naoki","Ryo","Shota","Takashi","Tomohiro","Yusuke","Sho","Taichi","Yuto","Kazuya","Masato"],
        "F": ["Yuki","Yuko","Yumiko","Sakura","Kaori","Naoko","Mariko","Megumi","Aiko","Akiko","Asuka","Chika","Eri","Hana","Hiroko","Kanako","Keiko","Kumiko","Mayumi","Miho","Sayaka","Tomoko"],
        "L": ["Sato","Suzuki","Takahashi","Tanaka","Watanabe","Ito","Yamamoto","Nakamura","Kobayashi","Kato","Yoshida","Yamada","Sasaki","Yamaguchi","Saito","Matsumoto","Inoue","Kimura","Hayashi","Shimizu"],
    },
    "Polish": {
        "M": ["Jan","Andrzej","Krzysztof","Stanislaw","Tadeusz","Piotr","Pawel","Marek","Jerzy","Tomasz","Jakub","Mateusz","Wojciech","Marcin","Michal","Adam","Lukasz","Filip","Bartosz","Maciej"],
        "F": ["Anna","Maria","Katarzyna","Malgorzata","Agnieszka","Krystyna","Barbara","Ewa","Joanna","Magdalena","Elzbieta","Zofia","Teresa","Halina","Janina","Aleksandra","Karolina","Natalia","Monika","Beata"],
        "L": ["Nowak","Kowalski","Wisniewski","Wojcik","Kowalczyk","Kaminski","Lewandowski","Zielinski","Szymanski","Wozniak","Dabrowski","Kozlowski","Jankowski","Mazur","Wojciechowski","Kwiatkowski","Krawczyk","Kaczmarek","Piotrowski"],
    },
    "Italian": {
        "M": ["Giuseppe","Giovanni","Antonio","Mario","Luigi","Francesco","Angelo","Vincenzo","Pietro","Salvatore","Carlo","Franco","Domenico","Roberto","Alessandro","Marco","Davide","Luca","Andrea","Simone"],
        "F": ["Maria","Anna","Giuseppina","Rosa","Angela","Giovanna","Teresa","Lucia","Antonietta","Maddalena","Margherita","Caterina","Carmela","Concetta","Francesca","Vittoria","Vincenza","Carla","Federica","Laura"],
        "L": ["Rossi","Russo","Ferrari","Esposito","Bianchi","Romano","Colombo","Ricci","Marino","Greco","Bruno","Gallo","Conti","De Luca","Mancini","Costa","Giordano","Rizzo","Lombardi","Moretti"],
    },
    "German": {
        "M": ["Hans","Peter","Klaus","Wolfgang","Jurgen","Walter","Helmut","Heinz","Friedrich","Werner","Dieter","Manfred","Thomas","Andreas","Michael","Stefan","Jens","Markus","Sebastian","Christian"],
        "F": ["Maria","Anna","Petra","Sabine","Birgit","Christa","Brigitte","Helga","Renate","Ursula","Monika","Karin","Hannelore","Doris","Ingrid","Susanne","Andrea","Claudia","Stefanie","Nicole"],
        "L": ["Muller","Schmidt","Schneider","Fischer","Weber","Meyer","Wagner","Becker","Schulz","Hoffmann","Schafer","Koch","Bauer","Richter","Klein","Wolf","Schroder","Neumann","Schwarz","Zimmermann"],
    },
    "Persian": {
        "M": ["Mohammad","Ali","Reza","Hossein","Amir","Mehdi","Hamid","Ahmad","Saeed","Behrouz","Bijan","Bahram","Cyrus","Darius","Farzad","Hooman","Kamran","Kaveh","Pejman","Shahram"],
        "F": ["Fatima","Zahra","Maryam","Sara","Setareh","Shirin","Soraya","Yasaman","Roya","Mehri","Mahsa","Leila","Nazanin","Niloufar","Parisa","Roxana","Shadi","Shaghayegh","Shahla","Tara"],
        "L": ["Khan","Mohammadi","Hosseini","Karimi","Ahmadi","Rahimi","Rezaei","Mousavi","Tehrani","Esfahani","Yazdi","Shirazi","Razavi","Bahrami","Farahani","Jafari","Kamali","Naderi","Rashidi"],
    },
    "Greek": {
        "M": ["Georgios","Yiannis","Konstantinos","Dimitrios","Nikolaos","Christos","Panagiotis","Athanasios","Vasileios","Spyridon","Stavros","Anastasios","Andreas","Apostolos","Pavlos","Kostas","Theodoros","Petros","Manolis"],
        "F": ["Maria","Eleni","Aikaterini","Vasiliki","Dimitra","Sophia","Anna","Ioanna","Konstantina","Despina","Christina","Athanasia","Stavroula","Athina","Evangelia","Aphrodite","Penelope","Olympia"],
        "L": ["Papadopoulos","Papandreou","Georgiou","Demetriou","Christodoulou","Karagiannis","Constantinou","Nikolaou","Andreou","Antoniou","Vlachos","Pavlou","Stavrou","Ioannou","Petrou","Markou"],
    },

    # === New languages this commit ===
    "Armenian": {
        "M": ["Aram","Artur","Davit","Edgar","Garegin","Gevorg","Hayk","Karen","Levon","Mher","Narek","Sargis","Tigran","Vahan","Vahe","Vardan","Arman","Suren","Hovhannes","Khachatur","Aleksan","Gor","Petros","Stepan","Smbat"],
        "F": ["Anahit","Anush","Arev","Armine","Astghik","Diana","Gohar","Hasmik","Karine","Lilit","Lusine","Mariam","Mary","Nare","Nelli","Nune","Satenik","Sirarpi","Sona","Susanna","Tamara","Tatevik","Varduhi","Zaruhi","Ani"],
        "L": ["Hakobyan","Petrosyan","Avetisyan","Grigoryan","Sarkisyan","Mkrtchyan","Hovhannisyan","Karapetyan","Manukyan","Vardanyan","Khachatryan","Sahakyan","Martirosyan","Ghazaryan","Tovmasyan","Kazaryan","Aslanyan","Adamyan","Antonyan"],
    },
    "Igbo": {
        "M": ["Chinedu","Chukwuma","Ikenna","Obinna","Emeka","Uche","Nnamdi","Chibuzo","Kelechi","Chima","Chidi","Ifeanyi","Tochukwu","Nwabueze","Okechukwu","Ebuka","Onyeka","Ekene","Nkemdirim","Chuks","Chibueze","Chiagozie"],
        "F": ["Adaeze","Chinonso","Chiamaka","Ngozi","Uchechi","Amara","Ifunanya","Obioma","Onyinye","Ezinne","Chinasa","Chinwe","Ada","Nkechi","Ifeoma","Nneka","Chioma","Olisa","Nwakaego","Chizoba","Adaobi","Adanna"],
        "L": ["Okafor","Eze","Nnamdi","Obi","Nwosu","Okonkwo","Okeke","Anyanwu","Onyeka","Igwe","Ikenna","Chukwu","Onyekwere","Anaeto","Okoli","Madu","Uzoma","Iwu","Ohaegbu","Onuoha","Nwoke"],
    },
    "Yoruba": {
        "M": ["Adebayo","Adekunle","Olumide","Babatunde","Olusegun","Akinwale","Ayodeji","Femi","Tunde","Wale","Kunle","Sola","Tope","Bayo","Funso","Olu","Seun","Yemi","Oluwaseun","Adesoji","Oluwafemi","Oluwadamilare"],
        "F": ["Adunni","Folake","Funmilayo","Yetunde","Bolanle","Toyin","Bisi","Mojisola","Iyabo","Kemi","Nike","Sade","Tola","Yejide","Olubunmi","Folashade","Foluke","Adeola","Tope","Olamide","Ronke","Funke"],
        "L": ["Adeyemi","Ogundimu","Akinyemi","Adesanya","Babatunde","Oluwole","Ayodele","Adeniyi","Adesina","Ojo","Olatunji","Akande","Olawale","Akinola","Olukoga","Adesoji","Bamidele","Adebanjo","Aderibigbe","Oyelaran","Falade"],
    },
    "Somali": {
        "M": ["Mohamed","Abdi","Ahmed","Ali","Omar","Ibrahim","Hassan","Yusuf","Abdullahi","Ismail","Abdulkadir","Hussein","Mahad","Said","Bashir","Farah","Khalid","Suleiman","Liban","Abdirahman","Mustafa","Sharmarke"],
        "F": ["Amina","Fadumo","Halima","Hodan","Khadija","Maryan","Najma","Nasra","Hawa","Fatuma","Zahra","Ifrah","Munira","Sahra","Sumaya","Asha","Idil","Anab","Faduma","Hibo","Deqa","Ruun"],
        "L": ["Mohamed","Hassan","Ali","Ahmed","Abdi","Omar","Ibrahim","Yusuf","Farah","Adan","Aden","Warsame","Hashi","Egal","Issa","Ismail","Diriye","Said","Jama","Roble","Hirsi"],
    },
    "Hmong": {
        "M": ["Tou","Pao","Vang","Kao","Chong","Cheng","Yia","Bee","Kong","Long","Mai","Mee","Nou","Pa","Phong","Toua","Tong","Xao","Xay","Yer","Choua","Neng","Yeng","Vang","Sou"],
        "F": ["Mai","Pang","Mee","Yer","Chia","Choua","Houa","Kalia","Kia","Maiv","Nia","Pa","See","Shoua","Va","Vang","Ying","Zoua","Mim","Maika","Yia"],
        "L": ["Vang","Yang","Xiong","Lee","Lor","Thao","Moua","Vue","Cha","Her","Khang","Ly","Hang","Heu","Vu"],
    },
    "Tibetan": {
        "M": ["Tenzin","Tashi","Pema","Lobsang","Sonam","Dorjee","Karma","Norbu","Phuntsok","Wangchuk","Sherab","Jampa","Choden","Ngawang","Thubten","Jigme","Yeshi","Kalsang","Dawa"],
        "F": ["Tenzin","Tsering","Yangchen","Choden","Pema","Dolma","Lhamo","Yangzom","Dechen","Wangmo","Sangmo","Norzom","Sonam","Tashi","Drolma","Kunsang"],
        "L": ["Tashi","Tenzin","Wangchuk","Dorjee","Tsering","Sherpa","Lama","Bhutia","Choden","Norbu","Lhamo","Phuntsok","Yangzom","Pema","Wangmo"],
    },
    "Swahili": {
        "M": ["Juma","Hassan","Ali","Said","Mussa","Salim","Omar","Bakari","Khalifa","Mohamed","Faraji","Jabari","Hamisi","Yusuf","Idris","Issa","Ramadhani","Mwalimu","Daudi","Hamza"],
        "F": ["Aisha","Fatuma","Asha","Zainabu","Mwanaisha","Halima","Mariamu","Salama","Amina","Nuru","Bahati","Furaha","Imani","Subira","Rehema","Tabitha","Saidah"],
        "L": ["Mohamed","Hassan","Said","Ali","Omar","Salim","Juma","Bakari","Issa","Mussa","Mwangi","Kamau","Otieno","Wanjiku","Mbeki","Karanja","Njoroge","Kariuki","Owino"],
    },
    "Amharic": {
        "M": ["Abebe","Bekele","Dawit","Daniel","Ephrem","Fikadu","Getachew","Habtamu","Henok","Mesfin","Selam","Solomon","Tadesse","Tesfaye","Yohannes","Yoseph","Abel","Abreham","Mulugeta","Eyob"],
        "F": ["Almaz","Birtukan","Eden","Eleni","Etenesh","Genet","Hanna","Hewan","Hirut","Mahlet","Mekdes","Meron","Sara","Selam","Tigist","Tirhas","Zewditu","Bethelhem","Rahel","Tsehay"],
        "L": ["Abebe","Bekele","Tadesse","Tesfaye","Getachew","Yohannes","Solomon","Daniel","Haile","Wolde","Worku","Kebede","Belay","Asfaw","Mengistu","Berhanu","Demissie","Girma"],
    },
    "Khmer": {
        "M": ["Sok","Sokhom","Chea","Vannak","Sopheap","Phany","Vichea","Borey","Pisey","Reaksmey","Visal","Chanthorn","Mony","Ponleu","Saroeun","Sambath","Touch","Veasna","Boran"],
        "F": ["Sreyna","Sreypov","Channary","Bopha","Sokhana","Theary","Vichara","Sotheary","Maly","Saroth","Lykheang","Phally","Ratha","Sopheak","Sreyleak","Sreymom","Sreyneath","Sokunthea"],
        "L": ["Sok","Chea","Sam","Chan","Heng","Khun","Kim","Lim","Long","Meas","Mok","Ouk","Phan","Phay","Pich","Por","Prak","Sao","Seng","So","Tang","Touch","Ung","Yim"],
    },
    "Thai": {
        "M": ["Somchai","Somsak","Surasak","Suwit","Sombat","Niran","Sutthi","Anan","Boonchai","Sakda","Krit","Wirat","Kraisak","Sunan","Phongchai","Apichat","Worawut","Chatchai","Akhom","Phairoj"],
        "F": ["Siriporn","Wassana","Malee","Suchada","Wanida","Pailin","Kanya","Saowapa","Wanpen","Pranee","Sirinya","Nuanjan","Suphaphan","Patcharin","Yupin","Anong","Ratchada","Naree","Nantana"],
        "L": ["Saetang","Saetan","Sukhum","Sripong","Wongsa","Wongchai","Chaiyaporn","Wong","Phimphathana","Khamphakdi","Thongchai","Phimphat","Boonpot","Sutthikiat","Charoenchai","Songkhla","Suriya","Ratanapakdee","Phromjak"],
    },
    "Hebrew": {
        "M": ["David","Daniel","Michael","Yosef","Yehoshua","Avraham","Yitzhak","Yaakov","Moshe","Aharon","Eliyahu","Shmuel","Yehuda","Binyamin","Naftali","Asher","Reuven","Shimon","Levi","Mordechai","Yair","Itamar"],
        "F": ["Sarah","Rivka","Rachel","Leah","Miriam","Devorah","Esther","Shoshana","Tziporah","Hadassah","Yael","Yehudit","Naomi","Avigail","Ruth","Talia","Maya","Noa","Tamar","Liora","Ariella","Shira"],
        "L": ["Cohen","Levi","Mizrahi","Peretz","Biton","Avraham","Friedman","Goldberg","Rosen","Klein","Katz","Adler","Stern","Schwartz","Weiss","Berman","Eisenberg","Goldstein","Greenberg","Rubin"],
    },
    "Yiddish": {
        "M": ["Avrum","Yankel","Mendel","Berel","Hershel","Chaim","Shlomo","Yitzchok","Moishe","Dovid","Pinchas","Velvel","Zalman","Tzvi","Hersh","Mottel","Naftoli","Yossel","Reuven"],
        "F": ["Rivka","Yenta","Bracha","Faiga","Chana","Gittel","Esther","Sura","Leah","Miriam","Devorah","Yocheved","Pesha","Shaindel","Toba","Rifka","Rachel","Reizel"],
        "L": ["Cohen","Levin","Greenberg","Goldberg","Schwartz","Weinstein","Friedman","Bernstein","Steinberg","Goldstein","Katz","Rosenberg","Silverman","Klein","Stern","Weiss","Adler","Lipschitz","Rosenbaum","Rabinowitz"],
    },
    "Hungarian": {
        "M": ["Laszlo","Istvan","Sandor","Janos","Jozsef","Mihaly","Ferenc","Karoly","Tibor","Zoltan","Andras","Gabor","Imre","Bela","Attila","Gyorgy","Peter","Zsolt","Daniel","Akos"],
        "F": ["Maria","Erzsebet","Eszter","Anna","Katalin","Ildiko","Edit","Aniko","Klara","Krisztina","Adrienn","Reka","Boglarka","Brigitta","Csilla","Eniko","Henrietta","Judit","Veronika","Zita"],
        "L": ["Nagy","Kovacs","Toth","Szabo","Horvath","Varga","Kiss","Molnar","Nemeth","Farkas","Balogh","Papp","Takacs","Juhasz","Lakatos","Meszaros","Olah","Simon","Racz","Fekete"],
    },
    "Ukrainian": {
        "M": ["Oleksandr","Mykhailo","Volodymyr","Yuriy","Ivan","Vasyl","Mykola","Petro","Andriy","Serhiy","Roman","Bohdan","Taras","Maksym","Pavlo","Stepan","Vadym","Vitaliy","Yaroslav","Anton"],
        "F": ["Olha","Tetyana","Iryna","Oksana","Anna","Yuliya","Mariya","Natalya","Olena","Hanna","Lyudmyla","Halyna","Svitlana","Larysa","Lyubov","Kateryna","Valeriya","Yelyzaveta","Daryna","Sofiya"],
        "L": ["Melnyk","Shevchenko","Kovalenko","Bondarenko","Tkachenko","Boyko","Kovalchuk","Kravchenko","Oliynyk","Shevchuk","Polishchuk","Marchenko","Moroz","Lysenko","Savchenko"],
    },
    "Romanian": {
        "M": ["Andrei","Alexandru","Mihai","Ion","Ioan","Vasile","Constantin","Gheorghe","Daniel","Cristian","Florin","Marius","Adrian","Bogdan","Catalin","Cosmin","Dan","Dragos","Eduard","Florentin","Sergiu"],
        "F": ["Maria","Elena","Ioana","Ana","Andreea","Alexandra","Cristina","Daniela","Diana","Florentina","Gabriela","Georgiana","Lavinia","Mihaela","Monica","Roxana","Simona","Stefania","Teodora"],
        "L": ["Popa","Popescu","Ionescu","Stoica","Stan","Constantin","Marin","Munteanu","Gheorghiu","Tudor","Dumitrescu","Niculescu","Radu","Vasiliu","Anghel","Florea","Iliescu","Petrescu"],
    },

    # === Indian-subcontinent languages, split from previous catch-all "Hindi" ===
    "Hindi": {
        "M": ["Raj","Ravi","Amit","Vijay","Sanjay","Anil","Sunil","Ramesh","Suresh","Mahesh","Dinesh","Arjun","Akash","Rohan","Rohit","Karan","Aditya","Vikram","Pradeep","Manoj","Rakesh","Anand","Ashok","Mohan","Deepak","Sachin","Rajesh","Krishna","Naveen","Praveen"],
        "F": ["Priya","Anjali","Pooja","Sunita","Kavita","Asha","Rekha","Geeta","Lakshmi","Meera","Radha","Sita","Anita","Indira","Maya","Neha","Riya","Diya","Ananya","Aditi","Tara","Padma","Shanti","Deepa","Shilpa","Kavya","Saraswati","Parvati"],
        "L": ["Sharma","Verma","Singh","Kumar","Gupta","Joshi","Tiwari","Mishra","Yadav","Pandey","Saxena","Chandra","Agarwal","Bhatt","Kapoor","Chopra","Malhotra","Khurana","Bansal","Garg","Mehta","Aggarwal","Dixit","Rastogi","Srivastava"],
    },
    "Urdu": {
        "M": ["Muhammad","Ali","Ahmed","Hassan","Hussain","Bilal","Faisal","Umar","Usman","Imran","Shahid","Tariq","Asif","Adnan","Akbar","Amir","Bashir","Farooq","Hamid","Iqbal","Junaid","Kamran","Naseem","Nadeem","Rashid","Shahbaz","Tahir","Waqas","Yasir","Zafar"],
        "F": ["Aisha","Fatima","Khadija","Maryam","Zara","Saba","Sana","Hira","Nadia","Rabia","Sadia","Farah","Mehreen","Nazia","Nida","Samina","Sumera","Yasmin","Zainab","Bushra","Rukhsana","Shazia","Tahira"],
        "L": ["Khan","Malik","Sheikh","Chaudhry","Ahmed","Ali","Hussain","Raza","Iqbal","Aslam","Rafiq","Akhtar","Mahmood","Bhatti","Aziz","Saleem","Hashmi","Qureshi","Siddiqui","Awan","Butt","Ashraf"],
    },
    "Bengali": {
        "M": ["Rahim","Rakib","Rafi","Hossain","Karim","Nazrul","Salah","Tanvir","Shahidul","Mizanur","Anwar","Ashraf","Mahbub","Mostofa","Bishwajit","Debashish","Pranab","Sanjay","Subir","Tapan","Sumon","Niloy","Abir","Arif"],
        "F": ["Roksana","Nasrin","Nazma","Salma","Sumaya","Rumana","Tanjila","Anika","Mim","Sneha","Mou","Ananya","Sharmin","Dipa","Sumi","Tahmina","Nilufa","Suchitra","Anwara","Farida"],
        "L": ["Khan","Ahmed","Hossain","Rahman","Islam","Chowdhury","Karim","Sheikh","Mondal","Das","Mukherjee","Chakraborty","Bhattacharya","Sen","Ghosh","Dutta","Roy","Banerjee","Saha","Pal","Bose","Ganguly"],
    },
    "Punjabi": {
        "M": ["Gurpreet","Gurdeep","Jaspreet","Harpreet","Manpreet","Amrit","Gurbir","Inderjit","Jagdeep","Karandeep","Lakhwinder","Mandeep","Navdeep","Paramjit","Rajinder","Ravinder","Sandeep","Sukhdev","Tarlochan","Varinder","Balwinder","Hardeep","Kuldeep","Sukhwinder","Surinder","Jasvinder","Davinder"],
        "F": ["Gurpreet","Harpreet","Manpreet","Jasmeet","Amrit","Sukhdeep","Rajwinder","Surinder","Kulwinder","Jagdeep","Navdeep","Sandeep","Simran","Maninder","Inderjit","Baljit","Jagjit","Pavandeep","Charanjit","Jasleen","Manjit"],
        "L": ["Singh","Kaur","Gill","Sandhu","Sidhu","Brar","Dhillon","Mann","Sekhon","Bains","Cheema","Sodhi","Sahota","Bhatti","Saini","Bedi","Khera","Grewal","Atwal","Virk","Bajwa","Aulakh"],
    },
    "Marathi": {
        "M": ["Ajit","Anil","Arvind","Ashok","Bhalchandra","Chandrakant","Datta","Ganesh","Gopal","Hemant","Jayesh","Kiran","Madhav","Mahesh","Manohar","Mukund","Narayan","Nilesh","Pradeep","Pramod","Prasad","Pravin","Rajendra","Ramesh","Sachin","Sanjeev","Shantanu","Shrikant","Subhash","Sudhakar"],
        "F": ["Aditi","Anita","Aparna","Asha","Bhakti","Chitra","Deepa","Geeta","Hemlata","Jaya","Kalpana","Lata","Madhuri","Manisha","Meena","Mukta","Padma","Pradnya","Pratibha","Priti","Rama","Rekha","Sangeeta","Shalini","Shubha","Smita","Sneha","Sunita","Suvarna","Swati"],
        "L": ["Patil","Joshi","Deshmukh","Kulkarni","Desai","Deshpande","Bhosale","Naik","Jadhav","Pawar","Shinde","Pandit","Apte","Phadke","Bedekar","Tendulkar","Ranade","Marathe","Sane","Kale","Karandikar"],
    },
    "Gujarati": {
        "M": ["Amit","Arun","Bharat","Bhavin","Chandra","Devang","Dilip","Hardik","Hasmukh","Hemant","Jagdish","Jay","Jignesh","Kalpesh","Ketan","Krishna","Mahendra","Mehul","Mukesh","Naresh","Nikhil","Nitin","Pankaj","Paresh","Pradeep","Prakash","Prashant","Pravin","Ramesh","Sanjay"],
        "F": ["Anjali","Bharti","Bina","Daxa","Dipti","Disha","Falguni","Hemali","Jagruti","Kalpana","Komal","Krupali","Manisha","Meena","Mital","Nidhi","Nisha","Nita","Pinal","Pooja","Pratiksha","Priya","Rekha","Reshma","Rina","Sandhya","Shilpa","Smita","Sneha","Sweta"],
        "L": ["Patel","Shah","Modi","Mehta","Desai","Joshi","Bhatt","Trivedi","Vyas","Pandya","Parekh","Sheth","Doshi","Gandhi","Kothari","Mistry","Pandit","Sanghvi","Soni","Thakkar","Shukla"],
    },
    "Nepali": {
        "M": ["Suresh","Ramesh","Prakash","Rajesh","Bishnu","Krishna","Hari","Govinda","Rabindra","Nabin","Nirmal","Manoj","Sanjeev","Dipendra","Sushil","Anil","Ganesh","Mahesh","Pradeep","Rajan","Roshan","Sandeep","Sunil","Surya","Tika","Tilak","Bikram","Bishal","Niraj"],
        "F": ["Sita","Maya","Sarita","Sangita","Lakshmi","Saraswati","Parbati","Bishnu","Kalpana","Manju","Nani","Indra","Bimala","Gita","Goma","Jamuna","Kamala","Kamana","Laxmi","Punam","Pushpa","Rita","Rina","Sumitra","Susmita","Sweta"],
        "L": ["Shrestha","Sharma","Adhikari","Thapa","Karki","Bhattarai","Pokharel","Rai","Limbu","Gurung","Magar","Tamang","Khadka","Bhandari","Gautam","Kafle","Pandey","Pant","Rana","Subedi","Acharya","Dahal"],
    },
    "Telugu": {
        "M": ["Anand","Anil","Aravind","Arjun","Ashok","Bharath","Chandra","Chandrashekar","Eshwar","Ganesh","Gopal","Hari","Kalyan","Karthik","Krishna","Madhu","Mahesh","Manohar","Murali","Naga","Narayana","Naveen","Praveen","Raghav","Rajesh","Ramana","Ravi","Sai","Sandeep","Sridhar","Srinivas","Suresh","Venkat"],
        "F": ["Anjali","Bhavani","Deepika","Divya","Geeta","Jayalakshmi","Kavya","Lakshmi","Madhavi","Mounika","Padmaja","Padmavati","Parvati","Priya","Radha","Rajeswari","Ramya","Renuka","Rohini","Sandhya","Saritha","Saraswati","Sirisha","Sita","Sridevi","Subhadra","Sunitha","Swathi","Vasundhara","Vijaya"],
        "L": ["Reddy","Naidu","Rao","Choudhary","Sastry","Verma","Murthy","Krishna","Prasad","Bhaskar","Suresh","Ramana","Subba","Yadav","Acharya","Iyengar","Mallik","Goud","Setty","Sharma","Varma","Pillai"],
    },
    "Kannada": {
        "M": ["Anand","Ashwin","Bharath","Chandru","Deepak","Dheeraj","Ganesh","Girish","Harish","Karthik","Kiran","Madhav","Manjunath","Mohan","Murali","Narayan","Naveen","Nikhil","Pradeep","Prakash","Prashanth","Raghu","Rajesh","Ramesh","Ravi","Sandeep","Santhosh","Shashi","Srinivas","Subramanya","Sudhakar","Vasanth","Venkat"],
        "F": ["Anjali","Anu","Bhavani","Chaitra","Deepa","Divya","Geeta","Indu","Jaya","Kavya","Lakshmi","Lavanya","Madhavi","Manjula","Meera","Nalini","Nandini","Padma","Pavithra","Pooja","Priya","Radha","Rama","Saraswati","Shashikala","Sheela","Sneha","Sumitra","Suma","Vidya","Vijaya"],
        "L": ["Gowda","Hegde","Bhat","Shastri","Rao","Patil","Naidu","Acharya","Achar","Joshi","Murthy","Shenoy","Pai","Kamath","Kulkarni","Bangera","Kotian","Salian","Mallya","Hebbar","Heggade","Aithal"],
    },
    "Malayalam": {
        "M": ["Anish","Ajith","Anil","Anoop","Arjun","Arun","Bipin","Deepak","Dileep","Joseph","Kiran","Krishnan","Manoj","Mohan","Mohanan","Nair","Nikhil","Praveen","Rajan","Rajesh","Rajiv","Rakesh","Ranjith","Sajeev","Sajith","Sanjay","Santhosh","Sarath","Suresh","Sunil","Vinod","Vishnu"],
        "F": ["Aishwarya","Anitha","Anjali","Anu","Arya","Asha","Athira","Bindu","Deepa","Divya","Geetha","Jaya","Jisha","Kavya","Lakshmi","Latha","Mary","Meera","Nimisha","Nisha","Parvathy","Priya","Radhika","Rajalakshmi","Reshma","Rohini","Saira","Sangeetha","Saritha","Shilpa","Sindhu","Soumya","Sujatha"],
        "L": ["Nair","Menon","Pillai","Kurup","Panicker","Krishnan","Namboothiri","Bhattathiri","Mathai","Thomas","Joseph","Varghese","Mathew","Iyer","Ayyappan","Unnithan","Warrier","Kaimal","Marar"],
    },
    "Tamil": {
        "M": ["Anand","Aravind","Arjun","Arun","Balaji","Bharath","Chandra","Dinesh","Ganesh","Gopal","Hari","Karthik","Krishnan","Manoj","Mohan","Murali","Naveen","Prabhakar","Prakash","Pranav","Praveen","Raghav","Rahul","Rajesh","Ram","Ramesh","Ravi","Sanjay","Senthil","Shankar","Shiva","Sridhar","Srinivas","Suresh","Vijay"],
        "F": ["Aishwarya","Anjali","Bharathi","Chitra","Deepa","Divya","Gayathri","Geetha","Jaya","Kalaivani","Kalpana","Kanmani","Kavya","Lakshmi","Lavanya","Latha","Madhumitha","Malar","Meena","Nandini","Padma","Parvathi","Priya","Rajalakshmi","Radha","Rajeswari","Sangeetha","Saritha","Saraswathi","Shobha","Sumathi","Tamilarasi","Vidya"],
        "L": ["Iyer","Iyengar","Pillai","Mudaliar","Chettiar","Naidu","Krishnan","Subramanian","Raman","Ramachandran","Venkataraman","Balasubramanian","Natarajan","Ganesan","Sundaram","Murugan","Kannan","Selvam","Murthy","Sastri","Bhattachariar"],
    },
    "Sinhala": {
        "M": ["Asanga","Chamara","Dilshan","Dinesh","Gayan","Indika","Janaka","Kasun","Krishan","Lasith","Mahesh","Malith","Niroshan","Nuwan","Pasindu","Pradeep","Prasanna","Ranjith","Rohitha","Sajith","Sameera","Saman","Sanjeewa","Susantha","Tharindu","Thilak","Upul","Vimukthi"],
        "F": ["Amali","Anuradha","Chamari","Damayanthi","Dilini","Dinusha","Ganga","Hemamali","Hiranthi","Iresha","Janaki","Kanchana","Kumari","Kumudini","Lakmali","Lasanthi","Madara","Madhushani","Malsha","Nayanthara","Nilanthi","Niluka","Pavithra","Prabhashini","Sajini","Samanthi","Sandya","Saumya","Sashika","Sumudu"],
        "L": ["Silva","Perera","Fernando","Jayawardena","Wijesinghe","Bandara","Mendis","De Silva","Karunaratne","Senanayake","Wickramasinghe","Rajapaksa","Ratnayake","Ekanayake","Gunasekara","Liyanage","Wijeratne","Goonatilake","Hettiarachchi"],
    },
}


LANP_TO_LANG = {
    # Spanish
    "1200": "Spanish",
    # Chinese / Mandarin / Cantonese / Min Nan
    "1970": "Chinese", "2000": "Chinese", "2030": "Chinese", "2050": "Chinese",
    # Filipino languages -> Tagalog
    "2910": "Tagalog", "2920": "Tagalog", "2950": "Tagalog", "3150": "Tagalog", "3190": "Tagalog",
    # Vietnamese
    "1960": "Vietnamese",
    # Korean
    "2575": "Korean",
    # Arabic
    "4500": "Arabic",
    # Russian
    "1250": "Russian",
    # Portuguese
    "1210": "Portuguese",
    # French (incl. Cajun)
    "1170": "French", "1175": "French",
    # Haitian
    "1055": "Haitian",
    # Japanese
    "2560": "Japanese",
    # Polish
    "1270": "Polish",
    # Italian
    "1155": "Italian",
    # German (incl. Swiss, Pennsylvania)
    "1110": "German", "1120": "German", "1125": "German",
    # Persian / Farsi / Dari
    "1290": "Persian", "1292": "Persian",
    # Greek
    "1235": "Greek",
    # Armenian
    "1288": "Armenian",
    # African languages
    "6370": "Igbo",
    "6290": "Yoruba",
    "4840": "Somali",
    "5150": "Swahili",
    "4590": "Amharic",
    # Southeast Asian
    "2535": "Hmong",
    "2100": "Tibetan",
    "1900": "Khmer",
    "2430": "Thai",
    # Hebrew / Yiddish
    "4545": "Hebrew",
    "1130": "Yiddish",
    # European
    "1582": "Hungarian",
    "1260": "Ukrainian",
    "1220": "Romanian",
    # Indian subcontinent (split out from previous "Hindi" catch-all)
    "1340": "Hindi", "1350": "Hindi",  # India NEC + Hindi
    "1435": "Hindi",                    # Konkani -> Hindi pool (tiny)
    "1540": "Hindi",                    # Other Indo-Iranian -> Hindi pool
    "1360": "Urdu",
    "1380": "Bengali",
    "1420": "Punjabi",
    "1440": "Marathi",
    "1450": "Gujarati",
    "1500": "Nepali",
    "1530": "Sinhala",
    "1730": "Telugu",
    "1737": "Kannada",
    "1750": "Malayalam",
    "1765": "Tamil",
}
