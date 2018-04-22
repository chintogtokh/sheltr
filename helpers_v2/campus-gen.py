import json
import re
unis = ["AAPoly__AMI_Education",
"AAPoly__Melbourne_Campus",
"Academia_International__Melbourne_Campus",
"Acumen_Institute_of_Further_Education__CBD_Campus",
"Acumen_Institute_of_Further_Education__Richmond_Campus",
"AGB_Training__Geelong_Campus",
"ALACC_Health_College__Australia",
"Alfred_Deakin_College_(MIBT)__Waurn_Ponds_Campus",
"ALTEC_College__Melbourne_Campus",
"Angad_Australian_Institute_of_Technology__La_Trobe_st_Campus",
"Angad_Australian_Institute_of_Technology__Lonsdale_st_Campus",
"AOI_Institute",
"Ashton_College__Footscray_Campus",
"Ashton_College__Hallam_Campus",
"Ashton_College__Hospitality_Campus",
"Ashton_College__Northcote_Campus",
"Australian_Academy_of_Fashion_Design",
"Australian_Careers_Education__Donald_Street_Campus_(Aurora_Building)",
"Australian_Careers_Education__Victoria_Street_Campus",
"Australian_Catholic_Univeristy__Melbourne_Campus",
"Australian_Catholic_University__Ballarat_Campus",
"Australian_Centre_of_Further_Education",
"Australian_College_of_Applied_Psychology__ACAP_-_Melbourne_Campus",
"Australian_College_of_Sport__Basketball__Melbourne_Campus",
"Australian_College_of_Theology",
"Australian_College_of_Trade__Thornbury_Campus",
"Australian_Education_Academy__10_Blissington_Street__Springvale",
"Australian_Institute_of_Technical_Training__(AITT)__Melbourne_Campus",
"Australian_Institute_of_Trades__Institute_of_Hotel_Management_Australia",
"Australian_Institute_of_Translation___Interpretation_(AITI)__Melbourne_Campus",
"Australian_IT___Hospitality_Institute__Footscray_Campus",
"Australian_National_Airline_College",
"Australian_National_College__Franklin_Street_Campus",
"Australian_National_Institute_of_Business___Technology_(ANIBT)__Melbourne_Campus",
"Australian_Pacific_College__Melbourne_Campus",
"Australian_Study_Link_Institute",
"AVETA_-_Australian_Vocational_Education___Training_Academy",
"Barkly_International_College__City_Campus",
"Barkly_International_College__North_Melbourne_Campus___Automotive_Workshop",
"Barkly_International_College",
"Baxter_Institute__Automotive___Bakery_Campus",
"Baxter_Institute__Fabrication_campus",
"Baxter_Institute__Hairdressing_and_Beauty_Campus_(Flinders_Street)",
"Beaconhills_College",
"Bendigo_TAFE__Bendigo",
"Bendigo_TAFE_and_Kangan_Institute__Broadmeadows_Campus",
"Biba_Academy__Swantson_street_Campus",
"Box_Hill_Institute__City_Campus",
"Box_Hill_Institute",
"Brighton_Institute_of_Technology",
"Catholic_Theological_College_(CTC)__Melbourne_College_of_Divinity_-_East_Melbourne_Campus",
"Central_Australian_College_(CAC)__Melbourne_Campus",
"Central_Melbourne_Institute_(CMI)__City_Campus",
"Central_Melbourne_Institute",
"Charles_Sturt_University_Study_Centres__Melbourne",
"Chisholm_Institue__Chisholm_At_331",
"Chisholm_Institute__Bass_Coast",
"Chisholm_Institute__Cranbourne_Campus",
"Chisholm_Institute__Dandenong_Campus",
"Chisholm_Institute__Flinders_Lane_Campus",
"Chisholm_Institute__Melbourne_City_Campus",
"Collarts_-_Australian_College_of_the_Arts",
"Dalton_College",
"Dance_Factory",
"Deakin_College_(MIBT)__Burwood_Campus",
"Deakin_University__Burwood_Campus",
"Deakin_University__Geelong_Waterfront_Campus",
"Deakin_University__Warrnambool_Campus",
"Deakin_University__Waurn_Ponds_Campus",
"Della_International_College__City_Campus",
"Della_International_College__Sunshine_Campus",
"Department_of_Education_and_Training__Victoria",
"East_West_College_Of_Natural_Therapies",
"Education_Access_Australia",
"Education_Training___Employment_Australia__ETEA",
"Elite_Training_Institute",
"Elly_Lukas_Beauty_Therapy_College",
"ELSIS__Melbourne_Campus",
"Endeavour_College_of_Natural_Health__Melbourne_Campus",
"Everest_Institute_of_Education",
"Explore_English",
"Federation_University__Ballarat_Campus",
"Flinders_International_College",
"Fusion_Enlgish__Melbourne_Campus",
"Global_Business_College_Of_Australia",
"Gordon_Institute_of_TAFE__East_Geelong_Campus",
"Gordon_Institute_of_TAFE__East_Geelong_ELICOS_Campus",
"Greenwich_English_College__Melbourne",
"Harvest_Bible_College",
"Hays_International_College",
"Heading_Out_Academy",
"Headmasters_Advanced_Academy_of_Training",
"Holmesglen__Holmesglen_Institute__Chadstone_Campus",
"Holmesglen__Holmesglen_Institute__City_Campus",
"Holmesglen__Holmesglen_Institute__Waverley_Campus",
"Holmesglen_Institute__Holmesglen_Moorabbin_Campus",
"Hospitality_Management_Institute_of_Australia",
"Impact_English_College__Melbourne_Campus",
"Imperial_College_of_Technology_and_Management",
"Institute_of_Health_and_Nursing_Australia",
"Institute_of_Tertiary_and_Higher_Education_Australia_(ITHEA)",
"INUS_Australia_Education_and_Training",
"JMC_Academy",
"Job_Training_Institute__Dandenong_Campus",
"Kangan_Batman_Institute_of_TAFE__Docklands",
"Kangan_Batman_Institute_of_TAFE__Richmond",
"Kangan_Institute__Moonee_Ponds_Campus",
"Kaplan_Business_School",
"La_Trobe_Bundoora_Campus",
"La_Trobe_University__Albury-Wodonga_Campus",
"La_Trobe_University__Bendigo_Campus",
"La_Trobe_University__City_Campus_(Collins_Street)__City_Campus_(Collins_Street)",
"La_Trobe_University__Melbourne_(Bundoora)_Campus",
"La_Trobe_University__Mildura_Campus",
"La_Trobe_University__Shepparton_Campus",
"Latrobe_College_of_Art_and_Design",
"Lawson_College_Australia",
"Lonsdale_Institute__Eurocentres_Melbourne",
"Marcus_Oldham_College",
"MEGT_Institute__Melbourne_Campus",
"Melbourne_College_of_Hair_and_Beauty",
"Melbourne_Flight_Training",
"Melbourne_Institute_of_Technology_(Federation_University)__Melbourne_Campus",
"Melbourne_Polytechnic__Brunswick_Campus",
"Melbourne_Polytechnic__Epping_Campus",
"Melbourne_Polytechnic__Fairfield_Campus",
"Melbourne_Polytechnic__Heidelberg_Campus",
"Melbourne_Polytechnic__Preston_Campus",
"Melbourne_Polytechnic__Preston_TAFE_Campus",
"Melbourne_Rudolf_Steiner_Seminar",
"Melbourne_School_of_Theology",
"Melbourne_University__Hawthorn_English_Language_Centre",
"Melbourne_University__Trinity_College",
"Menzies_Institute_of_Technology__Adderley_Campus",
"Menzies_Institute_of_Technology__Batman_Campus",
"Menzies_Institute_of_Technology__Spencer_Campus",
"Monash_College__Monash_University_English_Language_Centre",
"Monash_International__Berwick_Campus",
"Monash_International__Peninsula_Campus",
"Monash_University__Caulfield_Campus",
"Monash_University__City_Campus",
"Monash_University__Clayton_Campus",
"Monash_University__Gippsland_Campus",
"Monash_University__Parkville_Campus_(Manning_Building)",
"Monash_University_English_Language_Centre__Monash_College__City_Campus",
"Moorabbin_Flying_Services",
"National_Theatre_(Drama___Ballet_School)",
"Navitas_College_of_Public_Safety_(NCPS)",
"North_Melbourne_College",
"Nova_Institute_of_Technology",
"Oceania_Polytechnic_Institute_of_Education_(OPIE)",
"Orange_International_College",
"Ozford_College_of_Busines",
"Ozford_College_of_Business",
"Ozford_College",
"Pax_Institute_of_Education",
"Pearson_Aviation__Essendon_Airport",
"Photography_Studies_College_(PSC)__Melbourne_Campus",
"Pilgrim_Theological_College",
"Planetshakers_College",
"Presbyterian_Theological_College__Box_Hill_Campus",
"Rabbinical_College_of_Australia_and_N_Z_",
"RC_(Rhodes_College)",
"Reformed_Theological_College__Geelong_Campus",
"Ridley_College__Parkville_Campus",
"RMIT_English_Worldwide",
"RMIT_Univeristy__Brunswick_Campus",
"RMIT_University_(RMIT)__City_Campus",
"RMIT_University__Bundoora_Campus",
"RMIT_University__Point_Cook_Campus",
"Royal_Gurkhas_Institute_of_Technology_(RGIT)_Australia__Gurkhas_Institute_of_Hospitality___Management",
"Royal_Gurkhas_Institute_of_Technology_Australia_(RGIT)",
"Royal_Victorian_Aero_Club",
"SAE_Institute_Qantm_College__Melbourne_Campus",
"School_for_F_M__Alexander_Studies",
"South_Australian_College_of_English_(SACE)_Melbourne_College_of_English",
"South_Pacific_Institute_(SPI)__Melbourne_Campus",
"Southern_Cross_Education_Institute_(SCEI)__Second_Campus",
"Southern_Cross_Education_Institute_(SCEI)__Third_Campus",
"Southern_School_of_Natural_Therapies",
"St__Peters_Institute",
"ST_AEROSPACE_ACADEMY_(AUSTRALIA)_PTY_LTD_2_Bowral_Court__Mitchell_Park",
"St_Peter_Institute__Bourke_Street_Campus",
"St_Peter_Institute__Little_Collins_Campus",
"Stott's_Colleges_(Front_Cooking_School_-_Carlton_Campus)_-_VET",
"Stott's_Colleges__Box_Hill_Campus",
"Stott's_Colleges__Melbourne_Campus",
"Strathfield_College__Melbourne_Campus",
"Sunraysia_Institute_of_TAFE__Mildura_Campus",
"Sunshine_College_of_Management",
"Swinburne_University_of_Technology__Hawthorn_Campus",
"Swinburne_University_of_Technology__Prahan_Campus",
"Technical_Education_Development_Institute",
"Technical_Institute_of_Victoria",
"The_Academy_of_Interactive_Entertainment__Melbourne_Campus",
"The_Academy_of_Interactive_Entertainment",
"The_Australian_Ballet_School",
"The_Australian_Conservatoire_of_Ballet__Melbourne_Campus",
"The_University_of_Melbourne",
"TMG_College",
"Torrens_University__Fitzroy_Campus",
"Torrens_University__Flinders_st_Campus",
"Trinity_College_Theological_School",
"Turner_English__Box_Hill_Campus",
"Turner_English__Camberwell_Campus",
"Turner_English__Dandenong_Campus",
"Turner_English__Melbourne_CBD_Campus",
"Univeristy_of_Divinity__Whitley_College",
"Universal_Institute_of_Technology",
"University_of_Canberra__UC_Melbourne_-_Chadstone_Campus",
"University_of_Divinity__Stirling_College",
"University_of_Divinity__Yarra_Theological_Union",
"Victoria_University__City_Flinders",
"Victoria_University__City_Queen",
"Victoria_University__Footscray_Nicholson",
"Victoria_University__Footscray_Park",
"Victoria_University__Melbourne_Campus",
"Victoria_University__St_Albans",
"Victoria_University__Sunshine",
"Victoria_University__Werribee",
"Victorian_Academy_Of_Commerce_and_Technology_Startups_(VACTS)",
"Victorian_Institute_of_Culinary_Arts___Technology__Main_Campus_-_Spotswood",
"Victorian_Institute_of_Culinary_Arts___Technology__Regional_Campus_1_-_Kerang_Scoresby_st",
"Victorian_Institute_of_Culinary_Arts___Technology__Regional_Campus_2_-_Kerang_Wellington_st",
"Victorian_Institute_of_Culinary_Arts___Technology__Regional_Campus_3_-_Shepparton",
"VIT_(Victorian_Institute_of_Technology)__Abbotsford_Campus",
"VIT_(Victorian_Institute_of_Technology)__Melbourne_CBD_Campus",
"Whitehouse_Institute_of_Design__Australia",
"William_Angliss_Institute",
"Yorke_Institute"]


def row_to_obj(data):
    # print data
    # random.randint(1,101),
    coords = data[1][2:-1].split(", ")
    return {
        "name": data[0],
        "shim": re.sub('[^0-9a-zA-Z]+', '-', data[0].lower()),
        "coords": {
            "lat": float(coords[0]),
            "lng": float(coords[1])
        }
    }


#This generates the filenames

# i=481
# for line in unis:
#     print('"' + re.sub('[^0-9a-zA-Z]+', '-', line.lower()) + "\": data[" + str(i) + "],")
#     i+=1
# print initial
# for row in readr:
#   print ', '.join(row)


#This generates json file

i=481
for line in unis:
    print('"' + re.sub('[^0-9a-zA-Z]+', '-', line.lower()) + "\": data[" + str(i) + "],")
    i+=1