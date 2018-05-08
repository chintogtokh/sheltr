import csv
import json
import random
import re
import os
def row_to_obj(data):
    # print data
    # random.randint(1,101),
    #os.chdir("C:/Users/James2/Documents/UNI/IT/Year 2/Sem 2/IE/Iteration_2_ETL/Iteration_1_fix/binding_v2/helpers_v2")
    with open('./data/geojson/' + data[0] + "_xaaaa.geojson", 'r') as json_file:
        json_data = json.loads(json_file.read())
        return {
            "name": data[0].title(),
            "shim": re.sub('[^0-9a-zA-Z]+', '-', data[0].lower()),
            "rating_safety": int(data[9]),
            "rating_affordability": int(data[17]),
            "geojson": json_data,
            "coords": {
                "lat": float(data[3]),
                "lng": float(data[2])
            },
            "stats": {


{
    "number":float(data[4]),
    "year": "2016",
    "desc":"suburb-residents"
},

{
    "number":float(data[6]),
    "year": "2016",
    "desc":"total-crimes-by-year-and-area"
},

{
    "number":float(data[7]),
    "year": "2016",
    "desc":"offences-per-10000-population"
},

{
    "number":float(data[8]),
    "year": "2016",
    "desc":"suburb-town-name-2016-adjusted-crime-rank"
},

{
    "number":float(data[10]),
    "year": "2016",
    "desc":"offence-count"
},

{
    "number":float(data[11]),
    "year": "2016",
    "desc":"suburb-town-name-2016-real-crime-rank"
},

{
    "number":str(data[12]),
    "year": "2016",
    "desc":"suburb-most-common-expense-tier"
},

{
    "number":float(data[13]),
    "year": "2016",
    "desc":"number-of-rental-properties"
},

{
    "number":float(data[14]),
    "year": "2016",
    "desc":"price-range-rank"
},

{
    "number":float(data[15]),
    "year": "2016",
    "desc":"rental-price-range-lower"
},

{
    "number":float(data[16]),
    "year": "2016",
    "desc":"rental-price-range-upper"
},

{
    "number":str(data[20]),
    "year": "2016",
    "desc":"suburb-most-int-student-lang"
},

{
    "number":float(data[21]),
    "year": "2016",
    "desc":"total-int-students-per-suburb"
},

{
    "number":float(data[22]),
    "year": "2016",
    "desc":"total-int-student-per-language"
},

{
    "number":float(data[23]),
    "year": "2016",
    "desc":"student-population-rating"
},

{
    "number":float(data[24]),
    "year": "2016",
    "desc":"suburb-largest-lang-int-student-pop"
},

{
    "number":str(data[25]),
    "year": "2016",
    "desc":"suburb-largest-int-student-lang"
},

{
    "number":float(data[26]),
    "year": "2016",
    "desc":"percent-of-int-students-language-in-suburb"
},

{
    "number":float(data[27]),
    "year": "2016",
    "desc":"int-student-language-rank-all-langs"
},

{
    "number":float(data[157]),
    "year": "2016",
    "desc":"average-public-transport-users-per-suburb"
},

{
    "number":float(data[158]),
    "year": "2016",
    "desc":"total-public-transport-users-per-suburb"
},

{
    "number":float(data[159]),
    "year": "2016",
    "desc":"total-other-usage-by-suburb"
},

{
    "number":float(data[160]),
    "year": "2016",
    "desc":"adjusted-total-other-usage-scale-rank"
},

{
    "number":float(data[161]),
    "year": "2016",
    "desc":"adjusted-total-transport-use-per-suburb"
},

{
    "number":float(data[162]),
    "year": "2016",
    "desc":"adjusted-total-transport-use-per-suburb-rank"
},

{
    "number":float(data[163]),
    "year": "2016",
    "desc":"adjusted-total-transport-use-per-suburb-scale-rank"
},

{
    "number":str(data[164]),
    "year": "2016",
    "desc":"most-common-transport-method"
},

{
    "number":str(data[165]),
    "year": "2016",
    "desc":"most-common-distance-per-suburb"
},

{
    "number":float(data[170]),
    "year": "2016",
    "desc":"university-campus-long.x"
},

{
    "number":float(data[629]),
    "year": "2016",
    "desc":"whitehouse-institute-of-design--australia-rank"
},

{
    "number":float(data[630]),
    "year": "2016",
    "desc":"william-angliss-institute-rank"
},

{
    "number":float(data[631]),
    "year": "2016",
    "desc":"yorke-institute-rank"
},

{
    "number":float(data[632]),
    "year": "2016",
    "desc":"number-of-medical-workers"
},

{
    "number":float(data[633]),
    "year": "2016",
    "desc":"total-med-staff-per-suburb"
},

{
    "number":float(data[634]),
    "year": "2016",
    "desc":"suburb-med-staff-presence-by-type-rank"
},

{
    "number":float(data[635]),
    "year": "2016",
    "desc":"pop-per-doc"
},

{
    "number":float(data[636]),
    "year": "2016",
    "desc":"pop-per-doc-type"
},

{
    "number":float(data[637]),
    "year": "2016",
    "desc":"total-vic-med-staff"
},

{
    "number":float(data[638]),
    "year": "2016",
    "desc":"real-suburb-med-staff-presence-rank"
},

{
    "number":float(data[639]),
    "year": "2016",
    "desc":"suburb-adjusted-med-staff-presence-rank"
},

{
    "number":float(data[640]),
    "year": "2016",
    "desc":"suburb-adjusted-med-staff-by-type-presence-rank"
},

{
    "number":float(data[641]),
    "year": "2016",
    "desc":"population-adjusted-med-staff-rating"
},

{
    "number":float(data[662]),
    "year": "2016",
    "desc":"aged-care-residential-services"
},

{
    "number":float(data[663]),
    "year": "2016",
    "desc":"allied-health-services"
},

{
    "number":float(data[664]),
    "year": "2016",
    "desc":"ambulance-services"
},

{
    "number":float(data[665]),
    "year": "2016",
    "desc":"chiropractic-and-osteopathic-services"
},

{
    "number":float(data[666]),
    "year": "2016",
    "desc":"dental-services"
},

{
    "number":float(data[667]),
    "year": "2016",
    "desc":"general-practice-medical-services"
},

{
    "number":float(data[668]),
    "year": "2016",
    "desc":"hospitals"
},

{
    "number":float(data[669]),
    "year": "2016",
    "desc":"hospitals-except-psychiatric-hospitals"
},

{
    "number":float(data[670]),
    "year": "2016",
    "desc":"medical-and-other-health-care-services"
},

{
    "number":float(data[671]),
    "year": "2016",
    "desc":"medical-services"
},

{
    "number":float(data[672]),
    "year": "2016",
    "desc":"no-medical-facilities-in-the-area"
},

{
    "number":float(data[673]),
    "year": "2016",
    "desc":"optometry-and-optical-dispensing"
},

{
    "number":float(data[674]),
    "year": "2016",
    "desc":"other-allied-health-services"
},

{
    "number":float(data[675]),
    "year": "2016",
    "desc":"other-residential-care-services"
},

{
    "number":float(data[676]),
    "year": "2016",
    "desc":"pathology-and-diagnostic-imaging-services"
},

{
    "number":float(data[677]),
    "year": "2016",
    "desc":"physiotherapy-services"
},

{
    "number":float(data[678]),
    "year": "2016",
    "desc":"psychiatric-hospitals"
},

{
    "number":float(data[679]),
    "year": "2016",
    "desc":"residential-care-services"
},

{
    "number":float(data[680]),
    "year": "2016",
    "desc":"specialist-medical-services"
},

{
    "number":float(data[681]),
    "year": "2016",
    "desc":"number-of-police-place-of-work"
},

{
    "number":float(data[683]),
    "year": "2016",
    "desc":"pop-per-cop"
},

{
    "number":float(data[684]),
    "year": "2016",
    "desc":"total-vic-pol"
},

{
    "number":float(data[685]),
    "year": "2016",
    "desc":"suburb-police-presence-rank"
},

{
    "number":float(data[686]),
    "year": "2016",
    "desc":"suburb-adjusted-police-presence-rank"
},

{
    "number":float(data[687]),
    "year": "2016",
    "desc":"population-adjusted-police-rating"
},

{
    "number":float(data[688]),
    "year": "2016",
    "desc":"acholi-population"
},

{
    "number":float(data[689]),
    "year": "2016",
    "desc":"african-languages--nec-population"
},

{
    "number":float(data[690]),
    "year": "2016",
    "desc":"african-languages--nfd-population"
},

{
    "number":float(data[691]),
    "year": "2016",
    "desc":"afrikaans-population"
},

{
    "number":float(data[692]),
    "year": "2016",
    "desc":"akan-population"
},

{
    "number":float(data[693]),
    "year": "2016",
    "desc":"albanian-population"
},

{
    "number":float(data[694]),
    "year": "2016",
    "desc":"amharic-population"
},

{
    "number":float(data[695]),
    "year": "2016",
    "desc":"anuak-population"
},

{
    "number":float(data[696]),
    "year": "2016",
    "desc":"arabic-population"
},

{
    "number":float(data[697]),
    "year": "2016",
    "desc":"armenian-population"
},

{
    "number":float(data[698]),
    "year": "2016",
    "desc":"assyrian-neo-aramaic-population"
},

{
    "number":float(data[699]),
    "year": "2016",
    "desc":"bengali-population"
},

{
    "number":float(data[700]),
    "year": "2016",
    "desc":"bisaya-population"
},

{
    "number":float(data[701]),
    "year": "2016",
    "desc":"bosnian-population"
},

{
    "number":float(data[702]),
    "year": "2016",
    "desc":"bulgarian-population"
},

{
    "number":float(data[703]),
    "year": "2016",
    "desc":"burmese-and-related-languages--nec-population"
},

{
    "number":float(data[704]),
    "year": "2016",
    "desc":"burmese-and-related-languages--nfd-population"
},

{
    "number":float(data[705]),
    "year": "2016",
    "desc":"burmese-population"
},

{
    "number":float(data[706]),
    "year": "2016",
    "desc":"cantonese-population"
},

{
    "number":float(data[707]),
    "year": "2016",
    "desc":"catalan-population"
},

{
    "number":float(data[708]),
    "year": "2016",
    "desc":"cebuano-population"
},

{
    "number":float(data[709]),
    "year": "2016",
    "desc":"chaldean-neo-aramaic-population"
},

{
    "number":float(data[710]),
    "year": "2016",
    "desc":"chin-haka-population"
},

{
    "number":float(data[711]),
    "year": "2016",
    "desc":"chinese--nfd-population"
},

{
    "number":float(data[712]),
    "year": "2016",
    "desc":"creole--nfd-population"
},

{
    "number":float(data[713]),
    "year": "2016",
    "desc":"croatian-population"
},

{
    "number":float(data[714]),
    "year": "2016",
    "desc":"czech-population"
},

{
    "number":float(data[715]),
    "year": "2016",
    "desc":"danish-population"
},

{
    "number":float(data[716]),
    "year": "2016",
    "desc":"dari-population"
},

{
    "number":float(data[717]),
    "year": "2016",
    "desc":"dhivehi-population"
},

{
    "number":float(data[718]),
    "year": "2016",
    "desc":"dinka-population"
},

{
    "number":float(data[719]),
    "year": "2016",
    "desc":"dravidian--nec-population"
},

{
    "number":float(data[720]),
    "year": "2016",
    "desc":"dutch-population"
},

{
    "number":float(data[721]),
    "year": "2016",
    "desc":"english-population"
},

{
    "number":float(data[722]),
    "year": "2016",
    "desc":"estonian-population"
},

{
    "number":float(data[723]),
    "year": "2016",
    "desc":"fijian-population"
},

{
    "number":float(data[724]),
    "year": "2016",
    "desc":"filipino-population"
},

{
    "number":float(data[725]),
    "year": "2016",
    "desc":"finnish-population"
},

{
    "number":float(data[726]),
    "year": "2016",
    "desc":"french-creole--nfd-population"
},

{
    "number":float(data[727]),
    "year": "2016",
    "desc":"french-population"
},

{
    "number":float(data[728]),
    "year": "2016",
    "desc":"german-population"
},

{
    "number":float(data[729]),
    "year": "2016",
    "desc":"greek-population"
},

{
    "number":float(data[730]),
    "year": "2016",
    "desc":"gujarati-population"
},

{
    "number":float(data[731]),
    "year": "2016",
    "desc":"hakka-population"
},

{
    "number":float(data[732]),
    "year": "2016",
    "desc":"harari-population"
},

{
    "number":float(data[733]),
    "year": "2016",
    "desc":"hausa-population"
},

{
    "number":float(data[734]),
    "year": "2016",
    "desc":"hazaraghi-population"
},

{
    "number":float(data[735]),
    "year": "2016",
    "desc":"hebrew-population"
},

{
    "number":float(data[736]),
    "year": "2016",
    "desc":"hindi-population"
},

{
    "number":float(data[737]),
    "year": "2016",
    "desc":"hungarian-population"
},

{
    "number":float(data[738]),
    "year": "2016",
    "desc":"iban-population"
},

{
    "number":float(data[739]),
    "year": "2016",
    "desc":"igbo-population"
},

{
    "number":float(data[740]),
    "year": "2016",
    "desc":"ilonggo--hiligaynon--population"
},

{
    "number":float(data[741]),
    "year": "2016",
    "desc":"inadequately-described-population"
},

{
    "number":float(data[742]),
    "year": "2016",
    "desc":"indonesian-population"
},

{
    "number":float(data[743]),
    "year": "2016",
    "desc":"iranic--nfd-population"
},

{
    "number":float(data[744]),
    "year": "2016",
    "desc":"italian-population"
},

{
    "number":float(data[745]),
    "year": "2016",
    "desc":"japanese-population"
},

{
    "number":float(data[746]),
    "year": "2016",
    "desc":"kannada-population"
},

{
    "number":float(data[747]),
    "year": "2016",
    "desc":"karen-population"
},

{
    "number":float(data[748]),
    "year": "2016",
    "desc":"khmer-population"
},

{
    "number":float(data[749]),
    "year": "2016",
    "desc":"kinyarwanda--rwanda--population"
},

{
    "number":float(data[750]),
    "year": "2016",
    "desc":"kirundi--rundi--population"
},

{
    "number":float(data[751]),
    "year": "2016",
    "desc":"konkani-population"
},

{
    "number":float(data[752]),
    "year": "2016",
    "desc":"korean-population"
},

{
    "number":float(data[753]),
    "year": "2016",
    "desc":"kurdish-population"
},

{
    "number":float(data[754]),
    "year": "2016",
    "desc":"lao-population"
},

{
    "number":float(data[755]),
    "year": "2016",
    "desc":"lithuanian-population"
},

{
    "number":float(data[756]),
    "year": "2016",
    "desc":"loma--lorma--population"
},

{
    "number":float(data[757]),
    "year": "2016",
    "desc":"luganda-population"
},

{
    "number":float(data[758]),
    "year": "2016",
    "desc":"macedonian-population"
},

{
    "number":float(data[759]),
    "year": "2016",
    "desc":"malay-population"
},

{
    "number":float(data[760]),
    "year": "2016",
    "desc":"malayalam-population"
},

{
    "number":float(data[761]),
    "year": "2016",
    "desc":"maltese-population"
},

{
    "number":float(data[762]),
    "year": "2016",
    "desc":"mandarin-population"
},

{
    "number":float(data[763]),
    "year": "2016",
    "desc":"maori--cook-island--population"
},

{
    "number":float(data[764]),
    "year": "2016",
    "desc":"maori--new-zealand--population"
},

{
    "number":float(data[765]),
    "year": "2016",
    "desc":"marathi-population"
},

{
    "number":float(data[766]),
    "year": "2016",
    "desc":"mauritian-creole-population"
},

{
    "number":float(data[767]),
    "year": "2016",
    "desc":"min-nan-population"
},

{
    "number":float(data[768]),
    "year": "2016",
    "desc":"mongolian-population"
},

{
    "number":float(data[769]),
    "year": "2016",
    "desc":"nepali-population"
},

{
    "number":float(data[770]),
    "year": "2016",
    "desc":"norwegian-population"
},

{
    "number":float(data[771]),
    "year": "2016",
    "desc":"not-stated-population"
},

{
    "number":float(data[772]),
    "year": "2016",
    "desc":"nuer-population"
},

{
    "number":float(data[773]),
    "year": "2016",
    "desc":"nyanja--chichewa--population"
},

{
    "number":float(data[774]),
    "year": "2016",
    "desc":"oriya-population"
},

{
    "number":float(data[775]),
    "year": "2016",
    "desc":"oromo-population"
},

{
    "number":float(data[776]),
    "year": "2016",
    "desc":"other-southern-asian-languages-population"
},

{
    "number":float(data[777]),
    "year": "2016",
    "desc":"pashto-population"
},

{
    "number":float(data[778]),
    "year": "2016",
    "desc":"persian--excluding-dari--population"
},

{
    "number":float(data[779]),
    "year": "2016",
    "desc":"pidgin--nfd-population"
},

{
    "number":float(data[780]),
    "year": "2016",
    "desc":"polish-population"
},

{
    "number":float(data[781]),
    "year": "2016",
    "desc":"portuguese-population"
},

{
    "number":float(data[782]),
    "year": "2016",
    "desc":"punjabi-population"
},

{
    "number":float(data[783]),
    "year": "2016",
    "desc":"rohingya-population"
},

{
    "number":float(data[784]),
    "year": "2016",
    "desc":"romanian-population"
},

{
    "number":float(data[785]),
    "year": "2016",
    "desc":"russian-population"
},

{
    "number":float(data[786]),
    "year": "2016",
    "desc":"samoan-population"
},

{
    "number":float(data[787]),
    "year": "2016",
    "desc":"serbian-population"
},

{
    "number":float(data[788]),
    "year": "2016",
    "desc":"shilluk-population"
},

{
    "number":float(data[789]),
    "year": "2016",
    "desc":"shona-population"
},

{
    "number":float(data[790]),
    "year": "2016",
    "desc":"sindhi-population"
},

{
    "number":float(data[791]),
    "year": "2016",
    "desc":"sinhalese-population"
},

{
    "number":float(data[792]),
    "year": "2016",
    "desc":"slovak-population"
},

{
    "number":float(data[793]),
    "year": "2016",
    "desc":"slovene-population"
},

{
    "number":float(data[794]),
    "year": "2016",
    "desc":"somali-population"
},

{
    "number":float(data[795]),
    "year": "2016",
    "desc":"southern-asian-languages--nfd-population"
},

{
    "number":float(data[796]),
    "year": "2016",
    "desc":"spanish-population"
},

{
    "number":float(data[797]),
    "year": "2016",
    "desc":"swahili-population"
},

{
    "number":float(data[798]),
    "year": "2016",
    "desc":"swedish-population"
},

{
    "number":float(data[799]),
    "year": "2016",
    "desc":"tagalog-population"
},

{
    "number":float(data[800]),
    "year": "2016",
    "desc":"tamil-population"
},

{
    "number":float(data[801]),
    "year": "2016",
    "desc":"telugu-population"
},

{
    "number":float(data[802]),
    "year": "2016",
    "desc":"tetum-population"
},

{
    "number":float(data[803]),
    "year": "2016",
    "desc":"thai-population"
},

{
    "number":float(data[804]),
    "year": "2016",
    "desc":"tibetan-population"
},

{
    "number":float(data[805]),
    "year": "2016",
    "desc":"tigrinya-population"
},

{
    "number":float(data[806]),
    "year": "2016",
    "desc":"tok-pisin--neomelanesian--population"
},

{
    "number":float(data[807]),
    "year": "2016",
    "desc":"tongan-population"
},

{
    "number":float(data[808]),
    "year": "2016",
    "desc":"tswana-population"
},

{
    "number":float(data[809]),
    "year": "2016",
    "desc":"turkish-population"
},

{
    "number":float(data[810]),
    "year": "2016",
    "desc":"tuvaluan-population"
},

{
    "number":float(data[811]),
    "year": "2016",
    "desc":"ukrainian-population"
},

{
    "number":float(data[812]),
    "year": "2016",
    "desc":"urdu-population"
},

{
    "number":float(data[813]),
    "year": "2016",
    "desc":"vietnamese-population"
},

{
    "number":float(data[814]),
    "year": "2016",
    "desc":"wu-population"
},

{
    "number":float(data[815]),
    "year": "2016",
    "desc":"yoruba-population"
},

{
    "number":float(data[816]),
    "year": "2016",
    "desc":"zomi-population"
},

{
    "number":float(data[817]),
    "year": "2016",
    "desc":"suburb-speaks-aboriginal-english"
},

{
    "number":float(data[818]),
    "year": "2016",
    "desc":"suburb-speaks-acholi"
},

{
    "number":float(data[819]),
    "year": "2016",
    "desc":"suburb-speaks-african-languages"
},

{
    "number":float(data[820]),
    "year": "2016",
    "desc":"suburb-speaks-afrikaans"
},

{
    "number":float(data[821]),
    "year": "2016",
    "desc":"suburb-speaks-akan"
},

{
    "number":float(data[822]),
    "year": "2016",
    "desc":"suburb-speaks-albanian"
},

{
    "number":float(data[823]),
    "year": "2016",
    "desc":"suburb-speaks-american-languages"
},

{
    "number":float(data[824]),
    "year": "2016",
    "desc":"suburb-speaks-amharic"
},

{
    "number":float(data[825]),
    "year": "2016",
    "desc":"suburb-speaks-anuak"
},

{
    "number":float(data[826]),
    "year": "2016",
    "desc":"suburb-speaks-arabic"
},

{
    "number":float(data[827]),
    "year": "2016",
    "desc":"suburb-speaks-armenian"
},

{
    "number":float(data[828]),
    "year": "2016",
    "desc":"suburb-speaks-aromunian-(macedo-romanian)"
},

{
    "number":float(data[829]),
    "year": "2016",
    "desc":"suburb-speaks-assamese"
},

{
    "number":float(data[830]),
    "year": "2016",
    "desc":"suburb-speaks-assyrian-neo-aramaic"
},

{
    "number":float(data[831]),
    "year": "2016",
    "desc":"suburb-speaks-auslan"
},

{
    "number":float(data[832]),
    "year": "2016",
    "desc":"suburb-speaks-australian-indigenous-languages"
},

{
    "number":float(data[833]),
    "year": "2016",
    "desc":"suburb-speaks-azeri"
},

{
    "number":float(data[834]),
    "year": "2016",
    "desc":"suburb-speaks-balinese"
},

{
    "number":float(data[835]),
    "year": "2016",
    "desc":"suburb-speaks-balochi"
},

{
    "number":float(data[836]),
    "year": "2016",
    "desc":"suburb-speaks-bari"
},

{
    "number":float(data[837]),
    "year": "2016",
    "desc":"suburb-speaks-basque"
},

{
    "number":float(data[838]),
    "year": "2016",
    "desc":"suburb-speaks-bassa"
},

{
    "number":float(data[839]),
    "year": "2016",
    "desc":"suburb-speaks-belorussian"
},

{
    "number":float(data[840]),
    "year": "2016",
    "desc":"suburb-speaks-bemba"
},

{
    "number":float(data[841]),
    "year": "2016",
    "desc":"suburb-speaks-bengali"
},

{
    "number":float(data[842]),
    "year": "2016",
    "desc":"suburb-speaks-bidjara"
},

{
    "number":float(data[843]),
    "year": "2016",
    "desc":"suburb-speaks-bikol"
},

{
    "number":float(data[844]),
    "year": "2016",
    "desc":"suburb-speaks-bisaya"
},

{
    "number":float(data[845]),
    "year": "2016",
    "desc":"suburb-speaks-bislama"
},

{
    "number":float(data[846]),
    "year": "2016",
    "desc":"suburb-speaks-bosnian"
},

{
    "number":float(data[847]),
    "year": "2016",
    "desc":"suburb-speaks-bulgarian"
},

{
    "number":float(data[848]),
    "year": "2016",
    "desc":"suburb-speaks-burmese"
},

{
    "number":float(data[849]),
    "year": "2016",
    "desc":"suburb-speaks-burmese-and-related-languages"
},

{
    "number":float(data[850]),
    "year": "2016",
    "desc":"suburb-speaks-cantonese"
},

{
    "number":float(data[851]),
    "year": "2016",
    "desc":"suburb-speaks-catalan"
},

{
    "number":float(data[852]),
    "year": "2016",
    "desc":"suburb-speaks-cebuano"
},

{
    "number":float(data[853]),
    "year": "2016",
    "desc":"suburb-speaks-celtic"
},

{
    "number":float(data[854]),
    "year": "2016",
    "desc":"suburb-speaks-chaldean-neo-aramaic"
},

{
    "number":float(data[855]),
    "year": "2016",
    "desc":"suburb-speaks-chin-haka"
},

{
    "number":float(data[856]),
    "year": "2016",
    "desc":"suburb-speaks-chinese"
},

{
    "number":float(data[857]),
    "year": "2016",
    "desc":"suburb-speaks-creole"
},

{
    "number":float(data[858]),
    "year": "2016",
    "desc":"suburb-speaks-croatian"
},

{
    "number":float(data[859]),
    "year": "2016",
    "desc":"suburb-speaks-cypriot"
},

{
    "number":float(data[860]),
    "year": "2016",
    "desc":"suburb-speaks-czech"
},

{
    "number":float(data[861]),
    "year": "2016",
    "desc":"suburb-speaks-czechoslovakian"
},

{
    "number":float(data[862]),
    "year": "2016",
    "desc":"suburb-speaks-dan-(gio-dan)"
},

{
    "number":float(data[863]),
    "year": "2016",
    "desc":"suburb-speaks-danish"
},

{
    "number":float(data[864]),
    "year": "2016",
    "desc":"suburb-speaks-dari"
},

{
    "number":float(data[865]),
    "year": "2016",
    "desc":"suburb-speaks-dhivehi"
},

{
    "number":float(data[866]),
    "year": "2016",
    "desc":"suburb-speaks-dinka"
},

{
    "number":float(data[867]),
    "year": "2016",
    "desc":"suburb-speaks-djambarrpuyngu"
},

{
    "number":float(data[868]),
    "year": "2016",
    "desc":"suburb-speaks-dravidian"
},

{
    "number":float(data[869]),
    "year": "2016",
    "desc":"suburb-speaks-dutch"
},

{
    "number":float(data[870]),
    "year": "2016",
    "desc":"suburb-speaks-eastern-european-languages"
},

{
    "number":float(data[871]),
    "year": "2016",
    "desc":"suburb-speaks-english"
},

{
    "number":float(data[872]),
    "year": "2016",
    "desc":"suburb-speaks-estonian"
},

{
    "number":float(data[873]),
    "year": "2016",
    "desc":"suburb-speaks-ewe"
},

{
    "number":float(data[874]),
    "year": "2016",
    "desc":"suburb-speaks-fijian"
},

{
    "number":float(data[875]),
    "year": "2016",
    "desc":"suburb-speaks-fijian-hindustani"
},

{
    "number":float(data[876]),
    "year": "2016",
    "desc":"suburb-speaks-filipino"
},

{
    "number":float(data[877]),
    "year": "2016",
    "desc":"suburb-speaks-finnish"
},

{
    "number":float(data[878]),
    "year": "2016",
    "desc":"suburb-speaks-french"
},

{
    "number":float(data[879]),
    "year": "2016",
    "desc":"suburb-speaks-french-creole"
},

{
    "number":float(data[880]),
    "year": "2016",
    "desc":"suburb-speaks-frisian"
},

{
    "number":float(data[881]),
    "year": "2016",
    "desc":"suburb-speaks-fulfulde"
},

{
    "number":float(data[882]),
    "year": "2016",
    "desc":"suburb-speaks-ga"
},

{
    "number":float(data[883]),
    "year": "2016",
    "desc":"suburb-speaks-gaelic-(scotland)"
},

{
    "number":float(data[884]),
    "year": "2016",
    "desc":"suburb-speaks-georgian"
},

{
    "number":float(data[885]),
    "year": "2016",
    "desc":"suburb-speaks-german"
},

{
    "number":float(data[886]),
    "year": "2016",
    "desc":"suburb-speaks-gilbertese"
},

{
    "number":float(data[887]),
    "year": "2016",
    "desc":"suburb-speaks-greek"
},

{
    "number":float(data[888]),
    "year": "2016",
    "desc":"suburb-speaks-gujarati"
},

{
    "number":float(data[889]),
    "year": "2016",
    "desc":"suburb-speaks-guugu-yimidhirr"
},

{
    "number":float(data[890]),
    "year": "2016",
    "desc":"suburb-speaks-hakka"
},

{
    "number":float(data[891]),
    "year": "2016",
    "desc":"suburb-speaks-harari"
},

{
    "number":float(data[892]),
    "year": "2016",
    "desc":"suburb-speaks-hausa"
},

{
    "number":float(data[893]),
    "year": "2016",
    "desc":"suburb-speaks-hazaraghi"
},

{
    "number":float(data[894]),
    "year": "2016",
    "desc":"suburb-speaks-hebrew"
},

{
    "number":float(data[895]),
    "year": "2016",
    "desc":"suburb-speaks-hindi"
},

{
    "number":float(data[896]),
    "year": "2016",
    "desc":"suburb-speaks-hmong"
},

{
    "number":float(data[897]),
    "year": "2016",
    "desc":"suburb-speaks-hungarian"
},

{
    "number":float(data[898]),
    "year": "2016",
    "desc":"suburb-speaks-iban"
},

{
    "number":float(data[899]),
    "year": "2016",
    "desc":"suburb-speaks-iberian-romance"
},

{
    "number":float(data[900]),
    "year": "2016",
    "desc":"suburb-speaks-icelandic"
},

{
    "number":float(data[901]),
    "year": "2016",
    "desc":"suburb-speaks-igbo"
},

{
    "number":float(data[902]),
    "year": "2016",
    "desc":"suburb-speaks-iiokano"
},

{
    "number":float(data[903]),
    "year": "2016",
    "desc":"suburb-speaks-ilonggo-(hiligaynon)"
},

{
    "number":float(data[904]),
    "year": "2016",
    "desc":"suburb-speaks-inadequately-described"
},

{
    "number":float(data[905]),
    "year": "2016",
    "desc":"suburb-speaks-indo-aryan"
},

{
    "number":float(data[906]),
    "year": "2016",
    "desc":"suburb-speaks-indonesian"
},

{
    "number":float(data[907]),
    "year": "2016",
    "desc":"suburb-speaks-invented-languages"
},

{
    "number":float(data[908]),
    "year": "2016",
    "desc":"suburb-speaks-iranic"
},

{
    "number":float(data[909]),
    "year": "2016",
    "desc":"suburb-speaks-irish"
},

{
    "number":float(data[910]),
    "year": "2016",
    "desc":"suburb-speaks-italian"
},

{
    "number":float(data[911]),
    "year": "2016",
    "desc":"suburb-speaks-japanese"
},

{
    "number":float(data[912]),
    "year": "2016",
    "desc":"suburb-speaks-javanese"
},

{
    "number":float(data[913]),
    "year": "2016",
    "desc":"suburb-speaks-kanai"
},

{
    "number":float(data[914]),
    "year": "2016",
    "desc":"suburb-speaks-kannada"
},

{
    "number":float(data[915]),
    "year": "2016",
    "desc":"suburb-speaks-karen"
},

{
    "number":float(data[916]),
    "year": "2016",
    "desc":"suburb-speaks-kashmiri"
},

{
    "number":float(data[917]),
    "year": "2016",
    "desc":"suburb-speaks-key-word-sign-australia"
},

{
    "number":float(data[918]),
    "year": "2016",
    "desc":"suburb-speaks-khmer"
},

{
    "number":float(data[919]),
    "year": "2016",
    "desc":"suburb-speaks-kikuyu"
},

{
    "number":float(data[920]),
    "year": "2016",
    "desc":"suburb-speaks-kinyarwanda-(rwanda)"
},

{
    "number":float(data[921]),
    "year": "2016",
    "desc":"suburb-speaks-kirundi-(rundi)"
},

{
    "number":float(data[922]),
    "year": "2016",
    "desc":"suburb-speaks-konkani"
},

{
    "number":float(data[923]),
    "year": "2016",
    "desc":"suburb-speaks-korean"
},

{
    "number":float(data[924]),
    "year": "2016",
    "desc":"suburb-speaks-krahn"
},

{
    "number":float(data[925]),
    "year": "2016",
    "desc":"suburb-speaks-krio"
},

{
    "number":float(data[926]),
    "year": "2016",
    "desc":"suburb-speaks-kriol"
},

{
    "number":float(data[927]),
    "year": "2016",
    "desc":"suburb-speaks-kune"
},

{
    "number":float(data[928]),
    "year": "2016",
    "desc":"suburb-speaks-kurdish"
},

{
    "number":float(data[929]),
    "year": "2016",
    "desc":"suburb-speaks-lao"
},

{
    "number":float(data[930]),
    "year": "2016",
    "desc":"suburb-speaks-latin"
},

{
    "number":float(data[931]),
    "year": "2016",
    "desc":"suburb-speaks-latvian"
},

{
    "number":float(data[932]),
    "year": "2016",
    "desc":"suburb-speaks-letzeburgish"
},

{
    "number":float(data[933]),
    "year": "2016",
    "desc":"suburb-speaks-liberian-(liberian-english)"
},

{
    "number":float(data[934]),
    "year": "2016",
    "desc":"suburb-speaks-lingala"
},

{
    "number":float(data[935]),
    "year": "2016",
    "desc":"suburb-speaks-lithuanian"
},

{
    "number":float(data[936]),
    "year": "2016",
    "desc":"suburb-speaks-loma-(lorma)"
},

{
    "number":float(data[937]),
    "year": "2016",
    "desc":"suburb-speaks-luganda"
},

{
    "number":float(data[938]),
    "year": "2016",
    "desc":"suburb-speaks-luo"
},

{
    "number":float(data[939]),
    "year": "2016",
    "desc":"suburb-speaks-macedonian"
},

{
    "number":float(data[940]),
    "year": "2016",
    "desc":"suburb-speaks-madi"
},

{
    "number":float(data[941]),
    "year": "2016",
    "desc":"suburb-speaks-malay"
},

{
    "number":float(data[942]),
    "year": "2016",
    "desc":"suburb-speaks-malayalam"
},

{
    "number":float(data[943]),
    "year": "2016",
    "desc":"suburb-speaks-maltese"
},

{
    "number":float(data[944]),
    "year": "2016",
    "desc":"suburb-speaks-mandaean-(mandaic)"
},

{
    "number":float(data[945]),
    "year": "2016",
    "desc":"suburb-speaks-mandarin"
},

{
    "number":float(data[946]),
    "year": "2016",
    "desc":"suburb-speaks-mandinka"
},

{
    "number":float(data[947]),
    "year": "2016",
    "desc":"suburb-speaks-mann"
},

{
    "number":float(data[948]),
    "year": "2016",
    "desc":"suburb-speaks-manyjilyjarra"
},

{
    "number":float(data[949]),
    "year": "2016",
    "desc":"suburb-speaks-maori-(cook-island)"
},

{
    "number":float(data[950]),
    "year": "2016",
    "desc":"suburb-speaks-maori-(new-zealand)"
},

{
    "number":float(data[951]),
    "year": "2016",
    "desc":"suburb-speaks-marathi"
},

{
    "number":float(data[952]),
    "year": "2016",
    "desc":"suburb-speaks-mauritian-creole"
},

{
    "number":float(data[953]),
    "year": "2016",
    "desc":"suburb-speaks-middle-eastern-semitic-languages"
},

{
    "number":float(data[954]),
    "year": "2016",
    "desc":"suburb-speaks-min-nan"
},

{
    "number":float(data[955]),
    "year": "2016",
    "desc":"suburb-speaks-mon"
},

{
    "number":float(data[956]),
    "year": "2016",
    "desc":"suburb-speaks-mon-khmer"
},

{
    "number":float(data[957]),
    "year": "2016",
    "desc":"suburb-speaks-mongolian"
},

{
    "number":float(data[958]),
    "year": "2016",
    "desc":"suburb-speaks-moro-(nuba-moro)"
},

{
    "number":float(data[959]),
    "year": "2016",
    "desc":"suburb-speaks-motu-(hirimotu)"
},

{
    "number":float(data[960]),
    "year": "2016",
    "desc":"suburb-speaks-murrinh-patha"
},

{
    "number":float(data[961]),
    "year": "2016",
    "desc":"suburb-speaks-nauruan"
},

{
    "number":float(data[962]),
    "year": "2016",
    "desc":"suburb-speaks-ndebele"
},

{
    "number":float(data[963]),
    "year": "2016",
    "desc":"suburb-speaks-nepali"
},

{
    "number":float(data[964]),
    "year": "2016",
    "desc":"suburb-speaks-ngarrindjeri"
},

{
    "number":float(data[965]),
    "year": "2016",
    "desc":"suburb-speaks-niue"
},

{
    "number":float(data[966]),
    "year": "2016",
    "desc":"suburb-speaks-norf'k-pitcairn"
},

{
    "number":float(data[967]),
    "year": "2016",
    "desc":"suburb-speaks-norwegian"
},

{
    "number":float(data[968]),
    "year": "2016",
    "desc":"suburb-speaks-nuer"
},

{
    "number":float(data[969]),
    "year": "2016",
    "desc":"suburb-speaks-nyanja-(chichewa)"
},

{
    "number":float(data[970]),
    "year": "2016",
    "desc":"suburb-speaks-nyungar"
},

{
    "number":float(data[971]),
    "year": "2016",
    "desc":"suburb-speaks-oceanian-pidgins-and-creoles"
},

{
    "number":float(data[972]),
    "year": "2016",
    "desc":"suburb-speaks-oriya"
},

{
    "number":float(data[973]),
    "year": "2016",
    "desc":"suburb-speaks-oromo"
},

{
    "number":float(data[974]),
    "year": "2016",
    "desc":"suburb-speaks-other-eastern-asian-languages"
},

{
    "number":float(data[975]),
    "year": "2016",
    "desc":"suburb-speaks-other-southeast-asian-languages"
},

{
    "number":float(data[976]),
    "year": "2016",
    "desc":"suburb-speaks-other-southern-asian-languages"
},

{
    "number":float(data[977]),
    "year": "2016",
    "desc":"suburb-speaks-other-southern-european-languages"
},

{
    "number":float(data[978]),
    "year": "2016",
    "desc":"suburb-speaks-paakantyi"
},

{
    "number":float(data[979]),
    "year": "2016",
    "desc":"suburb-speaks-pacific-austronesian-languages"
},

{
    "number":float(data[980]),
    "year": "2016",
    "desc":"suburb-speaks-pampangan"
},

{
    "number":float(data[981]),
    "year": "2016",
    "desc":"suburb-speaks-papua-new-guinea-languages"
},

{
    "number":float(data[982]),
    "year": "2016",
    "desc":"suburb-speaks-pashto"
},

{
    "number":float(data[983]),
    "year": "2016",
    "desc":"suburb-speaks-persian-(excluding-dari)"
},

{
    "number":float(data[984]),
    "year": "2016",
    "desc":"suburb-speaks-pidgin"
},

{
    "number":float(data[985]),
    "year": "2016",
    "desc":"suburb-speaks-pitjantjatjara"
},

{
    "number":float(data[986]),
    "year": "2016",
    "desc":"suburb-speaks-polish"
},

{
    "number":float(data[987]),
    "year": "2016",
    "desc":"suburb-speaks-portuguese"
},

{
    "number":float(data[988]),
    "year": "2016",
    "desc":"suburb-speaks-portuguese-creole"
},

{
    "number":float(data[989]),
    "year": "2016",
    "desc":"suburb-speaks-punjabi"
},

{
    "number":float(data[990]),
    "year": "2016",
    "desc":"suburb-speaks-rohingya"
},

{
    "number":float(data[991]),
    "year": "2016",
    "desc":"suburb-speaks-romanian"
},

{
    "number":float(data[992]),
    "year": "2016",
    "desc":"suburb-speaks-romany"
},

{
    "number":float(data[993]),
    "year": "2016",
    "desc":"suburb-speaks-rotuman"
},

{
    "number":float(data[994]),
    "year": "2016",
    "desc":"suburb-speaks-russian"
},

{
    "number":float(data[995]),
    "year": "2016",
    "desc":"suburb-speaks-samoan"
},

{
    "number":float(data[996]),
    "year": "2016",
    "desc":"suburb-speaks-scandinavian"
},

{
    "number":float(data[997]),
    "year": "2016",
    "desc":"suburb-speaks-serbian"
},

{
    "number":float(data[998]),
    "year": "2016",
    "desc":"suburb-speaks-serbo-croatian/yugoslavian"
},

{
    "number":float(data[999]),
    "year": "2016",
    "desc":"suburb-speaks-seychelles-creole"
},

{
    "number":float(data[1000]),
    "year": "2016",
    "desc":"suburb-speaks-shilluk"
},

{
    "number":float(data[1001]),
    "year": "2016",
    "desc":"suburb-speaks-shona"
},

{
    "number":float(data[1002]),
    "year": "2016",
    "desc":"suburb-speaks-sign-languages"
},

{
    "number":float(data[1003]),
    "year": "2016",
    "desc":"suburb-speaks-sindhi"
},

{
    "number":float(data[1004]),
    "year": "2016",
    "desc":"suburb-speaks-sinhalese"
},

{
    "number":float(data[1005]),
    "year": "2016",
    "desc":"suburb-speaks-slovak"
},

{
    "number":float(data[1006]),
    "year": "2016",
    "desc":"suburb-speaks-slovene"
},

{
    "number":float(data[1007]),
    "year": "2016",
    "desc":"suburb-speaks-somali"
},

{
    "number":float(data[1008]),
    "year": "2016",
    "desc":"suburb-speaks-southeast-asian-austronesian-languages"
},

{
    "number":float(data[1009]),
    "year": "2016",
    "desc":"suburb-speaks-southern-asian-languages"
},

{
    "number":float(data[1010]),
    "year": "2016",
    "desc":"suburb-speaks-spanish"
},

{
    "number":float(data[1011]),
    "year": "2016",
    "desc":"suburb-speaks-spanish-creole"
},

{
    "number":float(data[1012]),
    "year": "2016",
    "desc":"suburb-speaks-swahili"
},

{
    "number":float(data[1013]),
    "year": "2016",
    "desc":"suburb-speaks-swedish"
},

{
    "number":float(data[1014]),
    "year": "2016",
    "desc":"suburb-speaks-swiss"
},

{
    "number":float(data[1015]),
    "year": "2016",
    "desc":"suburb-speaks-tagalog"
},

{
    "number":float(data[1016]),
    "year": "2016",
    "desc":"suburb-speaks-tai"
},

{
    "number":float(data[1017]),
    "year": "2016",
    "desc":"suburb-speaks-tamil"
},

{
    "number":float(data[1018]),
    "year": "2016",
    "desc":"suburb-speaks-tatar"
},

{
    "number":float(data[1019]),
    "year": "2016",
    "desc":"suburb-speaks-telugu"
},

{
    "number":float(data[1020]),
    "year": "2016",
    "desc":"suburb-speaks-tetum"
},

{
    "number":float(data[1021]),
    "year": "2016",
    "desc":"suburb-speaks-thai"
},

{
    "number":float(data[1022]),
    "year": "2016",
    "desc":"suburb-speaks-tibetan"
},

{
    "number":float(data[1023]),
    "year": "2016",
    "desc":"suburb-speaks-tigre"
},

{
    "number":float(data[1024]),
    "year": "2016",
    "desc":"suburb-speaks-tigrinya"
},

{
    "number":float(data[1025]),
    "year": "2016",
    "desc":"suburb-speaks-timorese"
},

{
    "number":float(data[1026]),
    "year": "2016",
    "desc":"suburb-speaks-tok-pisin-(neomelanesian)"
},

{
    "number":float(data[1027]),
    "year": "2016",
    "desc":"suburb-speaks-tokelauan"
},

{
    "number":float(data[1028]),
    "year": "2016",
    "desc":"suburb-speaks-tongan"
},

{
    "number":float(data[1029]),
    "year": "2016",
    "desc":"suburb-speaks-tswana"
},

{
    "number":float(data[1030]),
    "year": "2016",
    "desc":"suburb-speaks-tulu"
},

{
    "number":float(data[1031]),
    "year": "2016",
    "desc":"suburb-speaks-turkic"
},

{
    "number":float(data[1032]),
    "year": "2016",
    "desc":"suburb-speaks-turkish"
},

{
    "number":float(data[1033]),
    "year": "2016",
    "desc":"suburb-speaks-turkmen"
},

{
    "number":float(data[1034]),
    "year": "2016",
    "desc":"suburb-speaks-tuvaluan"
},

{
    "number":float(data[1035]),
    "year": "2016",
    "desc":"suburb-speaks-ukrainian"
},

{
    "number":float(data[1036]),
    "year": "2016",
    "desc":"suburb-speaks-urdu"
},

{
    "number":float(data[1037]),
    "year": "2016",
    "desc":"suburb-speaks-uygur"
},

{
    "number":float(data[1038]),
    "year": "2016",
    "desc":"suburb-speaks-uzbek"
},

{
    "number":float(data[1039]),
    "year": "2016",
    "desc":"suburb-speaks-vietnamese"
},

{
    "number":float(data[1040]),
    "year": "2016",
    "desc":"suburb-speaks-wajarri"
},

{
    "number":float(data[1041]),
    "year": "2016",
    "desc":"suburb-speaks-warlpiri"
},

{
    "number":float(data[1042]),
    "year": "2016",
    "desc":"suburb-speaks-welsh"
},

{
    "number":float(data[1043]),
    "year": "2016",
    "desc":"suburb-speaks-wergaia"
},

{
    "number":float(data[1044]),
    "year": "2016",
    "desc":"suburb-speaks-wiradjuri"
},

{
    "number":float(data[1045]),
    "year": "2016",
    "desc":"suburb-speaks-wu"
},

{
    "number":float(data[1046]),
    "year": "2016",
    "desc":"suburb-speaks-xhosa"
},

{
    "number":float(data[1047]),
    "year": "2016",
    "desc":"suburb-speaks-yankunytjatjara"
},

{
    "number":float(data[1048]),
    "year": "2016",
    "desc":"suburb-speaks-yiddish"
},

{
    "number":float(data[1049]),
    "year": "2016",
    "desc":"suburb-speaks-yidiny"
},

{
    "number":float(data[1050]),
    "year": "2016",
    "desc":"suburb-speaks-yolngu-matha"
},

{
    "number":float(data[1051]),
    "year": "2016",
    "desc":"suburb-speaks-yorta-yorta"
},

{
    "number":float(data[1052]),
    "year": "2016",
    "desc":"suburb-speaks-yoruba"
},

{
    "number":float(data[1053]),
    "year": "2016",
    "desc":"suburb-speaks-yumplatok-(torres-strait-creole)"
},

{
    "number":float(data[1054]),
    "year": "2016",
    "desc":"suburb-speaks-zomi"
},

{
    "number":float(data[1055]),
    "year": "2016",
    "desc":"suburb-speaks-zulu"
},

{
    "number":str(data[1056]),
    "year": "2016",
    "desc":"int-student-rental-price-bracket"
},

{
    "number":float(data[1057]),
    "year": "2016",
    "desc":"number-of-int-students-in-rental-bracket"
},

{
    "number":float(data[1058]),
    "year": "2016",
    "desc":"international-students-renting-in-suburb"
},

{
    "number":float(data[1059]),
    "year": "2016",
    "desc":"avg-rental-expenditure-per-int-student-per-suburb"
},

{
    "number":float(data[1060]),
    "year": "2016",
    "desc":"avg-rental-expenditure-for-int-students-in-victoria"
},

{
    "number":str(data[1061]),
    "year": "2016",
    "desc":"vic-int-student-most-common-expense-tier"
},

{
    "number":float(data[1062]),
    "year": "2016",
    "desc":"vic-total-crime-stats"
},

{
    "number":float(data[1063]),
    "year": "2016",
    "desc":"total-crime-in-suburb-stats"
},

{
    "number":float(data[1064]),
    "year": "2016",
    "desc":"avg-crime-per-suburb-vic-stats"
},



            },
            "university_distances": {


{
    "number":float(data[171]),
    "year": "2016",
    "desc":"aapoly-melbourne-campus-distance"
},

{
    "number":float(data[172]),
    "year": "2016",
    "desc":"academia-international-melbourne-campus-distance"
},

{
    "number":float(data[173]),
    "year": "2016",
    "desc":"acumen-institute-of-further-education-cbd-campus-distance"
},

{
    "number":float(data[174]),
    "year": "2016",
    "desc":"acumen-institute-of-further-education-richmond-campus-distance"
},

{
    "number":float(data[175]),
    "year": "2016",
    "desc":"agb-training-geelong-campus-distance"
},

{
    "number":float(data[176]),
    "year": "2016",
    "desc":"alacc-health-college-australia-distance"
},

{
    "number":float(data[177]),
    "year": "2016",
    "desc":"alfred-deakin-college-(mibt)-waurn-ponds-campus-distance"
},

{
    "number":float(data[178]),
    "year": "2016",
    "desc":"altec-college-melbourne-campus-distance"
},

{
    "number":float(data[179]),
    "year": "2016",
    "desc":"angad-australian-institute-of-technology-la-trobe-st-campus-distance"
},

{
    "number":float(data[180]),
    "year": "2016",
    "desc":"aoi-institute-distance"
},

{
    "number":float(data[181]),
    "year": "2016",
    "desc":"ashton-college-footscray-campus-distance"
},

{
    "number":float(data[182]),
    "year": "2016",
    "desc":"ashton-college-hallam-campus-distance"
},

{
    "number":float(data[183]),
    "year": "2016",
    "desc":"ashton-college-hospitality-campus-distance"
},

{
    "number":float(data[184]),
    "year": "2016",
    "desc":"ashton-college-northcote-campus-distance"
},

{
    "number":float(data[185]),
    "year": "2016",
    "desc":"australian-academy-of-fashion-design-distance"
},

{
    "number":float(data[186]),
    "year": "2016",
    "desc":"australian-careers-education-donald-street-campus-(aurora-building)-distance"
},

{
    "number":float(data[187]),
    "year": "2016",
    "desc":"australian-careers-education-victoria-street-campus-distance"
},

{
    "number":float(data[188]),
    "year": "2016",
    "desc":"australian-catholic-univeristy-melbourne-campus-distance"
},

{
    "number":float(data[189]),
    "year": "2016",
    "desc":"australian-catholic-university-ballarat-campus-distance"
},

{
    "number":float(data[190]),
    "year": "2016",
    "desc":"australian-centre-of-further-education-distance"
},

{
    "number":float(data[191]),
    "year": "2016",
    "desc":"australian-college-of-applied-psychology-acap---melbourne-campus-distance"
},

{
    "number":float(data[192]),
    "year": "2016",
    "desc":"australian-college-of-sport-basketball-melbourne-campus-distance"
},

{
    "number":float(data[193]),
    "year": "2016",
    "desc":"australian-college-of-theology-distance"
},

{
    "number":float(data[194]),
    "year": "2016",
    "desc":"australian-college-of-trade-thornbury-campus-distance"
},

{
    "number":float(data[195]),
    "year": "2016",
    "desc":"australian-education-academy-10-blissington-street-springvale-distance"
},

{
    "number":float(data[196]),
    "year": "2016",
    "desc":"australian-institute-of-technical-training-(aitt)-melbourne-campus-distance"
},

{
    "number":float(data[197]),
    "year": "2016",
    "desc":"australian-institute-of-trades-institute-of-hotel-management-australia-distance"
},

{
    "number":float(data[198]),
    "year": "2016",
    "desc":"australian-institute-of-translation-interpretation-(aiti)-melbourne-campus-distance"
},

{
    "number":float(data[199]),
    "year": "2016",
    "desc":"australian-it-hospitality-institute-footscray-campus-distance"
},

{
    "number":float(data[200]),
    "year": "2016",
    "desc":"australian-national-airline-college-distance"
},

{
    "number":float(data[201]),
    "year": "2016",
    "desc":"australian-national-college-franklin-street-campus-distance"
},

{
    "number":float(data[202]),
    "year": "2016",
    "desc":"australian-national-institute-of-business-technology-(anibt)-melbourne-campus-distance"
},

{
    "number":float(data[203]),
    "year": "2016",
    "desc":"australian-pacific-college-melbourne-campus-distance"
},

{
    "number":float(data[204]),
    "year": "2016",
    "desc":"australian-study-link-institute-distance"
},

{
    "number":float(data[205]),
    "year": "2016",
    "desc":"aveta---australian-vocational-education-training-academy-distance"
},

{
    "number":float(data[206]),
    "year": "2016",
    "desc":"barkly-international-college-city-campus-distance"
},

{
    "number":float(data[207]),
    "year": "2016",
    "desc":"barkly-international-college-north-melbourne-campus-automotive-workshop-distance"
},

{
    "number":float(data[208]),
    "year": "2016",
    "desc":"baxter-institute-automotive-bakery-campus-distance"
},

{
    "number":float(data[209]),
    "year": "2016",
    "desc":"baxter-institute-fabrication-campus-distance"
},

{
    "number":float(data[210]),
    "year": "2016",
    "desc":"baxter-institute-hairdressing-and-beauty-campus-(flinders-street)-distance"
},

{
    "number":float(data[211]),
    "year": "2016",
    "desc":"beaconhills-college-distance"
},

{
    "number":float(data[212]),
    "year": "2016",
    "desc":"bendigo-tafe-bendigo-distance"
},

{
    "number":float(data[213]),
    "year": "2016",
    "desc":"bendigo-tafe-and-kangan-institute-broadmeadows-campus-distance"
},

{
    "number":float(data[214]),
    "year": "2016",
    "desc":"biba-academy-swantson-street-campus-distance"
},

{
    "number":float(data[215]),
    "year": "2016",
    "desc":"box-hill-institute-city-campus-distance"
},

{
    "number":float(data[216]),
    "year": "2016",
    "desc":"box-hill-institute-distance"
},

{
    "number":float(data[217]),
    "year": "2016",
    "desc":"brighton-institute-of-technology-distance"
},

{
    "number":float(data[218]),
    "year": "2016",
    "desc":"catholic-theological-college-(ctc)-melbourne-college-of-divinity---east-melbourne-campus-distance"
},

{
    "number":float(data[219]),
    "year": "2016",
    "desc":"central-australian-college-(cac)-melbourne-campus-distance"
},

{
    "number":float(data[220]),
    "year": "2016",
    "desc":"central-melbourne-institute-(cmi)-city-campus-distance"
},

{
    "number":float(data[221]),
    "year": "2016",
    "desc":"central-melbourne-institute-distance"
},

{
    "number":float(data[222]),
    "year": "2016",
    "desc":"central-queensland-university-city-campus-distance"
},

{
    "number":float(data[223]),
    "year": "2016",
    "desc":"charles-sturt-university-study-centres-melbourne-distance"
},

{
    "number":float(data[224]),
    "year": "2016",
    "desc":"chisholm-institue-chisholm-at-331-distance"
},

{
    "number":float(data[225]),
    "year": "2016",
    "desc":"chisholm-institute-bass-coast-distance"
},

{
    "number":float(data[226]),
    "year": "2016",
    "desc":"chisholm-institute-cranbourne-campus-distance"
},

{
    "number":float(data[227]),
    "year": "2016",
    "desc":"chisholm-institute-dandenong-campus-distance"
},

{
    "number":float(data[228]),
    "year": "2016",
    "desc":"chisholm-institute-flinders-lane-campus-distance"
},

{
    "number":float(data[229]),
    "year": "2016",
    "desc":"chisholm-institute-melbourne-city-campus-distance"
},

{
    "number":float(data[230]),
    "year": "2016",
    "desc":"collarts---australian-college-of-the-arts-distance"
},

{
    "number":float(data[231]),
    "year": "2016",
    "desc":"dalton-college-distance"
},

{
    "number":float(data[232]),
    "year": "2016",
    "desc":"dance-factory-distance"
},

{
    "number":float(data[233]),
    "year": "2016",
    "desc":"deakin-college-(mibt)-burwood-campus-distance"
},

{
    "number":float(data[234]),
    "year": "2016",
    "desc":"deakin-university-geelong-waterfront-campus-distance"
},

{
    "number":float(data[235]),
    "year": "2016",
    "desc":"deakin-university-warrnambool-campus-distance"
},

{
    "number":float(data[236]),
    "year": "2016",
    "desc":"deakin-university-waurn-ponds-campus-distance"
},

{
    "number":float(data[237]),
    "year": "2016",
    "desc":"della-international-college-city-campus-distance"
},

{
    "number":float(data[238]),
    "year": "2016",
    "desc":"della-international-college-sunshine-campus-distance"
},

{
    "number":float(data[239]),
    "year": "2016",
    "desc":"department-of-education-and-training-victoria-distance"
},

{
    "number":float(data[240]),
    "year": "2016",
    "desc":"east-west-college-of-natural-therapies-distance"
},

{
    "number":float(data[241]),
    "year": "2016",
    "desc":"education-access-australia-distance"
},

{
    "number":float(data[242]),
    "year": "2016",
    "desc":"education-training-employment-australia-etea-distance"
},

{
    "number":float(data[243]),
    "year": "2016",
    "desc":"elite-training-institute-distance"
},

{
    "number":float(data[244]),
    "year": "2016",
    "desc":"elly-lukas-beauty-therapy-college-distance"
},

{
    "number":float(data[245]),
    "year": "2016",
    "desc":"elsis-melbourne-campus-distance"
},

{
    "number":float(data[246]),
    "year": "2016",
    "desc":"endeavour-college-of-natural-health-melbourne-campus-distance"
},

{
    "number":float(data[247]),
    "year": "2016",
    "desc":"everest-institute-of-education-distance"
},

{
    "number":float(data[248]),
    "year": "2016",
    "desc":"explore-english-distance"
},

{
    "number":float(data[249]),
    "year": "2016",
    "desc":"federation-university-ballarat-campus-distance"
},

{
    "number":float(data[250]),
    "year": "2016",
    "desc":"federation-university-gippsland-campus-distance"
},

{
    "number":float(data[251]),
    "year": "2016",
    "desc":"federation-university-wimmera-campus-distance"
},

{
    "number":float(data[306]),
    "year": "2016",
    "desc":"federation-university-berwick-campus-distance"
},

{
    "number":float(data[252]),
    "year": "2016",
    "desc":"flinders-international-college-distance"
},

{
    "number":float(data[253]),
    "year": "2016",
    "desc":"fusion-enlgish-melbourne-campus-distance"
},

{
    "number":float(data[254]),
    "year": "2016",
    "desc":"global-business-college-of-australia-distance"
},

{
    "number":float(data[255]),
    "year": "2016",
    "desc":"gordon-institute-of-tafe-east-geelong-campus-distance"
},

{
    "number":float(data[256]),
    "year": "2016",
    "desc":"gordon-institute-of-tafe-east-geelong-elicos-campus-distance"
},

{
    "number":float(data[257]),
    "year": "2016",
    "desc":"greenwich-english-college-melbourne-distance"
},

{
    "number":float(data[258]),
    "year": "2016",
    "desc":"harvest-bible-college-distance"
},

{
    "number":float(data[259]),
    "year": "2016",
    "desc":"hays-international-college-distance"
},

{
    "number":float(data[260]),
    "year": "2016",
    "desc":"heading-out-academy-distance"
},

{
    "number":float(data[261]),
    "year": "2016",
    "desc":"headmasters-advanced-academy-of-training-distance"
},

{
    "number":float(data[262]),
    "year": "2016",
    "desc":"holmesglen-holmesglen-institute-chadstone-campus-distance"
},

{
    "number":float(data[263]),
    "year": "2016",
    "desc":"holmesglen-holmesglen-institute-city-campus-distance"
},

{
    "number":float(data[264]),
    "year": "2016",
    "desc":"holmesglen-holmesglen-institute-waverley-campus-distance"
},

{
    "number":float(data[265]),
    "year": "2016",
    "desc":"holmesglen-institute-holmesglen-moorabbin-campus-distance"
},

{
    "number":float(data[266]),
    "year": "2016",
    "desc":"hospitality-management-institute-of-australia-distance"
},

{
    "number":float(data[267]),
    "year": "2016",
    "desc":"impact-english-college-melbourne-campus-distance"
},

{
    "number":float(data[268]),
    "year": "2016",
    "desc":"imperial-college-of-technology-and-management-distance"
},

{
    "number":float(data[269]),
    "year": "2016",
    "desc":"institute-of-health-and-nursing-australia-distance"
},

{
    "number":float(data[270]),
    "year": "2016",
    "desc":"institute-of-tertiary-and-higher-education-australia-(ithea)-distance"
},

{
    "number":float(data[271]),
    "year": "2016",
    "desc":"inus-australia-education-and-training-distance"
},

{
    "number":float(data[272]),
    "year": "2016",
    "desc":"jmc-academy-distance"
},

{
    "number":float(data[273]),
    "year": "2016",
    "desc":"job-training-institute-dandenong-campus-distance"
},

{
    "number":float(data[274]),
    "year": "2016",
    "desc":"kangan-batman-institute-of-tafe-docklands-distance"
},

{
    "number":float(data[275]),
    "year": "2016",
    "desc":"kangan-batman-institute-of-tafe-richmond-distance"
},

{
    "number":float(data[276]),
    "year": "2016",
    "desc":"kangan-institute-moonee-ponds-campus-distance"
},

{
    "number":float(data[277]),
    "year": "2016",
    "desc":"kaplan-business-school-distance"
},

{
    "number":float(data[278]),
    "year": "2016",
    "desc":"la-trobe-bundoora-campus-distance"
},

{
    "number":float(data[279]),
    "year": "2016",
    "desc":"la-trobe-university-albury-wodonga-campus-distance"
},

{
    "number":float(data[280]),
    "year": "2016",
    "desc":"la-trobe-university-bendigo-campus-distance"
},

{
    "number":float(data[281]),
    "year": "2016",
    "desc":"la-trobe-university-city-campus-(collins-street)-city-campus-(collins-street)-distance"
},

{
    "number":float(data[282]),
    "year": "2016",
    "desc":"la-trobe-university-mildura-campus-distance"
},

{
    "number":float(data[283]),
    "year": "2016",
    "desc":"la-trobe-university-shepparton-campus-distance"
},

{
    "number":float(data[284]),
    "year": "2016",
    "desc":"latrobe-college-of-art-and-design-distance"
},

{
    "number":float(data[285]),
    "year": "2016",
    "desc":"lawson-college-australia-distance"
},

{
    "number":float(data[286]),
    "year": "2016",
    "desc":"lonsdale-institute-eurocentres-melbourne-distance"
},

{
    "number":float(data[287]),
    "year": "2016",
    "desc":"marcus-oldham-college-distance"
},

{
    "number":float(data[288]),
    "year": "2016",
    "desc":"megt-institute-melbourne-campus-distance"
},

{
    "number":float(data[289]),
    "year": "2016",
    "desc":"melbourne-college-of-hair-and-beauty-distance"
},

{
    "number":float(data[290]),
    "year": "2016",
    "desc":"melbourne-flight-training-distance"
},

{
    "number":float(data[291]),
    "year": "2016",
    "desc":"melbourne-institute-of-technology-(federation-university)-melbourne-campus-distance"
},

{
    "number":float(data[292]),
    "year": "2016",
    "desc":"melbourne-polytechnic-brunswick-campus-distance"
},

{
    "number":float(data[293]),
    "year": "2016",
    "desc":"melbourne-polytechnic-epping-campus-distance"
},

{
    "number":float(data[294]),
    "year": "2016",
    "desc":"melbourne-polytechnic-fairfield-campus-distance"
},

{
    "number":float(data[295]),
    "year": "2016",
    "desc":"melbourne-polytechnic-heidelberg-campus-distance"
},

{
    "number":float(data[296]),
    "year": "2016",
    "desc":"melbourne-polytechnic-preston-campus-distance"
},

{
    "number":float(data[297]),
    "year": "2016",
    "desc":"melbourne-polytechnic-preston-tafe-campus-distance"
},

{
    "number":float(data[298]),
    "year": "2016",
    "desc":"melbourne-rudolf-steiner-seminar-distance"
},

{
    "number":float(data[299]),
    "year": "2016",
    "desc":"melbourne-school-of-theology-distance"
},

{
    "number":float(data[300]),
    "year": "2016",
    "desc":"melbourne-university-hawthorn-english-language-centre-distance"
},

{
    "number":float(data[301]),
    "year": "2016",
    "desc":"melbourne-university-trinity-college-distance"
},

{
    "number":float(data[302]),
    "year": "2016",
    "desc":"menzies-institute-of-technology-adderley-campus-distance"
},

{
    "number":float(data[303]),
    "year": "2016",
    "desc":"menzies-institute-of-technology-batman-campus-distance"
},

{
    "number":float(data[304]),
    "year": "2016",
    "desc":"menzies-institute-of-technology-spencer-campus-distance"
},

{
    "number":float(data[305]),
    "year": "2016",
    "desc":"monash-college-monash-university-english-language-centre-distance"
},

{
    "number":float(data[307]),
    "year": "2016",
    "desc":"monash-international-peninsula-campus-distance"
},

{
    "number":float(data[308]),
    "year": "2016",
    "desc":"monash-university-caulfield-campus-distance"
},

{
    "number":float(data[309]),
    "year": "2016",
    "desc":"monash-university-city-campus-distance"
},

{
    "number":float(data[310]),
    "year": "2016",
    "desc":"monash-university-clayton-campus-distance"
},

{
    "number":float(data[311]),
    "year": "2016",
    "desc":"monash-university-parkville-campus-(manning-building)-distance"
},

{
    "number":float(data[312]),
    "year": "2016",
    "desc":"monash-university-english-language-centre-monash-college-city-campus-distance"
},

{
    "number":float(data[313]),
    "year": "2016",
    "desc":"moorabbin-flying-services-distance"
},

{
    "number":float(data[314]),
    "year": "2016",
    "desc":"national-theatre-(drama-ballet-school)-distance"
},

{
    "number":float(data[315]),
    "year": "2016",
    "desc":"navitas-college-of-public-safety-(ncps)-distance"
},

{
    "number":float(data[316]),
    "year": "2016",
    "desc":"north-melbourne-college-distance"
},

{
    "number":float(data[317]),
    "year": "2016",
    "desc":"nova-institute-of-technology-distance"
},

{
    "number":float(data[318]),
    "year": "2016",
    "desc":"oceania-polytechnic-institute-of-education-(opie)-distance"
},

{
    "number":float(data[319]),
    "year": "2016",
    "desc":"orange-international-college-distance"
},

{
    "number":float(data[320]),
    "year": "2016",
    "desc":"ozford-college-distance"
},

{
    "number":float(data[321]),
    "year": "2016",
    "desc":"ozford-college-of-busines-distance"
},

{
    "number":float(data[322]),
    "year": "2016",
    "desc":"ozford-college-of-business-distance"
},

{
    "number":float(data[323]),
    "year": "2016",
    "desc":"pax-institute-of-education-distance"
},

{
    "number":float(data[324]),
    "year": "2016",
    "desc":"pearson-aviation-essendon-airport-distance"
},

{
    "number":float(data[325]),
    "year": "2016",
    "desc":"photography-studies-college-(psc)-melbourne-campus-distance"
},

{
    "number":float(data[326]),
    "year": "2016",
    "desc":"pilgrim-theological-college-distance"
},

{
    "number":float(data[327]),
    "year": "2016",
    "desc":"planetshakers-college-distance"
},

{
    "number":float(data[328]),
    "year": "2016",
    "desc":"presbyterian-theological-college-box-hill-campus-distance"
},

{
    "number":float(data[329]),
    "year": "2016",
    "desc":"rabbinical-college-of-australia-and-n-z-distance"
},

{
    "number":float(data[330]),
    "year": "2016",
    "desc":"rc-(rhodes-college)-distance"
},

{
    "number":float(data[331]),
    "year": "2016",
    "desc":"reformed-theological-college-geelong-campus-distance"
},

{
    "number":float(data[332]),
    "year": "2016",
    "desc":"ridley-college-parkville-campus-distance"
},

{
    "number":float(data[333]),
    "year": "2016",
    "desc":"rmit-english-worldwide-distance"
},

{
    "number":float(data[334]),
    "year": "2016",
    "desc":"rmit-univeristy-brunswick-campus-distance"
},

{
    "number":float(data[335]),
    "year": "2016",
    "desc":"rmit-university-(rmit)-city-campus-distance"
},

{
    "number":float(data[336]),
    "year": "2016",
    "desc":"rmit-university-bundoora-campus-distance"
},

{
    "number":float(data[337]),
    "year": "2016",
    "desc":"rmit-university-point-cook-campus-distance"
},

{
    "number":float(data[338]),
    "year": "2016",
    "desc":"royal-gurkhas-institute-of-technology-(rgit)-australia-gurkhas-institute-of-hospitality-management-distance"
},

{
    "number":float(data[339]),
    "year": "2016",
    "desc":"royal-gurkhas-institute-of-technology-australia-(rgit)-distance"
},

{
    "number":float(data[340]),
    "year": "2016",
    "desc":"royal-victorian-aero-club-distance"
},

{
    "number":float(data[341]),
    "year": "2016",
    "desc":"sae-institute-qantm-college-melbourne-campus-distance"
},

{
    "number":float(data[342]),
    "year": "2016",
    "desc":"school-for-f-m-alexander-studies-distance"
},

{
    "number":float(data[343]),
    "year": "2016",
    "desc":"south-australian-college-of-english-(sace)-melbourne-college-of-english-distance"
},

{
    "number":float(data[344]),
    "year": "2016",
    "desc":"south-pacific-institute-(spi)-melbourne-campus-distance"
},

{
    "number":float(data[345]),
    "year": "2016",
    "desc":"southern-cross-education-institute-(scei)-second-campus-distance"
},

{
    "number":float(data[346]),
    "year": "2016",
    "desc":"southern-cross-education-institute-(scei)-third-campus-distance"
},

{
    "number":float(data[347]),
    "year": "2016",
    "desc":"southern-school-of-natural-therapies-distance"
},

{
    "number":float(data[348]),
    "year": "2016",
    "desc":"st-aerospace-academy-(australia)-pty-ltd-2-bowral-court-mitchell-park-distance"
},

{
    "number":float(data[349]),
    "year": "2016",
    "desc":"st-peter-institute-bourke-street-campus-distance"
},

{
    "number":float(data[350]),
    "year": "2016",
    "desc":"st-peter-institute-little-collins-campus-distance"
},

{
    "number":float(data[351]),
    "year": "2016",
    "desc":"stott's-colleges-(front-cooking-school---carlton-campus)---vet-distance"
},

{
    "number":float(data[352]),
    "year": "2016",
    "desc":"stott's-colleges-box-hill-campus-distance"
},

{
    "number":float(data[353]),
    "year": "2016",
    "desc":"stott's-colleges-melbourne-campus-distance"
},

{
    "number":float(data[354]),
    "year": "2016",
    "desc":"strathfield-college-melbourne-campus-distance"
},

{
    "number":float(data[355]),
    "year": "2016",
    "desc":"sunraysia-institute-of-tafe-mildura-campus-distance"
},

{
    "number":float(data[356]),
    "year": "2016",
    "desc":"sunshine-college-of-management-distance"
},

{
    "number":float(data[357]),
    "year": "2016",
    "desc":"swinburne-university-of-technology-croydon-campus-distance"
},

{
    "number":float(data[358]),
    "year": "2016",
    "desc":"swinburne-university-of-technology-wantirna-campus-distance"
},

{
    "number":float(data[359]),
    "year": "2016",
    "desc":"swinburne-university-of-technology-hawthorn-campus-distance"
},

{
    "number":float(data[360]),
    "year": "2016",
    "desc":"technical-education-development-institute-distance"
},

{
    "number":float(data[361]),
    "year": "2016",
    "desc":"technical-institute-of-victoria-distance"
},

{
    "number":float(data[362]),
    "year": "2016",
    "desc":"the-university-of-melbourne-southbank-campus-distance"
},

{
    "number":float(data[363]),
    "year": "2016",
    "desc":"the-academy-of-interactive-entertainment-melbourne-campus-distance"
},

{
    "number":float(data[364]),
    "year": "2016",
    "desc":"the-australian-ballet-school-distance"
},

{
    "number":float(data[365]),
    "year": "2016",
    "desc":"the-australian-conservatoire-of-ballet-melbourne-campus-distance"
},

{
    "number":float(data[366]),
    "year": "2016",
    "desc":"the-university-of-melbourne-burnley-campus-distance"
},

{
    "number":float(data[367]),
    "year": "2016",
    "desc":"the-university-of-melbourne-distance"
},

{
    "number":float(data[368]),
    "year": "2016",
    "desc":"the-university-of-melbourne-werribee-campus-distance"
},

{
    "number":float(data[369]),
    "year": "2016",
    "desc":"tmg-college-distance"
},

{
    "number":float(data[370]),
    "year": "2016",
    "desc":"torrens-university-fitzroy-campus-distance"
},

{
    "number":float(data[371]),
    "year": "2016",
    "desc":"torrens-university-flinders-st-campus-distance"
},

{
    "number":float(data[372]),
    "year": "2016",
    "desc":"trinity-college-theological-school-distance"
},

{
    "number":float(data[373]),
    "year": "2016",
    "desc":"turner-english-box-hill-campus-distance"
},

{
    "number":float(data[374]),
    "year": "2016",
    "desc":"turner-english-camberwell-campus-distance"
},

{
    "number":float(data[375]),
    "year": "2016",
    "desc":"turner-english-dandenong-campus-distance"
},

{
    "number":float(data[376]),
    "year": "2016",
    "desc":"turner-english-melbourne-cbd-campus-distance"
},

{
    "number":float(data[377]),
    "year": "2016",
    "desc":"univeristy-of-divinity-whitley-college-distance"
},

{
    "number":float(data[378]),
    "year": "2016",
    "desc":"universal-institute-of-technology-distance"
},

{
    "number":float(data[379]),
    "year": "2016",
    "desc":"university-of-canberra-uc-melbourne---chadstone-campus-distance"
},

{
    "number":float(data[380]),
    "year": "2016",
    "desc":"university-of-divinity-stirling-college-distance"
},

{
    "number":float(data[381]),
    "year": "2016",
    "desc":"university-of-divinity-yarra-theological-union-distance"
},

{
    "number":float(data[382]),
    "year": "2016",
    "desc":"victoria-university-city-flinders-distance"
},

{
    "number":float(data[383]),
    "year": "2016",
    "desc":"victoria-university-city-flinders-lane-distance"
},

{
    "number":float(data[384]),
    "year": "2016",
    "desc":"victoria-university-city-queen-distance"
},

{
    "number":float(data[385]),
    "year": "2016",
    "desc":"victoria-university-footscray-nicholson-distance"
},

{
    "number":float(data[386]),
    "year": "2016",
    "desc":"victoria-university-footscray-park-distance"
},

{
    "number":float(data[387]),
    "year": "2016",
    "desc":"victoria-university-st-albans-distance"
},

{
    "number":float(data[388]),
    "year": "2016",
    "desc":"victoria-university-sunshine-distance"
},

{
    "number":float(data[389]),
    "year": "2016",
    "desc":"victoria-university-werribee-distance"
},

{
    "number":float(data[390]),
    "year": "2016",
    "desc":"victoria-university-city-king-distance"
},

{
    "number":float(data[391]),
    "year": "2016",
    "desc":"victorian-academy-of-commerce-and-technology-startups-(vacts)-distance"
},

{
    "number":float(data[392]),
    "year": "2016",
    "desc":"victorian-institute-of-culinary-arts-technology-main-campus---spotswood-distance"
},

{
    "number":float(data[393]),
    "year": "2016",
    "desc":"victorian-institute-of-culinary-arts-technology-regional-campus-1---kerang-scoresby-st-distance"
},

{
    "number":float(data[394]),
    "year": "2016",
    "desc":"victorian-institute-of-culinary-arts-technology-regional-campus-2---kerang-wellington-st-distance"
},

{
    "number":float(data[395]),
    "year": "2016",
    "desc":"victorian-institute-of-culinary-arts-technology-regional-campus-3---shepparton-distance"
},

{
    "number":float(data[396]),
    "year": "2016",
    "desc":"vit-(victorian-institute-of-technology)-abbotsford-campus-distance"
},

{
    "number":float(data[397]),
    "year": "2016",
    "desc":"vit-(victorian-institute-of-technology)-melbourne-cbd-campus-distance"
},

{
    "number":float(data[398]),
    "year": "2016",
    "desc":"whitehouse-institute-of-design-australia-distance"
},

{
    "number":float(data[399]),
    "year": "2016",
    "desc":"william-angliss-institute-distance"
},

{
    "number":float(data[400]),
    "year": "2016",
    "desc":"yorke-institute-distance"
},

{
    "number":bool(data[167]),
    "year": "2016",
    "desc":"bus-line-flag"
},

{
    "number":bool(data[168]),
    "year": "2016",
    "desc":"ferry-flag"
},

{
    "number":bool(data[646]),
    "year": "2016",
    "desc":"suburb-aged-care-residential-services-fac-flag"
},

{
    "number":bool(data[656]),
    "year": "2016",
    "desc":"suburb-allied-health-services-fac-flag"
},

{
    "number":bool(data[654]),
    "year": "2016",
    "desc":"suburb-ambulance-services-fac-flag"
},

{
    "number":bool(data[644]),
    "year": "2016",
    "desc":"suburb-chiropractic-and-osteopathic-services-fac-flag"
},

{
    "number":bool(data[651]),
    "year": "2016",
    "desc":"suburb-dental-services-fac-flag"
},

{
    "number":bool(data[648]),
    "year": "2016",
    "desc":"suburb-general-practice-medical-services-fac-flag"
},

{
    "number":bool(data[658]),
    "year": "2016",
    "desc":"suburb-hospital-fac-flag"
},

{
    "number":bool(data[645]),
    "year": "2016",
    "desc":"suburb-hospitals-except-psychiatric-hospitals-fac-flag"
},

{
    "number":bool(data[642]),
    "year": "2016",
    "desc":"suburb-med-fac-flag"
},

{
    "number":bool(data[661]),
    "year": "2016",
    "desc":"suburb-medical-and-other-health-care-services-fac-flag"
},

{
    "number":bool(data[659]),
    "year": "2016",
    "desc":"suburb-medical-services-fac-flag"
},

{
    "number":bool(data[652]),
    "year": "2016",
    "desc":"suburb-optometry-optical-dispensing-services-fac-flag"
},

{
    "number":bool(data[647]),
    "year": "2016",
    "desc":"suburb-other-allied-health-services-fac-flag"
},

{
    "number":bool(data[653]),
    "year": "2016",
    "desc":"suburb-other-health-care-services-fac-flag"
},

{
    "number":bool(data[660]),
    "year": "2016",
    "desc":"suburb-other-residential-care-services-fac-flag"
},

{
    "number":bool(data[643]),
    "year": "2016",
    "desc":"suburb-pathology-and-diagnostic-imaging-services-fac-flag"
},

{
    "number":bool(data[649]),
    "year": "2016",
    "desc":"suburb-physiotherapy-services-fac-flag"
},

{
    "number":bool(data[682]),
    "year": "2016",
    "desc":"suburb-police-station-flag"
},

{
    "number":bool(data[657]),
    "year": "2016",
    "desc":"suburb-psychiatric-hospitals-fac-flag"
},

{
    "number":bool(data[655]),
    "year": "2016",
    "desc":"suburb-residential-care-services-fac-flag"
},

{
    "number":bool(data[650]),
    "year": "2016",
    "desc":"suburb-specialist-medical-services-fac-flag"
},

{
    "number":bool(data[166]),
    "year": "2016",
    "desc":"train-station-flag"
},

{
    "number":bool(data[169]),
    "year": "2016",
    "desc":"tram-line-flag"
},




            },
            "language": {
                "acholi": int(data[28]),
"african-languages-nec": int(data[29]),
"african-languages-nfd": int(data[30]),
"afrikaans": int(data[31]),
"akan": int(data[32]),
"albanian": int(data[33]),
"amharic": int(data[34]),
"anuak": int(data[35]),
"arabic": int(data[36]),
"armenian": int(data[37]),
"assyrian-neo-aramaic": int(data[38]),
"bengali": int(data[39]),
"bisaya": int(data[40]),
"bosnian": int(data[41]),
"bulgarian": int(data[42]),
"burmese": int(data[43]),
"burmese-and-related-languages-nec": int(data[44]),
"burmese-and-related-languages-nfd": int(data[45]),
"cantonese": int(data[46]),
"catalan": int(data[47]),
"cebuano": int(data[48]),
"chaldean-neo-aramaic": int(data[49]),
"chin-haka": int(data[50]),
"chinese-nfd": int(data[51]),
"creole-nfd": int(data[52]),
"croatian": int(data[53]),
"czech": int(data[54]),
"danish": int(data[55]),
"dari": int(data[56]),
"dhivehi": int(data[57]),
"dinka": int(data[58]),
"dravidian-nec": int(data[59]),
"dutch": int(data[60]),
"english": int(data[61]),
"estonian": int(data[62]),
"fijian": int(data[63]),
"filipino": int(data[64]),
"finnish": int(data[65]),
"french": int(data[66]),
"french-creole-nfd": int(data[67]),
"german": int(data[68]),
"greek": int(data[69]),
"gujarati": int(data[70]),
"hakka": int(data[71]),
"harari": int(data[72]),
"hausa": int(data[73]),
"hazaraghi": int(data[74]),
"hebrew": int(data[75]),
"hindi": int(data[76]),
"hungarian": int(data[77]),
"iban": int(data[78]),
"igbo": int(data[79]),
"ilonggo-hiligaynon-": int(data[80]),
"inadequately-described": int(data[81]),
"indonesian": int(data[82]),
"iranic-nfd": int(data[83]),
"italian": int(data[84]),
"japanese": int(data[85]),
"kannada": int(data[86]),
"karen": int(data[87]),
"khmer": int(data[88]),
"kinyarwanda-rwanda-": int(data[89]),
"kirundi-rundi-": int(data[90]),
"konkani": int(data[91]),
"korean": int(data[92]),
"kurdish": int(data[93]),
"lao": int(data[94]),
"lithuanian": int(data[95]),
"loma-lorma-": int(data[96]),
"luganda": int(data[97]),
"macedonian": int(data[98]),
"malay": int(data[99]),
"malayalam": int(data[100]),
"maltese": int(data[101]),
"mandarin": int(data[102]),
"maori-cook-island-": int(data[103]),
"maori-new-zealand-": int(data[104]),
"marathi": int(data[105]),
"mauritian-creole": int(data[106]),
"min-nan": int(data[107]),
"mongolian": int(data[108]),
"nepali": int(data[109]),
"norwegian": int(data[110]),
"not-stated": int(data[111]),
"nuer": int(data[112]),
"nyanja-chichewa-": int(data[113]),
"oriya": int(data[114]),
"oromo": int(data[115]),
"other-southern-asian-languages": int(data[116]),
"pashto": int(data[117]),
"persian-excluding-dari-": int(data[118]),
"pidgin-nfd": int(data[119]),
"polish": int(data[120]),
"portuguese": int(data[121]),
"punjabi": int(data[122]),
"rohingya": int(data[123]),
"romanian": int(data[124]),
"russian": int(data[125]),
"samoan": int(data[126]),
"serbian": int(data[127]),
"shilluk": int(data[128]),
"shona": int(data[129]),
"sindhi": int(data[130]),
"sinhalese": int(data[131]),
"slovak": int(data[132]),
"slovene": int(data[133]),
"somali": int(data[134]),
"southern-asian-languages-nfd": int(data[135]),
"spanish": int(data[136]),
"swahili": int(data[137]),
"swedish": int(data[138]),
"tagalog": int(data[139]),
"tamil": int(data[140]),
"telugu": int(data[141]),
"tetum": int(data[142]),
"thai": int(data[143]),
"tibetan": int(data[144]),
"tigrinya": int(data[145]),
"tok-pisin-neomelanesian-": int(data[146]),
"tongan": int(data[147]),
"tswana": int(data[148]),
"turkish": int(data[149]),
"tuvaluan": int(data[150]),
"ukrainian": int(data[151]),
"urdu": int(data[152]),
"vietnamese": int(data[153]),
"wu": int(data[154]),
"yoruba": int(data[155]),
"zomi": int(data[156]),
            },
            "universities": {
"aapoly-melbourne-campus": {"number": int(data[402]), "year": "2016"},
"academia-international-melbourne-campus": {"number": int(data[403]), "year": "2016"},
"acumen-institute-of-further-education-cbd-campus": {"number": int(data[404]), "year": "2016"},
"acumen-institute-of-further-education-richmond-campus": {"number": int(data[405]), "year": "2016"},
"agb-training-geelong-campus": {"number": int(data[406]), "year": "2016"},
"alacc-health-college-australia": {"number": int(data[407]), "year": "2016"},
"alfred-deakin-college-mibt-waurn-ponds-campus": {"number": int(data[408]), "year": "2016"},
"altec-college-melbourne-campus": {"number": int(data[409]), "year": "2016"},
"angad-australian-institute-of-technology-la-trobe-st-campus": {"number": int(data[410]), "year": "2016"},
"aoi-institute": {"number": int(data[411]), "year": "2016"},
"ashton-college-footscray-campus": {"number": int(data[412]), "year": "2016"},
"ashton-college-hallam-campus": {"number": int(data[413]), "year": "2016"},
"ashton-college-hospitality-campus": {"number": int(data[414]), "year": "2016"},
"ashton-college-northcote-campus": {"number": int(data[415]), "year": "2016"},
"australian-academy-of-fashion-design": {"number": int(data[416]), "year": "2016"},
"australian-careers-education-donald-street-campus-aurora-building": {"number": int(data[417]), "year": "2016"},
"australian-careers-education-victoria-street-campus": {"number": int(data[418]), "year": "2016"},
"australian-catholic-univeristy-melbourne-campus": {"number": int(data[419]), "year": "2016"},
"australian-catholic-university-ballarat-campus": {"number": int(data[420]), "year": "2016"},
"australian-centre-of-further-education": {"number": int(data[421]), "year": "2016"},
"australian-college-of-applied-psychology-acap-melbourne-campus": {"number": int(data[422]), "year": "2016"},
"australian-college-of-sport-basketball-melbourne-campus": {"number": int(data[423]), "year": "2016"},
"australian-college-of-theology": {"number": int(data[424]), "year": "2016"},
"australian-college-of-trade-thornbury-campus": {"number": int(data[425]), "year": "2016"},
"australian-education-academy-10-blissington-street-springvale": {"number": int(data[426]), "year": "2016"},
"australian-institute-of-technical-training-aitt-melbourne-campus": {"number": int(data[427]), "year": "2016"},
"australian-institute-of-trades-institute-of-hotel-management-australia": {"number": int(data[428]), "year": "2016"},
"australian-institute-of-translation-interpretation-aiti-melbourne-campus": {"number": int(data[429]), "year": "2016"},
"australian-it-hospitality-institute-footscray-campus": {"number": int(data[430]), "year": "2016"},
"australian-national-airline-college": {"number": int(data[431]), "year": "2016"},
"australian-national-college-franklin-street-campus": {"number": int(data[432]), "year": "2016"},
"australian-national-institute-of-business-technology-anibt-melbourne-campus": {"number": int(data[433]), "year": "2016"},
"australian-pacific-college-melbourne-campus": {"number": int(data[434]), "year": "2016"},
"australian-study-link-institute": {"number": int(data[435]), "year": "2016"},
"aveta-australian-vocational-education-training-academy": {"number": int(data[436]), "year": "2016"},
"barkly-international-college-city-campus": {"number": int(data[437]), "year": "2016"},
"barkly-international-college-north-melbourne-campus-automotive-workshop": {"number": int(data[438]), "year": "2016"},
"baxter-institute-automotive-bakery-campus": {"number": int(data[439]), "year": "2016"},
"baxter-institute-fabrication-campus": {"number": int(data[440]), "year": "2016"},
"baxter-institute-hairdressing-and-beauty-campus-flinders-street": {"number": int(data[441]), "year": "2016"},
"beaconhills-college": {"number": int(data[442]), "year": "2016"},
"bendigo-tafe-bendigo": {"number": int(data[443]), "year": "2016"},
"bendigo-tafe-and-kangan-institute-broadmeadows-campus": {"number": int(data[444]), "year": "2016"},
"biba-academy-swantson-street-campus": {"number": int(data[445]), "year": "2016"},
"box-hill-institute-city-campus": {"number": int(data[446]), "year": "2016"},
"box-hill-institute": {"number": int(data[447]), "year": "2016"},
"brighton-institute-of-technology": {"number": int(data[448]), "year": "2016"},
"catholic-theological-college-ctc-melbourne-college-of-divinity-east-melbourne-campus": {"number": int(data[449]), "year": "2016"},
"central-australian-college-cac-melbourne-campus": {"number": int(data[450]), "year": "2016"},
"central-melbourne-institute-cmi-city-campus": {"number": int(data[451]), "year": "2016"},
"central-melbourne-institute": {"number": int(data[452]), "year": "2016"},
"central-queensland-university-city-campus": {"number": int(data[453]), "year": "2016"},
"charles-sturt-university-study-centres-melbourne": {"number": int(data[454]), "year": "2016"},
"chisholm-institue-chisholm-at-331": {"number": int(data[455]), "year": "2016"},
"chisholm-institute-bass-coast": {"number": int(data[456]), "year": "2016"},
"chisholm-institute-cranbourne-campus": {"number": int(data[457]), "year": "2016"},
"chisholm-institute-dandenong-campus": {"number": int(data[458]), "year": "2016"},
"chisholm-institute-flinders-lane-campus": {"number": int(data[459]), "year": "2016"},
"chisholm-institute-melbourne-city-campus": {"number": int(data[460]), "year": "2016"},
"collarts-australian-college-of-the-arts": {"number": int(data[461]), "year": "2016"},
"dalton-college": {"number": int(data[462]), "year": "2016"},
"dance-factory": {"number": int(data[463]), "year": "2016"},
"deakin-college-mibt-burwood-campus": {"number": int(data[464]), "year": "2016"},
"deakin-university-geelong-waterfront-campus": {"number": int(data[465]), "year": "2016"},
"deakin-university-warrnambool-campus": {"number": int(data[466]), "year": "2016"},
"deakin-university-waurn-ponds-campus": {"number": int(data[467]), "year": "2016"},
"della-international-college-city-campus": {"number": int(data[468]), "year": "2016"},
"della-international-college-sunshine-campus": {"number": int(data[469]), "year": "2016"},
"department-of-education-and-training-victoria": {"number": int(data[470]), "year": "2016"},
"east-west-college-of-natural-therapies": {"number": int(data[471]), "year": "2016"},
"education-access-australia": {"number": int(data[472]), "year": "2016"},
"education-training-employment-australia-etea": {"number": int(data[473]), "year": "2016"},
"elite-training-institute": {"number": int(data[474]), "year": "2016"},
"elly-lukas-beauty-therapy-college": {"number": int(data[475]), "year": "2016"},
"elsis-melbourne-campus": {"number": int(data[476]), "year": "2016"},
"endeavour-college-of-natural-health-melbourne-campus": {"number": int(data[477]), "year": "2016"},
"everest-institute-of-education": {"number": int(data[478]), "year": "2016"},
"explore-english": {"number": int(data[479]), "year": "2016"},
"federation-university-ballarat-campus": {"number": int(data[480]), "year": "2016"},
"federation-university-gippsland-campus": {"number": int(data[481]), "year": "2016"},
"federation-university-wimmera-campus": {"number": int(data[482]), "year": "2016"},
"flinders-international-college": {"number": int(data[483]), "year": "2016"},
"fusion-enlgish-melbourne-campus": {"number": int(data[484]), "year": "2016"},
"global-business-college-of-australia": {"number": int(data[485]), "year": "2016"},
"gordon-institute-of-tafe-east-geelong-campus": {"number": int(data[486]), "year": "2016"},
"gordon-institute-of-tafe-east-geelong-elicos-campus": {"number": int(data[487]), "year": "2016"},
"greenwich-english-college-melbourne": {"number": int(data[488]), "year": "2016"},
"harvest-bible-college": {"number": int(data[489]), "year": "2016"},
"hays-international-college": {"number": int(data[490]), "year": "2016"},
"heading-out-academy": {"number": int(data[491]), "year": "2016"},
"headmasters-advanced-academy-of-training": {"number": int(data[492]), "year": "2016"},
"holmesglen-holmesglen-institute-chadstone-campus": {"number": int(data[493]), "year": "2016"},
"holmesglen-holmesglen-institute-city-campus": {"number": int(data[494]), "year": "2016"},
"holmesglen-holmesglen-institute-waverley-campus": {"number": int(data[495]), "year": "2016"},
"holmesglen-institute-holmesglen-moorabbin-campus": {"number": int(data[496]), "year": "2016"},
"hospitality-management-institute-of-australia": {"number": int(data[497]), "year": "2016"},
"impact-english-college-melbourne-campus": {"number": int(data[498]), "year": "2016"},
"imperial-college-of-technology-and-management": {"number": int(data[499]), "year": "2016"},
"institute-of-health-and-nursing-australia": {"number": int(data[500]), "year": "2016"},
"institute-of-tertiary-and-higher-education-australia-ithea": {"number": int(data[501]), "year": "2016"},
"inus-australia-education-and-training": {"number": int(data[502]), "year": "2016"},
"jmc-academy": {"number": int(data[503]), "year": "2016"},
"job-training-institute-dandenong-campus": {"number": int(data[504]), "year": "2016"},
"kangan-batman-institute-of-tafe-docklands": {"number": int(data[505]), "year": "2016"},
"kangan-batman-institute-of-tafe-richmond": {"number": int(data[506]), "year": "2016"},
"kangan-institute-moonee-ponds-campus": {"number": int(data[507]), "year": "2016"},
"kaplan-business-school": {"number": int(data[508]), "year": "2016"},
"la-trobe-bundoora-campus": {"number": int(data[509]), "year": "2016"},
"la-trobe-university-albury-wodonga-campus": {"number": int(data[510]), "year": "2016"},
"la-trobe-university-bendigo-campus": {"number": int(data[511]), "year": "2016"},
"la-trobe-university-city-campus-collins-street-city-campus-collins-street": {"number": int(data[512]), "year": "2016"},
"la-trobe-university-mildura-campus": {"number": int(data[513]), "year": "2016"},
"la-trobe-university-shepparton-campus": {"number": int(data[514]), "year": "2016"},
"latrobe-college-of-art-and-design": {"number": int(data[515]), "year": "2016"},
"lawson-college-australia": {"number": int(data[516]), "year": "2016"},
"lonsdale-institute-eurocentres-melbourne": {"number": int(data[517]), "year": "2016"},
"marcus-oldham-college": {"number": int(data[518]), "year": "2016"},
"megt-institute-melbourne-campus": {"number": int(data[519]), "year": "2016"},
"melbourne-college-of-hair-and-beauty": {"number": int(data[520]), "year": "2016"},
"melbourne-flight-training": {"number": int(data[521]), "year": "2016"},
"melbourne-institute-of-technology-federation-university-melbourne-campus": {"number": int(data[522]), "year": "2016"},
"melbourne-polytechnic-brunswick-campus": {"number": int(data[523]), "year": "2016"},
"melbourne-polytechnic-epping-campus": {"number": int(data[524]), "year": "2016"},
"melbourne-polytechnic-fairfield-campus": {"number": int(data[525]), "year": "2016"},
"melbourne-polytechnic-heidelberg-campus": {"number": int(data[526]), "year": "2016"},
"melbourne-polytechnic-preston-campus": {"number": int(data[527]), "year": "2016"},
"melbourne-polytechnic-preston-tafe-campus": {"number": int(data[528]), "year": "2016"},
"melbourne-rudolf-steiner-seminar": {"number": int(data[529]), "year": "2016"},
"melbourne-school-of-theology": {"number": int(data[530]), "year": "2016"},
"melbourne-university-hawthorn-english-language-centre": {"number": int(data[531]), "year": "2016"},
"melbourne-university-trinity-college": {"number": int(data[532]), "year": "2016"},
"menzies-institute-of-technology-adderley-campus": {"number": int(data[533]), "year": "2016"},
"menzies-institute-of-technology-batman-campus": {"number": int(data[534]), "year": "2016"},
"menzies-institute-of-technology-spencer-campus": {"number": int(data[535]), "year": "2016"},
"monash-college-monash-university-english-language-centre": {"number": int(data[536]), "year": "2016"},
"federation-university-berwick-campus": {"number": int(data[537]), "year": "2016"},
"monash-international-peninsula-campus": {"number": int(data[538]), "year": "2016"},
"monash-university-caulfield-campus": {"number": int(data[539]), "year": "2016"},
"monash-university-city-campus": {"number": int(data[540]), "year": "2016"},
"monash-university-clayton-campus": {"number": int(data[541]), "year": "2016"},
"monash-university-parkville-campus-manning-building": {"number": int(data[542]), "year": "2016"},
"monash-university-english-language-centre-monash-college-city-campus": {"number": int(data[543]), "year": "2016"},
"moorabbin-flying-services": {"number": int(data[544]), "year": "2016"},
"national-theatre-drama-ballet-school": {"number": int(data[545]), "year": "2016"},
"navitas-college-of-public-safety-ncps": {"number": int(data[546]), "year": "2016"},
"north-melbourne-college": {"number": int(data[547]), "year": "2016"},
"nova-institute-of-technology": {"number": int(data[548]), "year": "2016"},
"oceania-polytechnic-institute-of-education-opie": {"number": int(data[549]), "year": "2016"},
"orange-international-college": {"number": int(data[550]), "year": "2016"},
"ozford-college-of-busines": {"number": int(data[551]), "year": "2016"},
"ozford-college-of-business": {"number": int(data[552]), "year": "2016"},
"ozford-college": {"number": int(data[553]), "year": "2016"},
"pax-institute-of-education": {"number": int(data[554]), "year": "2016"},
"pearson-aviation-essendon-airport": {"number": int(data[555]), "year": "2016"},
"photography-studies-college-psc-melbourne-campus": {"number": int(data[556]), "year": "2016"},
"pilgrim-theological-college": {"number": int(data[557]), "year": "2016"},
"planetshakers-college": {"number": int(data[558]), "year": "2016"},
"presbyterian-theological-college-box-hill-campus": {"number": int(data[559]), "year": "2016"},
"rabbinical-college-of-australia-and-n-z": {"number": int(data[560]), "year": "2016"},
"rc-rhodes-college": {"number": int(data[561]), "year": "2016"},
"reformed-theological-college-geelong-campus": {"number": int(data[562]), "year": "2016"},
"ridley-college-parkville-campus": {"number": int(data[563]), "year": "2016"},
"rmit-english-worldwide": {"number": int(data[564]), "year": "2016"},
"rmit-univeristy-brunswick-campus": {"number": int(data[565]), "year": "2016"},
"rmit-university-rmit-city-campus": {"number": int(data[566]), "year": "2016"},
"rmit-university-bundoora-campus": {"number": int(data[567]), "year": "2016"},
"rmit-university-point-cook-campus": {"number": int(data[568]), "year": "2016"},
"royal-gurkhas-institute-of-technology-rgit-australia-gurkhas-institute-of-hospitality-management": {"number": int(data[569]), "year": "2016"},
"royal-gurkhas-institute-of-technology-australia-rgit": {"number": int(data[570]), "year": "2016"},
"royal-victorian-aero-club": {"number": int(data[571]), "year": "2016"},
"sae-institute-qantm-college-melbourne-campus": {"number": int(data[572]), "year": "2016"},
"school-for-f-m-alexander-studies": {"number": int(data[573]), "year": "2016"},
"south-australian-college-of-english-sace-melbourne-college-of-english": {"number": int(data[574]), "year": "2016"},
"south-pacific-institute-spi-melbourne-campus": {"number": int(data[575]), "year": "2016"},
"southern-cross-education-institute-scei-second-campus": {"number": int(data[576]), "year": "2016"},
"southern-cross-education-institute-scei-third-campus": {"number": int(data[577]), "year": "2016"},
"southern-school-of-natural-therapies": {"number": int(data[578]), "year": "2016"},
"st-aerospace-academy-australia-pty-ltd-2-bowral-court-mitchell-park": {"number": int(data[579]), "year": "2016"},
"st-peter-institute-bourke-street-campus": {"number": int(data[580]), "year": "2016"},
"st-peter-institute-little-collins-campus": {"number": int(data[581]), "year": "2016"},
"stott-s-colleges-front-cooking-school-carlton-campus-vet": {"number": int(data[582]), "year": "2016"},
"stott-s-colleges-box-hill-campus": {"number": int(data[583]), "year": "2016"},
"stott-s-colleges-melbourne-campus": {"number": int(data[584]), "year": "2016"},
"strathfield-college-melbourne-campus": {"number": int(data[585]), "year": "2016"},
"sunraysia-institute-of-tafe-mildura-campus": {"number": int(data[586]), "year": "2016"},
"sunshine-college-of-management": {"number": int(data[587]), "year": "2016"},
"swinburne-university-of-technology-croydon-campus": {"number": int(data[588]), "year": "2016"},
"swinburne-university-of-technology-wantirna-campus": {"number": int(data[589]), "year": "2016"},
"swinburne-university-of-technology-hawthorn-campus": {"number": int(data[590]), "year": "2016"},
"technical-education-development-institute": {"number": int(data[591]), "year": "2016"},
"technical-institute-of-victoria": {"number": int(data[592]), "year": "2016"},
"the-university-of-melbourne-southbank-campus": {"number": int(data[593]), "year": "2016"},
"the-academy-of-interactive-entertainment-melbourne-campus": {"number": int(data[594]), "year": "2016"},
"the-australian-ballet-school": {"number": int(data[595]), "year": "2016"},
"the-australian-conservatoire-of-ballet-melbourne-campus": {"number": int(data[596]), "year": "2016"},
"the-university-of-melbourne-burnley-campus": {"number": int(data[597]), "year": "2016"},
"the-university-of-melbourne": {"number": int(data[598]), "year": "2016"},
"the-university-of-melbourne-werribee-campus": {"number": int(data[599]), "year": "2016"},
"tmg-college": {"number": int(data[600]), "year": "2016"},
"torrens-university-fitzroy-campus": {"number": int(data[601]), "year": "2016"},
"torrens-university-flinders-st-campus": {"number": int(data[602]), "year": "2016"},
"trinity-college-theological-school": {"number": int(data[603]), "year": "2016"},
"turner-english-box-hill-campus": {"number": int(data[604]), "year": "2016"},
"turner-english-camberwell-campus": {"number": int(data[605]), "year": "2016"},
"turner-english-dandenong-campus": {"number": int(data[606]), "year": "2016"},
"turner-english-melbourne-cbd-campus": {"number": int(data[607]), "year": "2016"},
"univeristy-of-divinity-whitley-college": {"number": int(data[608]), "year": "2016"},
"universal-institute-of-technology": {"number": int(data[609]), "year": "2016"},
"university-of-canberra-uc-melbourne-chadstone-campus": {"number": int(data[610]), "year": "2016"},
"university-of-divinity-stirling-college": {"number": int(data[611]), "year": "2016"},
"university-of-divinity-yarra-theological-union": {"number": int(data[612]), "year": "2016"},
"victoria-university-city-flinders-lane": {"number": int(data[613]), "year": "2016"},
"victoria-university-city-flinders": {"number": int(data[614]), "year": "2016"},
"victoria-university-city-queen": {"number": int(data[615]), "year": "2016"},
"victoria-university-footscray-nicholson": {"number": int(data[616]), "year": "2016"},
"victoria-university-footscray-park": {"number": int(data[617]), "year": "2016"},
"victoria-university-st-albans": {"number": int(data[618]), "year": "2016"},
"victoria-university-sunshine": {"number": int(data[619]), "year": "2016"},
"victoria-university-werribee": {"number": int(data[620]), "year": "2016"},
"victoria-university-city-king": {"number": int(data[621]), "year": "2016"},
"victorian-academy-of-commerce-and-technology-startups-vacts": {"number": int(data[622]), "year": "2016"},
"victorian-institute-of-culinary-arts-technology-main-campus-spotswood": {"number": int(data[623]), "year": "2016"},
"victorian-institute-of-culinary-arts-technology-regional-campus-1-kerang-scoresby-st": {"number": int(data[624]), "year": "2016"},
"victorian-institute-of-culinary-arts-technology-regional-campus-2-kerang-wellington-st": {"number": int(data[625]), "year": "2016"},
"victorian-institute-of-culinary-arts-technology-regional-campus-3-shepparton": {"number": int(data[626]), "year": "2016"},
"vit-victorian-institute-of-technology-abbotsford-campus": {"number": int(data[627]), "year": "2016"},
"vit-victorian-institute-of-technology-melbourne-cbd-campus": {"number": int(data[628]), "year": "2016"},
"whitehouse-institute-of-design-australia": {"number": int(data[629]), "year": "2016"},
"william-angliss-institute": {"number": int(data[630]), "year": "2016"},
"yorke-institute": {"number": int(data[631]), "year": "2016"},

            }
        }


with open('IE_DATA_COMP_6_05_2018.csv', 'rb') as csvfile:
    readr = csv.reader(csvfile, delimiter=',')
    # readr.next()
    readr.next()
    for line in readr:
        print json.dumps(row_to_obj(line))
        #if(line[0]=="BROWN HILL"):
            #print line
#print line[620]