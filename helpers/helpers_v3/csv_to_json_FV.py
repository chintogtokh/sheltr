
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
                "lat": float(data[2]),
                "lng": float(data[3])
            },
            "stats": {
						"suburb-residents": {
							"number": int(data[4]),
							"year": "2016"

						},

						"total-crimes-by-year-and-area": {
							"number": int(data[6]),
							"year": "2016"

						},

						"offences-per-10000-population": {
							"number": float(data[7]),
							"year": "2016"

						},

						"suburb-town-name-2016-adjusted-crime-rank": {
							"number": int(data[8]),
							"year": "2016"

						},

						"offence-count": {
							"number": int(data[10]),
							"year": "2016"

						},

						"suburb-town-name-2016-real-crime-rank": {
							"number": int(data[11]),
							"year": "2016"

						},

						"suburb-most-common-expense-tier": {
							"number": (data[12]),
							"year": "2016"

						},

						"number-of-rental-properties": {
							"number": int(data[13]),
							"year": "2016"

						},

						"price-range-rank": {
							"number": int(data[14]),
							"year": "2016"

						},

						"rental-price-range-lower": {
							"number": int(data[15]),
							"year": "2016"

						},

						"rental-price-range-upper": {
							"number": int(data[16]),
							"year": "2016"

						},

						"suburb-most-int-student-lang": {
							"number": data[20],
							"year": "2016"

						},

						"total-int-students-per-suburb": {
							"number": int(data[21]),
							"year": "2016"

						},

						"total-int-student-per-language": {
							"number": int(data[22]),
							"year": "2016"

						},

						"student-population-rating": {
							"number": int(data[23]),
							"year": "2016"

						},

						"suburb-largest-lang-int-student-pop": {
							"number": int(data[24]),
							"year": "2016"

						},

						"suburb-largest-int-student-lang": {
							"number": data[25],
							"year": "2016"

						},

						"percent-of-int-students-language-in-suburb": {
							"number": float(data[26]),
							"year": "2016"

						},

						"int-student-language-rank-all-langs": {
							"number": int(data[27]),
							"year": "2016"

						},

						"average-public-transport-users-per-suburb": {
							"number": float(data[157]),
							"year": "2016"

						},

						"total-public-transport-users-per-suburb": {
							"number": int(data[158]),
							"year": "2016"

						},

						"total-other-usage-by-suburb": {
							"number": float(data[159]),
							"year": "2016"

						},

						"adjusted-total-other-usage-scale-rank": {
							"number": int(data[160]),
							"year": "2016"

						},

						"adjusted-total-transport-use-per-suburb": {
							"number": float(data[161]),
							"year": "2016"

						},

						"adjusted-total-transport-use-per-suburb-rank": {
							"number": int(data[162]),
							"year": "2016"

						},

						"adjusted-total-transport-use-per-suburb-scale-rank": {
							"number": int(data[163]),
							"year": "2016"

						},

						"most-common-transport-method": {
							"number": (data[164]),
							"year": "2016"

						},

						"most-common-distance-per-suburb": {
							"number": (data[165]),
							"year": "2016"

						},

						"train-station-flag": {
							"number": (data[166]),
							"year": "2016"

						},

						"bus-line-flag": {
							"number": (data[167]),
							"year": "2016"

						},

						"ferry-flag": {
							"number": (data[168]),
							"year": "2016"

						},

						"tram-line-flag": {
							"number": (data[169]),
							"year": "2016"

						},
						"number-of-medical-workers": {
							"number": int(data[628]),
							"year": "2016"

						},

						"total-med-staff-per-suburb": {
							"number": int(data[629]),
							"year": "2016"

						},

						"suburb-med-staff-presence-by-type-rank": {
							"number": int(data[630]),
							"year": "2016"

						},

						"pop-per-doc": {
							"number": int(data[631]),
							"year": "2016"

						},

						"pop-per-doc-type": {
							"number": int(data[632]),
							"year": "2016"

						},

						"total-vic-med-staff": {
							"number": int(data[633]),
							"year": "2016"

						},

						"real-suburb-med-staff-presence-rank": {
							"number": int(data[634]),
							"year": "2016"

						},

						"suburb-adjusted-med-staff-presence-rank": {
							"number": int(data[635]),
							"year": "2016"

						},

						"suburb-adjusted-med-staff-by-type-presence-rank": {
							"number": int(data[636]),
							"year": "2016"

						},

						"population-adjusted-med-staff-rating": {
							"number": int(data[637]),
							"year": "2016"

						},

						"suburb-med-fac-flag": {
							"number": (data[638]),
							"year": "2016"

						},

						"suburb-pathology-and-diagnostic-imaging-services-fac-flag": {
							"number": (data[639]),
							"year": "2016"

						},

						"suburb-chiropractic-and-osteopathic-services-fac-flag": {
							"number": (data[640]),
							"year": "2016"

						},

						"suburb-hospitals-except-psychiatric-hospitals-fac-flag": {
							"number": (data[641]),
							"year": "2016"

						},

						"suburb-aged-care-residential-services-fac-flag": {
							"number": (data[642]),
							"year": "2016"

						},

						"suburb-other-allied-health-services-fac-flag": {
							"number": (data[643]),
							"year": "2016"

						},

						"suburb-general-practice-medical-services-fac-flag": {
							"number": (data[644]),
							"year": "2016"

						},

						"suburb-physiotherapy-services-fac-flag": {
							"number": (data[645]),
							"year": "2016"

						},

						"suburb-specialist-medical-services-fac-flag": {
							"number": (data[646]),
							"year": "2016"

						},

						"suburb-dental-services-fac-flag": {
							"number": (data[647]),
							"year": "2016"

						},

						"suburb-optometry-optical-dispensing-services-fac-flag": {
							"number": (data[648]),
							"year": "2016"

						},

						"suburb-other-health-care-services-fac-flag": {
							"number": (data[649]),
							"year": "2016"

						},

						"suburb-ambulance-services-fac-flag": {
							"number": (data[650]),
							"year": "2016"

						},

						"suburb-residential-care-services-fac-flag": {
							"number": (data[651]),
							"year": "2016"

						},

						"suburb-allied-health-services-fac-flag": {
							"number": (data[652]),
							"year": "2016"

						},

						"suburb-psychiatric-hospitals-fac-flag": {
							"number": (data[653]),
							"year": "2016"

						},

						"suburb-hospital-fac-flag": {
							"number": (data[654]),
							"year": "2016"

						},

						"suburb-medical-services-fac-flag": {
							"number": (data[655]),
							"year": "2016"

						},

						"suburb-other-residential-care-services-fac-flag": {
							"number": (data[656]),
							"year": "2016"

						},

						"suburb-medical-and-other-health-care-services-fac-flag": {
							"number": (data[657]),
							"year": "2016"

						},

						"aged-care-residential-services": {
							"number": int(data[658]),
							"year": "2016"

						},

						"allied-health-services": {
							"number": int(data[659]),
							"year": "2016"

						},

						"ambulance-services": {
							"number": int(data[660]),
							"year": "2016"

						},

						"chiropractic-and-osteopathic-services": {
							"number": int(data[661]),
							"year": "2016"

						},

						"dental-services": {
							"number": int(data[662]),
							"year": "2016"

						},

						"general-practice-medical-services": {
							"number": int(data[663]),
							"year": "2016"

						},

						"hospitals": {
							"number": int(data[664]),
							"year": "2016"

						},

						"hospitals-except-psychiatric-hospitals": {
							"number": int(data[665]),
							"year": "2016"

						},

						"medical-and-other-health-care-services": {
							"number": int(data[666]),
							"year": "2016"

						},

						"medical-services": {
							"number": int(data[667]),
							"year": "2016"

						},

						"no-medical-facilities-in-the-area": {
							"number": int(data[668]),
							"year": "2016"

						},

						"optometry-and-optical-dispensing": {
							"number": int(data[669]),
							"year": "2016"

						},

						"other-allied-health-services": {
							"number": int(data[670]),
							"year": "2016"

						},

						"other-residential-care-services": {
							"number": int(data[671]),
							"year": "2016"

						},

						"pathology-and-diagnostic-imaging-services": {
							"number": int(data[672]),
							"year": "2016"

						},

						"physiotherapy-services": {
							"number": int(data[673]),
							"year": "2016"

						},

						"psychiatric-hospitals": {
							"number": int(data[674]),
							"year": "2016"

						},

						"residential-care-services": {
							"number": int(data[675]),
							"year": "2016"

						},

						"specialist-medical-services": {
							"number": int(data[676]),
							"year": "2016"

						},

						"number-of-police-place-of-work": {
							"number": int(data[677]),
							"year": "2016"

						},

						"suburb-police-station-flag": {
							"number": (data[678]),
							"year": "2016"

						},

						"pop-per-cop": {
							"number": int(data[679]),
							"year": "2016"

						},

						"total-vic-pol": {
							"number": int(data[680]),
							"year": "2016"

						},

						"suburb-police-presence-rank": {
							"number": int(data[681]),
							"year": "2016"

						},

						"suburb-adjusted-police-presence-rank": {
							"number": int(data[682]),
							"year": "2016"

						},

						"population-adjusted-police-rating": {
							"number": int(data[683]),
							"year": "2016"

						}
					},

					"university_distances": {

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
                "kirundi-rundi-":int(data[90]),
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
                "zomi": int(data[156])
            },
            "universities": {
				"aapoly-ami-education": int(data[399]),
				"aapoly-melbourne-campus": int(data[400]),
				"academia-international-melbourne-campus": int(data[401]),
				"acumen-institute-of-further-education-cbd-campus": int(data[402]),
				"acumen-institute-of-further-education-richmond-campus": int(data[403]),
				"agb-training-geelong-campus": int(data[404]),
				"alacc-health-college-australia": int(data[405]),
				"alfred-deakin-college-(mibt)-waurn-ponds-campus": int(data[406]),
				"altec-college-melbourne-campus": int(data[407]),
				"angad-australian-institute-of-technology-la-trobe-st-campus": int(data[408]),
				"angad-australian-institute-of-technology-lonsdale-st-campus": int(data[409]),
				"aoi-institute": int(data[410]),
				"ashton-college-footscray-campus": int(data[411]),
				"ashton-college-hallam-campus": int(data[412]),
				"ashton-college-hospitality-campus": int(data[413]),
				"ashton-college-northcote-campus": int(data[414]),
				"australian-academy-of-fashion-design": int(data[415]),
				"australian-careers-education-donald-street-campus-(aurora-building)": int(data[416]),
				"australian-careers-education-victoria-street-campus": int(data[417]),
				"australian-catholic-univeristy-melbourne-campus": int(data[418]),
				"australian-catholic-university-ballarat-campus": int(data[419]),
				"australian-centre-of-further-education": int(data[420]),
				"australian-college-of-applied-psychology-acap--melbourne-campus": int(data[421]),
				"australian-college-of-sport-basketball-melbourne-campus": int(data[422]),
				"australian-college-of-theology": int(data[423]),
				"australian-college-of-trade-thornbury-campus": int(data[424]),
				"australian-education-academy-10-blissington-street-springvale": int(data[425]),
				"australian-institute-of-technical-training-(aitt)-melbourne-campus": int(data[426]),
				"australian-institute-of-trades-institute-of-hotel-management-australia": int(data[427]),
				"australian-institute-of-translation--interpretation-(aiti)-melbourne-campus": int(data[428]),
				"australian-it--hospitality-institute-footscray-campus": int(data[429]),
				"australian-national-airline-college": int(data[430]),
				"australian-national-college-franklin-street-campus": int(data[431]),
				"australian-national-institute-of-business--technology-(anibt)-melbourne-campus": int(data[432]),
				"australian-pacific-college-melbourne-campus": int(data[433]),
				"australian-study-link-institute": int(data[434]),
				"aveta--australian-vocational-education--training-academy": int(data[435]),
				"barkly-international-college-city-campus": int(data[436]),
				"barkly-international-college-north-melbourne-campus--automotive-workshop": int(data[437]),
				"barkly-international-college": int(data[438]),
				"baxter-institute-automotive--bakery-campus": int(data[439]),
				"baxter-institute-fabrication-campus": int(data[440]),
				"baxter-institute-hairdressing-and-beauty-campus-(flinders-street)": int(data[441]),
				"beaconhills-college": int(data[442]),
				"bendigo-tafe-bendigo": int(data[443]),
				"bendigo-tafe-and-kangan-institute-broadmeadows-campus": int(data[444]),
				"biba-academy-swantson-street-campus": int(data[445]),
				"box-hill-institute-city-campus": int(data[446]),
				"box-hill-institute": int(data[447]),
				"brighton-institute-of-technology": int(data[448]),
				"catholic-theological-college-(ctc)-melbourne-college-of-divinity--east-melbourne-campus": int(data[449]),
				"central-australian-college-(cac)-melbourne-campus": int(data[450]),
				"central-melbourne-institute-(cmi)-city-campus": int(data[451]),
				"central-melbourne-institute": int(data[452]),
				"charles-sturt-university-study-centres-melbourne": int(data[453]),
				"chisholm-institue-chisholm-at-331": int(data[454]),
				"chisholm-institute-bass-coast": int(data[455]),
				"chisholm-institute-cranbourne-campus": int(data[456]),
				"chisholm-institute-dandenong-campus": int(data[457]),
				"chisholm-institute-flinders-lane-campus": int(data[458]),
				"chisholm-institute-melbourne-city-campus": int(data[459]),
				"collarts--australian-college-of-the-arts": int(data[460]),
				"dalton-college": int(data[461]),
				"dance-factory": int(data[462]),
				"deakin-college-(mibt)-burwood-campus": int(data[463]),
				"deakin-university-burwood-campus": int(data[464]),
				"deakin-university-geelong-waterfront-campus": int(data[465]),
				"deakin-university-warrnambool-campus": int(data[466]),
				"deakin-university-waurn-ponds-campus": int(data[467]),
				"della-international-college-city-campus": int(data[468]),
				"della-international-college-sunshine-campus": int(data[469]),
				"department-of-education-and-training-victoria": int(data[470]),
				"east-west-college-of-natural-therapies": int(data[471]),
				"education-access-australia": int(data[472]),
				"education-training--employment-australia-etea": int(data[473]),
				"elite-training-institute": int(data[474]),
				"elly-lukas-beauty-therapy-college": int(data[475]),
				"elsis-melbourne-campus": int(data[476]),
				"endeavour-college-of-natural-health-melbourne-campus": int(data[477]),
				"everest-institute-of-education": int(data[478]),
				"explore-english": int(data[479]),
				"federation-university-ballarat-campus": int(data[480]),
				"flinders-international-college": int(data[481]),
				"fusion-enlgish-melbourne-campus": int(data[482]),
				"global-business-college-of-australia": int(data[483]),
				"gordon-institute-of-tafe-east-geelong-campus": int(data[484]),
				"gordon-institute-of-tafe-east-geelong-elicos-campus": int(data[485]),
				"greenwich-english-college-melbourne": int(data[486]),
				"harvest-bible-college": int(data[487]),
				"hays-international-college": int(data[488]),
				"heading-out-academy": int(data[489]),
				"headmasters-advanced-academy-of-training": int(data[490]),
				"holmesglen-holmesglen-institute-chadstone-campus": int(data[491]),
				"holmesglen-holmesglen-institute-city-campus": int(data[492]),
				"holmesglen-holmesglen-institute-waverley-campus": int(data[493]),
				"holmesglen-institute-holmesglen-moorabbin-campus": int(data[494]),
				"hospitality-management-institute-of-australia": int(data[495]),
				"impact-english-college-melbourne-campus": int(data[496]),
				"imperial-college-of-technology-and-management": int(data[497]),
				"institute-of-health-and-nursing-australia": int(data[498]),
				"institute-of-tertiary-and-higher-education-australia-(ithea)": int(data[499]),
				"inus-australia-education-and-training": int(data[500]),
				"jmc-academy": int(data[501]),
				"job-training-institute-dandenong-campus": int(data[502]),
				"kangan-batman-institute-of-tafe-docklands": int(data[503]),
				"kangan-batman-institute-of-tafe-richmond": int(data[504]),
				"kangan-institute-moonee-ponds-campus": int(data[505]),
				"kaplan-business-school": int(data[506]),
				"la-trobe-bundoora-campus": int(data[507]),
				"la-trobe-university-albury-wodonga-campus": int(data[508]),
				"la-trobe-university-bendigo-campus": int(data[509]),
				"la-trobe-university-city-campus-(collins-street)-city-campus-(collins-street)": int(data[510]),
				"la-trobe-university-melbourne-(bundoora)-campus": int(data[511]),
				"la-trobe-university-mildura-campus": int(data[512]),
				"la-trobe-university-shepparton-campus": int(data[513]),
				"latrobe-college-of-art-and-design": int(data[514]),
				"lawson-college-australia": int(data[515]),
				"lonsdale-institute-eurocentres-melbourne": int(data[516]),
				"marcus-oldham-college": int(data[517]),
				"megt-institute-melbourne-campus": int(data[518]),
				"melbourne-college-of-hair-and-beauty": int(data[519]),
				"melbourne-flight-training": int(data[520]),
				"melbourne-institute-of-technology-(federation-university)-melbourne-campus": int(data[521]),
				"melbourne-polytechnic-brunswick-campus": int(data[522]),
				"melbourne-polytechnic-epping-campus": int(data[523]),
				"melbourne-polytechnic-fairfield-campus": int(data[524]),
				"melbourne-polytechnic-heidelberg-campus": int(data[525]),
				"melbourne-polytechnic-preston-campus": int(data[526]),
				"melbourne-polytechnic-preston-tafe-campus": int(data[527]),
				"melbourne-rudolf-steiner-seminar": int(data[528]),
				"melbourne-school-of-theology": int(data[529]),
				"melbourne-university-hawthorn-english-language-centre": int(data[530]),
				"melbourne-university-trinity-college": int(data[531]),
				"menzies-institute-of-technology-adderley-campus": int(data[532]),
				"menzies-institute-of-technology-batman-campus": int(data[533]),
				"menzies-institute-of-technology-spencer-campus": int(data[534]),
				"monash-college-monash-university-english-language-centre": int(data[535]),
				"monash-international-berwick-campus": int(data[536]),
				"monash-international-peninsula-campus": int(data[537]),
				"monash-university-caulfield-campus": int(data[538]),
				"monash-university-city-campus": int(data[539]),
				"monash-university-clayton-campus": int(data[540]),
				"monash-university-gippsland-campus": int(data[541]),
				"monash-university-parkville-campus-(manning-building)": int(data[542]),
				"monash-university-english-language-centre-monash-college-city-campus": int(data[543]),
				"moorabbin-flying-services": int(data[544]),
				"national-theatre-(drama--ballet-school)": int(data[545]),
				"navitas-college-of-public-safety-(ncps)": int(data[546]),
				"north-melbourne-college": int(data[547]),
				"nova-institute-of-technology": int(data[548]),
				"oceania-polytechnic-institute-of-education-(opie)": int(data[549]),
				"orange-international-college": int(data[550]),
				"ozford-college-of-busines": int(data[551]),
				"ozford-college-of-business": int(data[552]),
				"ozford-college": int(data[553]),
				"pax-institute-of-education": int(data[554]),
				"pearson-aviation-essendon-airport": int(data[555]),
				"photography-studies-college-(psc)-melbourne-campus": int(data[556]),
				"pilgrim-theological-college": int(data[557]),
				"planetshakers-college": int(data[558]),
				"presbyterian-theological-college-box-hill-campus": int(data[559]),
				"rabbinical-college-of-australia-and-n-z-": int(data[560]),
				"rc-(rhodes-college)": int(data[561]),
				"reformed-theological-college-geelong-campus": int(data[562]),
				"ridley-college-parkville-campus": int(data[563]),
				"rmit-english-worldwide": int(data[564]),
				"rmit-univeristy-brunswick-campus": int(data[565]),
				"rmit-university-(rmit)-city-campus": int(data[566]),
				"rmit-university-bundoora-campus": int(data[567]),
				"rmit-university-point-cook-campus": int(data[568]),
				"royal-gurkhas-institute-of-technology-(rgit)-australia-gurkhas-institute-of-hospitality--management": int(data[569]),
				"royal-gurkhas-institute-of-technology-australia-(rgit)": int(data[570]),
				"royal-victorian-aero-club": int(data[571]),
				"sae-institute-qantm-college-melbourne-campus": int(data[572]),
				"school-for-f-m-alexander-studies": int(data[573]),
				"south-australian-college-of-english-(sace)-melbourne-college-of-english": int(data[574]),
				"south-pacific-institute-(spi)-melbourne-campus": int(data[575]),
				"southern-cross-education-institute-(scei)-second-campus": int(data[576]),
				"southern-cross-education-institute-(scei)-third-campus": int(data[577]),
				"southern-school-of-natural-therapies": int(data[578]),
				"st-peters-institute": int(data[579]),
				"st-aerospace-academy-(australia)-pty-ltd-2-bowral-court-mitchell-park": int(data[580]),
				"st-peter-institute-bourke-street-campus": int(data[581]),
				"st-peter-institute-little-collins-campus": int(data[582]),
				"stott's-colleges-(front-cooking-school--carlton-campus)--vet": int(data[583]),
				"stott's-colleges-box-hill-campus": int(data[584]),
				"stott's-colleges-melbourne-campus": int(data[585]),
				"strathfield-college-melbourne-campus": int(data[586]),
				"sunraysia-institute-of-tafe-mildura-campus": int(data[587]),
				"sunshine-college-of-management": int(data[588]),
				"swinburne-university-of-technology-hawthorn-campus": int(data[589]),
				"swinburne-university-of-technology-prahan-campus": int(data[590]),
				"technical-education-development-institute": int(data[591]),
				"technical-institute-of-victoria": int(data[592]),
				"the-academy-of-interactive-entertainment-melbourne-campus": int(data[593]),
				"the-australian-ballet-school": int(data[594]),
				"the-australian-conservatoire-of-ballet-melbourne-campus": int(data[595]),
				"the-university-of-melbourne": int(data[596]),
				"tmg-college": int(data[597]),
				"torrens-university-fitzroy-campus": int(data[598]),
				"torrens-university-flinders-st-campus": int(data[599]),
				"trinity-college-theological-school": int(data[600]),
				"turner-english-box-hill-campus": int(data[601]),
				"turner-english-camberwell-campus": int(data[602]),
				"turner-english-dandenong-campus": int(data[603]),
				"turner-english-melbourne-cbd-campus": int(data[604]),
				"univeristy-of-divinity-whitley-college": int(data[605]),
				"universal-institute-of-technology": int(data[606]),
				"university-of-canberra-uc-melbourne--chadstone-campus": int(data[607]),
				"university-of-divinity-stirling-college": int(data[608]),
				"university-of-divinity-yarra-theological-union": int(data[609]),
				"victoria-university-city-flinders": int(data[610]),
				"victoria-university-city-queen": int(data[611]),
				"victoria-university-footscray-nicholson": int(data[612]),
				"victoria-university-footscray-park": int(data[613]),
				"victoria-university-melbourne-campus": int(data[614]),
				"victoria-university-st-albans": int(data[615]),
				"victoria-university-sunshine": int(data[616]),
				"victoria-university-werribee": int(data[617]),
				"victorian-academy-of-commerce-and-technology-startups-(vacts)": int(data[618]),
				"victorian-institute-of-culinary-arts--technology-main-campus--spotswood": int(data[619]),
				"victorian-institute-of-culinary-arts--technology-regional-campus-1--kerang-scoresby-st": int(data[620]),
				"victorian-institute-of-culinary-arts--technology-regional-campus-2--kerang-wellington-st": int(data[621]),
				"victorian-institute-of-culinary-arts--technology-regional-campus-3--shepparton": int(data[622]),
				"vit-(victorian-institute-of-technology)-abbotsford-campus": int(data[623]),
				"vit-(victorian-institute-of-technology)-melbourne-cbd-campus": int(data[624]),
				"whitehouse-institute-of-design-australia": int(data[625]),
				"william-angliss-institute": int(data[626]),
				"yorke-institute": int(data[627])

            }
        }


with open('ITERATION_2_TMP_2.csv', 'rb') as csvfile:
    readr = csv.reader(csvfile, delimiter=',')
    # readr.next()
    readr.next()
    for line in readr:
        print json.dumps(row_to_obj(line))
		#if(line[0]=="BROWN HILL"):
            #print line
            #print line[620]
#print json.dumps(row_to_obj(line))