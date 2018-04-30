
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
            # "outlinks": {
            #     "realestate": data[18],
            #     "domain": data[19]
            # },
            "geojson": json_data,
            "coords": {
                "lat": float(data[2]),
                "lng": float(data[3])
            },
            "stats": [
						{
							"number": int(data[4]),
							"year": "2016",
							"desc":"suburb-residents"
						},

						{
							"number": int(data[6]),
							"year": "2016",
							"desc":"total-crimes-by-year-and-area"
						},

						{
							"number": float(data[7]),
							"year": "2016",
							"desc":"offences-per-10000-population"
						},

						{
							"number": int(data[8]),
							"year": "2016",
							"desc":"suburb-town-name-2016-adjusted-crime-rank"
						},

						{
							"number": int(data[10]),
							"year": "2016",
							"desc":"offence-count"
						},

						{
							"number": int(data[11]),
							"year": "2016",
							"desc":"suburb-town-name-2016-real-crime-rank"
						},

						{
							"number": (data[12]),
							"year": "2016",
							"desc":"suburb-most-common-expense-tier"
						},

						{
							"number": int(data[13]),
							"year": "2016",
							"desc":"number-of-rental-properties"
						},

						{
							"number": int(data[14]),
							"year": "2016",
							"desc":"price-range-rank"
						},

						{
							"number": int(data[15]),
							"year": "2016",
							"desc":"rental-price-range-lower"
						},

						{
							"number": int(data[16]),
							"year": "2016",
							"desc":"rental-price-range-upper"
						},

						{
							"number": data[20],
							"year": "2016",
							"desc":"suburb-most-int-student-lang"
						},

						{
							"number": int(data[21]),
							"year": "2016",
							"desc":"total-int-students-per-suburb"
						},

						{
							"number": int(data[22]),
							"year": "2016",
							"desc":"total-int-student-per-language"
						},

						{
							"number": int(data[23]),
							"year": "2016",
							"desc":"student-population-rating"
						},

						{
							"number": int(data[24]),
							"year": "2016",
							"desc":"suburb-largest-lang-int-student-pop"
						},

						{
							"number": data[25],
							"year": "2016",
							"desc":"suburb-largest-int-student-lang"
						},

						{
							"number": float(data[26]),
							"year": "2016",
							"desc":"percent-of-int-students-language-in-suburb"
						},

						{
							"number": int(data[27]),
							"year": "2016",
							"desc":"int-student-language-rank-all-langs"
						},

						{
							"number": float(data[157]),
							"year": "2016",
							"desc":"average-public-transport-users-per-suburb"
						},

						{
							"number": int(data[158]),
							"year": "2016",
							"desc":"total-public-transport-users-per-suburb"
						},

						{
							"number": float(data[159]),
							"year": "2016",
							"desc":"total-other-usage-by-suburb"
						},

						{
							"number": int(data[160]),
							"year": "2016",
							"desc":"adjusted-total-other-usage-scale-rank"
						},

						{
							"number": float(data[161]),
							"year": "2016",
							"desc":"adjusted-total-transport-use-per-suburb"
						},

						{
							"number": int(data[162]),
							"year": "2016",
							"desc":"adjusted-total-transport-use-per-suburb-rank"
						},

						{
							"number": int(data[163]),
							"year": "2016",
							"desc":"adjusted-total-transport-use-per-suburb-scale-rank"
						},

						{
							"number": (data[164]),
							"year": "2016",
							"desc":"most-common-transport-method"
						},

						{
							"number": (data[165]),
							"year": "2016",
							"desc":"most-common-distance-per-suburb"
						},

						{
							"number": (data[166]),
							"year": "2016",
							"desc":"train-station-flag"
						},

						{
							"number": (data[167]),
							"year": "2016",
							"desc":"bus-line-flag"
						},

						{
							"number": (data[168]),
							"year": "2016",
							"desc":"ferry-flag"
						},

						{
							"number": (data[169]),
							"year": "2016",
							"desc":"tram-line-flag"
						},

						{
							"number": float(data[170]),
							"year": "2016",
							"desc":"aapoly-ami-education-distance"
						},

						{
							"number": float(data[171]),
							"year": "2016",
							"desc":"aapoly-melbourne-campus-distance"
						},

						{
							"number": float(data[172]),
							"year": "2016",
							"desc":"academia-international-melbourne-campus-distance"
						},

						{
							"number": float(data[173]),
							"year": "2016",
							"desc":"acumen-institute-of-further-education-cbd-campus-distance"
						},

						{
							"number": float(data[174]),
							"year": "2016",
							"desc":"acumen-institute-of-further-education-richmond-campus-distance"
						},

						{
							"number": float(data[175]),
							"year": "2016",
							"desc":"agb-training-geelong-campus-distance"
						},

						{
							"number": float(data[176]),
							"year": "2016",
							"desc":"alacc-health-college-australia-distance"
						},

						{
							"number": float(data[177]),
							"year": "2016",
							"desc":"alfred-deakin-college-(mibt)-waurn-ponds-campus-distance"
						},

						{
							"number": float(data[178]),
							"year": "2016",
							"desc":"altec-college-melbourne-campus-distance"
						},

						{
							"number": float(data[179]),
							"year": "2016",
							"desc":"angad-australian-institute-of-technology-la-trobe-st-campus-distance"
						},

						{
							"number": float(data[180]),
							"year": "2016",
							"desc":"angad-australian-institute-of-technology-lonsdale-st-campus-distance"
						},

						{
							"number": float(data[181]),
							"year": "2016",
							"desc":"aoi-institute-distance"
						},

						{
							"number": float(data[182]),
							"year": "2016",
							"desc":"ashton-college-footscray-campus-distance"
						},

						{
							"number": float(data[183]),
							"year": "2016",
							"desc":"ashton-college-hallam-campus-distance"
						},

						{
							"number": float(data[184]),
							"year": "2016",
							"desc":"ashton-college-hospitality-campus-distance"
						},

						{
							"number": float(data[185]),
							"year": "2016",
							"desc":"ashton-college-northcote-campus-distance"
						},

						{
							"number": float(data[186]),
							"year": "2016",
							"desc":"australian-academy-of-fashion-design-distance"
						},

						{
							"number": float(data[187]),
							"year": "2016",
							"desc":"australian-careers-education-donald-street-campus-(aurora-building)-distance"
						},

						{
							"number": float(data[188]),
							"year": "2016",
							"desc":"australian-careers-education-victoria-street-campus-distance"
						},

						{
							"number": float(data[189]),
							"year": "2016",
							"desc":"australian-catholic-univeristy-melbourne-campus-distance"
						},

						{
							"number": float(data[190]),
							"year": "2016",
							"desc":"australian-catholic-university-ballarat-campus-distance"
						},

						{
							"number": float(data[191]),
							"year": "2016",
							"desc":"australian-centre-of-further-education-distance"
						},

						{
							"number": float(data[192]),
							"year": "2016",
							"desc":"australian-college-of-applied-psychology-acap--melbourne-campus-distance"
						},

						{
							"number": float(data[193]),
							"year": "2016",
							"desc":"australian-college-of-sport-basketball-melbourne-campus-distance"
						},

						{
							"number": float(data[194]),
							"year": "2016",
							"desc":"australian-college-of-theology-distance"
						},

						{
							"number": float(data[195]),
							"year": "2016",
							"desc":"australian-college-of-trade-thornbury-campus-distance"
						},

						{
							"number": float(data[196]),
							"year": "2016",
							"desc":"australian-education-academy-10-blissington-street-springvale-distance"
						},

						{
							"number": float(data[197]),
							"year": "2016",
							"desc":"australian-institute-of-technical-training-(aitt)-melbourne-campus-distance"
						},

						{
							"number": float(data[198]),
							"year": "2016",
							"desc":"australian-institute-of-trades-institute-of-hotel-management-australia-distance"
						},

						{
							"number": float(data[199]),
							"year": "2016",
							"desc":"australian-institute-of-translation--interpretation-(aiti)-melbourne-campus-distance"
						},

						{
							"number": float(data[200]),
							"year": "2016",
							"desc":"australian-it--hospitality-institute-footscray-campus-distance"
						},

						{
							"number": float(data[201]),
							"year": "2016",
							"desc":"australian-national-airline-college-distance"
						},

						{
							"number": float(data[202]),
							"year": "2016",
							"desc":"australian-national-college-franklin-street-campus-distance"
						},

						{
							"number": float(data[203]),
							"year": "2016",
							"desc":"australian-national-institute-of-business--technology-(anibt)-melbourne-campus-distance"
						},

						{
							"number": float(data[204]),
							"year": "2016",
							"desc":"australian-pacific-college-melbourne-campus-distance"
						},

						{
							"number": float(data[205]),
							"year": "2016",
							"desc":"australian-study-link-institute-distance"
						},

						{
							"number": float(data[206]),
							"year": "2016",
							"desc":"aveta--australian-vocational-education--training-academy-distance"
						},

						{
							"number": float(data[207]),
							"year": "2016",
							"desc":"barkly-international-college-city-campus-distance"
						},

						{
							"number": float(data[208]),
							"year": "2016",
							"desc":"barkly-international-college-north-melbourne-campus--automotive-workshop-distance"
						},

						{
							"number": float(data[209]),
							"year": "2016",
							"desc":"barkly-international-college-distance"
						},

						{
							"number": float(data[210]),
							"year": "2016",
							"desc":"baxter-institute-automotive--bakery-campus-distance"
						},

						{
							"number": float(data[211]),
							"year": "2016",
							"desc":"baxter-institute-fabrication-campus-distance"
						},

						{
							"number": float(data[212]),
							"year": "2016",
							"desc":"baxter-institute-hairdressing-and-beauty-campus-(flinders-street)-distance"
						},

						{
							"number": float(data[213]),
							"year": "2016",
							"desc":"beaconhills-college-distance"
						},

						{
							"number": float(data[214]),
							"year": "2016",
							"desc":"bendigo-tafe-bendigo-distance"
						},

						{
							"number": float(data[215]),
							"year": "2016",
							"desc":"bendigo-tafe-and-kangan-institute-broadmeadows-campus-distance"
						},

						{
							"number": float(data[216]),
							"year": "2016",
							"desc":"biba-academy-swantson-street-campus-distance"
						},

						{
							"number": float(data[217]),
							"year": "2016",
							"desc":"box-hill-institute-city-campus-distance"
						},

						{
							"number": float(data[218]),
							"year": "2016",
							"desc":"box-hill-institute-distance"
						},

						{
							"number": float(data[219]),
							"year": "2016",
							"desc":"brighton-institute-of-technology-distance"
						},

						{
							"number": float(data[220]),
							"year": "2016",
							"desc":"catholic-theological-college-(ctc)-melbourne-college-of-divinity--east-melbourne-campus-distance"
						},

						{
							"number": float(data[221]),
							"year": "2016",
							"desc":"central-australian-college-(cac)-melbourne-campus-distance"
						},

						{
							"number": float(data[222]),
							"year": "2016",
							"desc":"central-melbourne-institute-(cmi)-city-campus-distance"
						},

						{
							"number": float(data[223]),
							"year": "2016",
							"desc":"central-melbourne-institute-distance"
						},

						{
							"number": float(data[224]),
							"year": "2016",
							"desc":"charles-sturt-university-study-centres-melbourne-distance"
						},

						{
							"number": float(data[225]),
							"year": "2016",
							"desc":"chisholm-institue-chisholm-at-331-distance"
						},

						{
							"number": float(data[226]),
							"year": "2016",
							"desc":"chisholm-institute-bass-coast-distance"
						},

						{
							"number": float(data[227]),
							"year": "2016",
							"desc":"chisholm-institute-cranbourne-campus-distance"
						},

						{
							"number": float(data[228]),
							"year": "2016",
							"desc":"chisholm-institute-dandenong-campus-distance"
						},

						{
							"number": float(data[229]),
							"year": "2016",
							"desc":"chisholm-institute-flinders-lane-campus-distance"
						},

						{
							"number": float(data[230]),
							"year": "2016",
							"desc":"chisholm-institute-melbourne-city-campus-distance"
						},

						{
							"number": float(data[231]),
							"year": "2016",
							"desc":"collarts--australian-college-of-the-arts-distance"
						},

						{
							"number": float(data[232]),
							"year": "2016",
							"desc":"dalton-college-distance"
						},

						{
							"number": float(data[233]),
							"year": "2016",
							"desc":"dance-factory-distance"
						},

						{
							"number": float(data[234]),
							"year": "2016",
							"desc":"deakin-college-(mibt)-burwood-campus-distance"
						},

						{
							"number": float(data[235]),
							"year": "2016",
							"desc":"deakin-university-burwood-campus-distance"
						},

						{
							"number": float(data[236]),
							"year": "2016",
							"desc":"deakin-university-geelong-waterfront-campus-distance"
						},

						{
							"number": float(data[237]),
							"year": "2016",
							"desc":"deakin-university-warrnambool-campus-distance"
						},

						{
							"number": float(data[238]),
							"year": "2016",
							"desc":"deakin-university-waurn-ponds-campus-distance"
						},

						{
							"number": float(data[239]),
							"year": "2016",
							"desc":"della-international-college-city-campus-distance"
						},

						{
							"number": float(data[240]),
							"year": "2016",
							"desc":"della-international-college-sunshine-campus-distance"
						},

						{
							"number": float(data[241]),
							"year": "2016",
							"desc":"department-of-education-and-training-victoria-distance"
						},

						{
							"number": float(data[242]),
							"year": "2016",
							"desc":"east-west-college-of-natural-therapies-distance"
						},

						{
							"number": float(data[243]),
							"year": "2016",
							"desc":"education-access-australia-distance"
						},

						{
							"number": float(data[244]),
							"year": "2016",
							"desc":"education-training--employment-australia-etea-distance"
						},

						{
							"number": float(data[245]),
							"year": "2016",
							"desc":"elite-training-institute-distance"
						},

						{
							"number": float(data[246]),
							"year": "2016",
							"desc":"elly-lukas-beauty-therapy-college-distance"
						},

						{
							"number": float(data[247]),
							"year": "2016",
							"desc":"elsis-melbourne-campus-distance"
						},

						{
							"number": float(data[248]),
							"year": "2016",
							"desc":"endeavour-college-of-natural-health-melbourne-campus-distance"
						},

						{
							"number": float(data[249]),
							"year": "2016",
							"desc":"everest-institute-of-education-distance"
						},

						{
							"number": float(data[250]),
							"year": "2016",
							"desc":"explore-english-distance"
						},

						{
							"number": float(data[251]),
							"year": "2016",
							"desc":"federation-university-ballarat-campus-distance"
						},

						{
							"number": float(data[252]),
							"year": "2016",
							"desc":"flinders-international-college-distance"
						},

						{
							"number": float(data[253]),
							"year": "2016",
							"desc":"fusion-enlgish-melbourne-campus-distance"
						},

						{
							"number": float(data[254]),
							"year": "2016",
							"desc":"global-business-college-of-australia-distance"
						},

						{
							"number": float(data[255]),
							"year": "2016",
							"desc":"gordon-institute-of-tafe-east-geelong-campus-distance"
						},

						{
							"number": float(data[256]),
							"year": "2016",
							"desc":"gordon-institute-of-tafe-east-geelong-elicos-campus-distance"
						},

						{
							"number": float(data[257]),
							"year": "2016",
							"desc":"greenwich-english-college-melbourne-distance"
						},

						{
							"number": float(data[258]),
							"year": "2016",
							"desc":"harvest-bible-college-distance"
						},

						{
							"number": float(data[259]),
							"year": "2016",
							"desc":"hays-international-college-distance"
						},

						{
							"number": float(data[260]),
							"year": "2016",
							"desc":"heading-out-academy-distance"
						},

						{
							"number": float(data[261]),
							"year": "2016",
							"desc":"headmasters-advanced-academy-of-training-distance"
						},

						{
							"number": float(data[262]),
							"year": "2016",
							"desc":"holmesglen-holmesglen-institute-chadstone-campus-distance"
						},

						{
							"number": float(data[263]),
							"year": "2016",
							"desc":"holmesglen-holmesglen-institute-city-campus-distance"
						},

						{
							"number": float(data[264]),
							"year": "2016",
							"desc":"holmesglen-holmesglen-institute-waverley-campus-distance"
						},

						{
							"number": float(data[265]),
							"year": "2016",
							"desc":"holmesglen-institute-holmesglen-moorabbin-campus-distance"
						},

						{
							"number": float(data[266]),
							"year": "2016",
							"desc":"hospitality-management-institute-of-australia-distance"
						},

						{
							"number": float(data[267]),
							"year": "2016",
							"desc":"impact-english-college-melbourne-campus-distance"
						},

						{
							"number": float(data[268]),
							"year": "2016",
							"desc":"imperial-college-of-technology-and-management-distance"
						},

						{
							"number": float(data[269]),
							"year": "2016",
							"desc":"institute-of-health-and-nursing-australia-distance"
						},

						{
							"number": float(data[270]),
							"year": "2016",
							"desc":"institute-of-tertiary-and-higher-education-australia-(ithea)-distance"
						},

						{
							"number": float(data[271]),
							"year": "2016",
							"desc":"inus-australia-education-and-training-distance"
						},

						{
							"number": float(data[272]),
							"year": "2016",
							"desc":"jmc-academy-distance"
						},

						{
							"number": float(data[273]),
							"year": "2016",
							"desc":"job-training-institute-dandenong-campus-distance"
						},

						{
							"number": float(data[274]),
							"year": "2016",
							"desc":"kangan-batman-institute-of-tafe-docklands-distance"
						},

						{
							"number": float(data[275]),
							"year": "2016",
							"desc":"kangan-batman-institute-of-tafe-richmond-distance"
						},

						{
							"number": float(data[276]),
							"year": "2016",
							"desc":"kangan-institute-moonee-ponds-campus-distance"
						},

						{
							"number": float(data[277]),
							"year": "2016",
							"desc":"kaplan-business-school-distance"
						},

						{
							"number": float(data[278]),
							"year": "2016",
							"desc":"la-trobe-bundoora-campus-distance"
						},

						{
							"number": float(data[279]),
							"year": "2016",
							"desc":"la-trobe-university-albury-wodonga-campus-distance"
						},

						{
							"number": float(data[280]),
							"year": "2016",
							"desc":"la-trobe-university-bendigo-campus-distance"
						},

						{
							"number": float(data[281]),
							"year": "2016",
							"desc":"la-trobe-university-city-campus-(collins-street)-city-campus-(collins-street)-distance"
						},

						{
							"number": float(data[282]),
							"year": "2016",
							"desc":"la-trobe-university-melbourne-(bundoora)-campus-distance"
						},

						{
							"number": float(data[283]),
							"year": "2016",
							"desc":"la-trobe-university-mildura-campus-distance"
						},

						{
							"number": float(data[284]),
							"year": "2016",
							"desc":"la-trobe-university-shepparton-campus-distance"
						},

						{
							"number": float(data[285]),
							"year": "2016",
							"desc":"latrobe-college-of-art-and-design-distance"
						},

						{
							"number": float(data[286]),
							"year": "2016",
							"desc":"lawson-college-australia-distance"
						},

						{
							"number": float(data[287]),
							"year": "2016",
							"desc":"lonsdale-institute-eurocentres-melbourne-distance"
						},

						{
							"number": float(data[288]),
							"year": "2016",
							"desc":"marcus-oldham-college-distance"
						},

						{
							"number": float(data[289]),
							"year": "2016",
							"desc":"megt-institute-melbourne-campus-distance"
						},

						{
							"number": float(data[290]),
							"year": "2016",
							"desc":"melbourne-college-of-hair-and-beauty-distance"
						},

						{
							"number": float(data[291]),
							"year": "2016",
							"desc":"melbourne-flight-training-distance"
						},

						{
							"number": float(data[292]),
							"year": "2016",
							"desc":"melbourne-institute-of-technology-(federation-university)-melbourne-campus-distance"
						},

						{
							"number": float(data[293]),
							"year": "2016",
							"desc":"melbourne-polytechnic-brunswick-campus-distance"
						},

						{
							"number": float(data[294]),
							"year": "2016",
							"desc":"melbourne-polytechnic-epping-campus-distance"
						},

						{
							"number": float(data[295]),
							"year": "2016",
							"desc":"melbourne-polytechnic-fairfield-campus-distance"
						},

						{
							"number": float(data[296]),
							"year": "2016",
							"desc":"melbourne-polytechnic-heidelberg-campus-distance"
						},

						{
							"number": float(data[297]),
							"year": "2016",
							"desc":"melbourne-polytechnic-preston-campus-distance"
						},

						{
							"number": float(data[298]),
							"year": "2016",
							"desc":"melbourne-polytechnic-preston-tafe-campus-distance"
						},

						{
							"number": float(data[299]),
							"year": "2016",
							"desc":"melbourne-rudolf-steiner-seminar-distance"
						},

						{
							"number": float(data[300]),
							"year": "2016",
							"desc":"melbourne-school-of-theology-distance"
						},

						{
							"number": float(data[301]),
							"year": "2016",
							"desc":"melbourne-university-hawthorn-english-language-centre-distance"
						},

						{
							"number": float(data[302]),
							"year": "2016",
							"desc":"melbourne-university-trinity-college-distance"
						},

						{
							"number": float(data[303]),
							"year": "2016",
							"desc":"menzies-institute-of-technology-adderley-campus-distance"
						},

						{
							"number": float(data[304]),
							"year": "2016",
							"desc":"menzies-institute-of-technology-batman-campus-distance"
						},

						{
							"number": float(data[305]),
							"year": "2016",
							"desc":"menzies-institute-of-technology-spencer-campus-distance"
						},

						{
							"number": float(data[306]),
							"year": "2016",
							"desc":"monash-college-monash-university-english-language-centre-distance"
						},

						{
							"number": float(data[307]),
							"year": "2016",
							"desc":"monash-international-berwick-campus-distance"
						},

						{
							"number": float(data[308]),
							"year": "2016",
							"desc":"monash-international-peninsula-campus-distance"
						},

						{
							"number": float(data[309]),
							"year": "2016",
							"desc":"monash-university-caulfield-campus-distance"
						},

						{
							"number": float(data[310]),
							"year": "2016",
							"desc":"monash-university-city-campus-distance"
						},

						{
							"number": float(data[311]),
							"year": "2016",
							"desc":"monash-university-clayton-campus-distance"
						},

						{
							"number": float(data[312]),
							"year": "2016",
							"desc":"monash-university-gippsland-campus-distance"
						},

						{
							"number": float(data[313]),
							"year": "2016",
							"desc":"monash-university-parkville-campus-(manning-building)-distance"
						},

						{
							"number": float(data[314]),
							"year": "2016",
							"desc":"monash-university-english-language-centre-monash-college-city-campus-distance"
						},

						{
							"number": float(data[315]),
							"year": "2016",
							"desc":"moorabbin-flying-services-distance"
						},

						{
							"number": float(data[316]),
							"year": "2016",
							"desc":"national-theatre-(drama--ballet-school)-distance"
						},

						{
							"number": float(data[317]),
							"year": "2016",
							"desc":"navitas-college-of-public-safety-(ncps)-distance"
						},

						{
							"number": float(data[318]),
							"year": "2016",
							"desc":"north-melbourne-college-distance"
						},

						{
							"number": float(data[319]),
							"year": "2016",
							"desc":"nova-institute-of-technology-distance"
						},

						{
							"number": float(data[320]),
							"year": "2016",
							"desc":"oceania-polytechnic-institute-of-education-(opie)-distance"
						},

						{
							"number": float(data[321]),
							"year": "2016",
							"desc":"orange-international-college-distance"
						},

						{
							"number": float(data[322]),
							"year": "2016",
							"desc":"ozford-college-distance"
						},

						{
							"number": float(data[323]),
							"year": "2016",
							"desc":"ozford-college-of-busines-distance"
						},

						{
							"number": float(data[324]),
							"year": "2016",
							"desc":"ozford-college-of-business-distance"
						},

						{
							"number": float(data[325]),
							"year": "2016",
							"desc":"pax-institute-of-education-distance"
						},

						{
							"number": float(data[326]),
							"year": "2016",
							"desc":"pearson-aviation-essendon-airport-distance"
						},

						{
							"number": float(data[327]),
							"year": "2016",
							"desc":"photography-studies-college-(psc)-melbourne-campus-distance"
						},

						{
							"number": float(data[328]),
							"year": "2016",
							"desc":"pilgrim-theological-college-distance"
						},

						{
							"number": float(data[329]),
							"year": "2016",
							"desc":"planetshakers-college-distance"
						},

						{
							"number": float(data[330]),
							"year": "2016",
							"desc":"presbyterian-theological-college-box-hill-campus-distance"
						},

						{
							"number": float(data[331]),
							"year": "2016",
							"desc":"rabbinical-college-of-australia-and-n-z-distance"
						},

						{
							"number": float(data[332]),
							"year": "2016",
							"desc":"rc-(rhodes-college)-distance"
						},

						{
							"number": float(data[333]),
							"year": "2016",
							"desc":"reformed-theological-college-geelong-campus-distance"
						},

						{
							"number": float(data[334]),
							"year": "2016",
							"desc":"ridley-college-parkville-campus-distance"
						},

						{
							"number": float(data[335]),
							"year": "2016",
							"desc":"rmit-english-worldwide-distance"
						},

						{
							"number": float(data[336]),
							"year": "2016",
							"desc":"rmit-univeristy-brunswick-campus-distance"
						},

						{
							"number": float(data[337]),
							"year": "2016",
							"desc":"rmit-university-(rmit)-city-campus-distance"
						},

						{
							"number": float(data[338]),
							"year": "2016",
							"desc":"rmit-university-bundoora-campus-distance"
						},

						{
							"number": float(data[339]),
							"year": "2016",
							"desc":"rmit-university-point-cook-campus-distance"
						},

						{
							"number": float(data[340]),
							"year": "2016",
							"desc":"royal-gurkhas-institute-of-technology-(rgit)-australia-gurkhas-institute-of-hospitality--management-distance"
						},

						{
							"number": float(data[341]),
							"year": "2016",
							"desc":"royal-gurkhas-institute-of-technology-australia-(rgit)-distance"
						},

						{
							"number": float(data[342]),
							"year": "2016",
							"desc":"royal-victorian-aero-club-distance"
						},

						{
							"number": float(data[343]),
							"year": "2016",
							"desc":"sae-institute-qantm-college-melbourne-campus-distance"
						},

						{
							"number": float(data[344]),
							"year": "2016",
							"desc":"school-for-f-m-alexander-studies-distance"
						},

						{
							"number": float(data[345]),
							"year": "2016",
							"desc":"south-australian-college-of-english-(sace)-melbourne-college-of-english-distance"
						},

						{
							"number": float(data[346]),
							"year": "2016",
							"desc":"south-pacific-institute-(spi)-melbourne-campus-distance"
						},

						{
							"number": float(data[347]),
							"year": "2016",
							"desc":"southern-cross-education-institute-(scei)-second-campus-distance"
						},

						{
							"number": float(data[348]),
							"year": "2016",
							"desc":"southern-cross-education-institute-(scei)-third-campus-distance"
						},

						{
							"number": float(data[349]),
							"year": "2016",
							"desc":"southern-school-of-natural-therapies-distance"
						},

						{
							"number": float(data[350]),
							"year": "2016",
							"desc":"st-peters-institute-distance"
						},

						{
							"number": float(data[351]),
							"year": "2016",
							"desc":"st-aerospace-academy-(australia)-pty-ltd-2-bowral-court-mitchell-park-distance"
						},

						{
							"number": float(data[352]),
							"year": "2016",
							"desc":"st-peter-institute-bourke-street-campus-distance"
						},

						{
							"number": float(data[353]),
							"year": "2016",
							"desc":"st-peter-institute-little-collins-campus-distance"
						},

						{
							"number": float(data[354]),
							"year": "2016",
							"desc":"stott's-colleges-(front-cooking-school--carlton-campus)--vet-distance"
						},

						{
							"number": float(data[355]),
							"year": "2016",
							"desc":"stott's-colleges-box-hill-campus-distance"
						},

						{
							"number": float(data[356]),
							"year": "2016",
							"desc":"stott's-colleges-melbourne-campus-distance"
						},

						{
							"number": float(data[357]),
							"year": "2016",
							"desc":"strathfield-college-melbourne-campus-distance"
						},

						{
							"number": float(data[358]),
							"year": "2016",
							"desc":"sunraysia-institute-of-tafe-mildura-campus-distance"
						},

						{
							"number": float(data[359]),
							"year": "2016",
							"desc":"sunshine-college-of-management-distance"
						},

						{
							"number": float(data[360]),
							"year": "2016",
							"desc":"swinburne-university-of-technology-hawthorn-campus-distance"
						},

						{
							"number": float(data[361]),
							"year": "2016",
							"desc":"swinburne-university-of-technology-prahan-campus-distance"
						},

						{
							"number": float(data[362]),
							"year": "2016",
							"desc":"technical-education-development-institute-distance"
						},

						{
							"number": float(data[363]),
							"year": "2016",
							"desc":"technical-institute-of-victoria-distance"
						},

						{
							"number": float(data[364]),
							"year": "2016",
							"desc":"the-academy-of-interactive-entertainment-melbourne-campus-distance"
						},

						{
							"number": float(data[365]),
							"year": "2016",
							"desc":"the-australian-ballet-school-distance"
						},

						{
							"number": float(data[366]),
							"year": "2016",
							"desc":"the-australian-conservatoire-of-ballet-melbourne-campus-distance"
						},

						{
							"number": float(data[367]),
							"year": "2016",
							"desc":"the-university-of-melbourne-distance"
						},

						{
							"number": float(data[368]),
							"year": "2016",
							"desc":"tmg-college-distance"
						},

						{
							"number": float(data[369]),
							"year": "2016",
							"desc":"torrens-university-fitzroy-campus-distance"
						},

						{
							"number": float(data[370]),
							"year": "2016",
							"desc":"torrens-university-flinders-st-campus-distance"
						},

						{
							"number": float(data[371]),
							"year": "2016",
							"desc":"trinity-college-theological-school-distance"
						},

						{
							"number": float(data[372]),
							"year": "2016",
							"desc":"turner-english-box-hill-campus-distance"
						},

						{
							"number": float(data[373]),
							"year": "2016",
							"desc":"turner-english-camberwell-campus-distance"
						},

						{
							"number": float(data[374]),
							"year": "2016",
							"desc":"turner-english-dandenong-campus-distance"
						},

						{
							"number": float(data[375]),
							"year": "2016",
							"desc":"turner-english-melbourne-cbd-campus-distance"
						},

						{
							"number": float(data[376]),
							"year": "2016",
							"desc":"univeristy-of-divinity-whitley-college-distance"
						},

						{
							"number": float(data[377]),
							"year": "2016",
							"desc":"universal-institute-of-technology-distance"
						},

						{
							"number": float(data[378]),
							"year": "2016",
							"desc":"university-of-canberra-uc-melbourne--chadstone-campus-distance"
						},

						{
							"number": float(data[379]),
							"year": "2016",
							"desc":"university-of-divinity-stirling-college-distance"
						},

						{
							"number": float(data[380]),
							"year": "2016",
							"desc":"university-of-divinity-yarra-theological-union-distance"
						},

						{
							"number": float(data[381]),
							"year": "2016",
							"desc":"victoria-university-city-flinders-distance"
						},

						{
							"number": float(data[382]),
							"year": "2016",
							"desc":"victoria-university-city-queen-distance"
						},

						{
							"number": float(data[383]),
							"year": "2016",
							"desc":"victoria-university-footscray-nicholson-distance"
						},

						{
							"number": float(data[384]),
							"year": "2016",
							"desc":"victoria-university-footscray-park-distance"
						},

						{
							"number": float(data[385]),
							"year": "2016",
							"desc":"victoria-university-melbourne-campus-distance"
						},

						{
							"number": float(data[386]),
							"year": "2016",
							"desc":"victoria-university-st-albans-distance"
						},

						{
							"number": float(data[387]),
							"year": "2016",
							"desc":"victoria-university-sunshine-distance"
						},

						{
							"number": float(data[388]),
							"year": "2016",
							"desc":"victoria-university-werribee-distance"
						},

						{
							"number": float(data[389]),
							"year": "2016",
							"desc":"victorian-academy-of-commerce-and-technology-startups-(vacts)-distance"
						},

						{
							"number": float(data[390]),
							"year": "2016",
							"desc":"victorian-institute-of-culinary-arts--technology-main-campus--spotswood-distance"
						},

						{
							"number": float(data[391]),
							"year": "2016",
							"desc":"victorian-institute-of-culinary-arts--technology-regional-campus-1--kerang-scoresby-st-distance"
						},

						{
							"number": float(data[392]),
							"year": "2016",
							"desc":"victorian-institute-of-culinary-arts--technology-regional-campus-2--kerang-wellington-st-distance"
						},

						{
							"number": float(data[393]),
							"year": "2016",
							"desc":"victorian-institute-of-culinary-arts--technology-regional-campus-3--shepparton-distance"
						},

						{
							"number": float(data[394]),
							"year": "2016",
							"desc":"vit-(victorian-institute-of-technology)-abbotsford-campus-distance"
						},

						{
							"number": float(data[395]),
							"year": "2016",
							"desc":"vit-(victorian-institute-of-technology)-melbourne-cbd-campus-distance"
						},

						{
							"number": float(data[396]),
							"year": "2016",
							"desc":"whitehouse-institute-of-design-australia-distance"
						},

						{
							"number": float(data[397]),
							"year": "2016",
							"desc":"william-angliss-institute-distance"
						},

						{
							"number": float(data[398]),
							"year": "2016",
							"desc":"yorke-institute-distance"
						},

						{
							"number": int(data[628]),
							"year": "2016",
							"desc":"number-of-medical-workers"
						},

						{
							"number": int(data[629]),
							"year": "2016",
							"desc":"total-med-staff-per-suburb"
						},

						{
							"number": int(data[630]),
							"year": "2016",
							"desc":"suburb-med-staff-presence-by-type-rank"
						},

						{
							"number": int(data[631]),
							"year": "2016",
							"desc":"pop-per-doc"
						},

						{
							"number": int(data[632]),
							"year": "2016",
							"desc":"pop-per-doc-type"
						},

						{
							"number": int(data[633]),
							"year": "2016",
							"desc":"total-vic-med-staff"
						},

						{
							"number": int(data[634]),
							"year": "2016",
							"desc":"real-suburb-med-staff-presence-rank"
						},

						{
							"number": int(data[635]),
							"year": "2016",
							"desc":"suburb-adjusted-med-staff-presence-rank"
						},

						{
							"number": int(data[636]),
							"year": "2016",
							"desc":"suburb-adjusted-med-staff-by-type-presence-rank"
						},

						{
							"number": int(data[637]),
							"year": "2016",
							"desc":"population-adjusted-med-staff-rating"
						},

						{
							"number": (data[638]),
							"year": "2016",
							"desc":"suburb-med-fac-flag"
						},

						{
							"number": (data[639]),
							"year": "2016",
							"desc":"suburb-pathology-and-diagnostic-imaging-services-fac-flag"
						},

						{
							"number": (data[640]),
							"year": "2016",
							"desc":"suburb-chiropractic-and-osteopathic-services-fac-flag"
						},

						{
							"number": (data[641]),
							"year": "2016",
							"desc":"suburb-hospitals-except-psychiatric-hospitals-fac-flag"
						},

						{
							"number": (data[642]),
							"year": "2016",
							"desc":"suburb-aged-care-residential-services-fac-flag"
						},

						{
							"number": (data[643]),
							"year": "2016",
							"desc":"suburb-other-allied-health-services-fac-flag"
						},

						{
							"number": (data[644]),
							"year": "2016",
							"desc":"suburb-general-practice-medical-services-fac-flag"
						},

						{
							"number": (data[645]),
							"year": "2016",
							"desc":"suburb-physiotherapy-services-fac-flag"
						},

						{
							"number": (data[646]),
							"year": "2016",
							"desc":"suburb-specialist-medical-services-fac-flag"
						},

						{
							"number": (data[647]),
							"year": "2016",
							"desc":"suburb-dental-services-fac-flag"
						},

						{
							"number": (data[648]),
							"year": "2016",
							"desc":"suburb-optometry-optical-dispensing-services-fac-flag"
						},

						{
							"number": (data[649]),
							"year": "2016",
							"desc":"suburb-other-health-care-services-fac-flag"
						},

						{
							"number": (data[650]),
							"year": "2016",
							"desc":"suburb-ambulance-services-fac-flag"
						},

						{
							"number": (data[651]),
							"year": "2016",
							"desc":"suburb-residential-care-services-fac-flag"
						},

						{
							"number": (data[652]),
							"year": "2016",
							"desc":"suburb-allied-health-services-fac-flag"
						},

						{
							"number": (data[653]),
							"year": "2016",
							"desc":"suburb-psychiatric-hospitals-fac-flag"
						},

						{
							"number": (data[654]),
							"year": "2016",
							"desc":"suburb-hospital-fac-flag"
						},

						{
							"number": (data[655]),
							"year": "2016",
							"desc":"suburb-medical-services-fac-flag"
						},

						{
							"number": (data[656]),
							"year": "2016",
							"desc":"suburb-other-residential-care-services-fac-flag"
						},

						{
							"number": (data[657]),
							"year": "2016",
							"desc":"suburb-medical-and-other-health-care-services-fac-flag"
						},

						{
							"number": int(data[658]),
							"year": "2016",
							"desc":"aged-care-residential-services"
						},

						{
							"number": int(data[659]),
							"year": "2016",
							"desc":"allied-health-services"
						},

						{
							"number": int(data[660]),
							"year": "2016",
							"desc":"ambulance-services"
						},

						{
							"number": int(data[661]),
							"year": "2016",
							"desc":"chiropractic-and-osteopathic-services"
						},

						{
							"number": int(data[662]),
							"year": "2016",
							"desc":"dental-services"
						},

						{
							"number": int(data[663]),
							"year": "2016",
							"desc":"general-practice-medical-services"
						},

						{
							"number": int(data[664]),
							"year": "2016",
							"desc":"hospitals"
						},

						{
							"number": int(data[665]),
							"year": "2016",
							"desc":"hospitals-except-psychiatric-hospitals"
						},

						{
							"number": int(data[666]),
							"year": "2016",
							"desc":"medical-and-other-health-care-services"
						},

						{
							"number": int(data[667]),
							"year": "2016",
							"desc":"medical-services"
						},

						{
							"number": int(data[668]),
							"year": "2016",
							"desc":"no-medical-facilities-in-the-area"
						},

						{
							"number": int(data[669]),
							"year": "2016",
							"desc":"optometry-and-optical-dispensing"
						},

						{
							"number": int(data[670]),
							"year": "2016",
							"desc":"other-allied-health-services"
						},

						{
							"number": int(data[671]),
							"year": "2016",
							"desc":"other-residential-care-services"
						},

						{
							"number": int(data[672]),
							"year": "2016",
							"desc":"pathology-and-diagnostic-imaging-services"
						},

						{
							"number": int(data[673]),
							"year": "2016",
							"desc":"physiotherapy-services"
						},

						{
							"number": int(data[674]),
							"year": "2016",
							"desc":"psychiatric-hospitals"
						},

						{
							"number": int(data[675]),
							"year": "2016",
							"desc":"residential-care-services"
						},

						{
							"number": int(data[676]),
							"year": "2016",
							"desc":"specialist-medical-services"
						},

						{
							"number": int(data[677]),
							"year": "2016",
							"desc":"number-of-police-place-of-work"
						},

						{
							"number": (data[678]),
							"year": "2016",
							"desc":"suburb-police-station-flag"
						},

						{
							"number": int(data[679]),
							"year": "2016",
							"desc":"pop-per-cop"
						},

						{
							"number": int(data[680]),
							"year": "2016",
							"desc":"total-vic-pol"
						},

						{
							"number": int(data[681]),
							"year": "2016",
							"desc":"suburb-police-presence-rank"
						},

						{
							"number": int(data[682]),
							"year": "2016",
							"desc":"suburb-adjusted-police-presence-rank"
						},

						{
							"number": int(data[683]),
							"year": "2016",
							"desc":"population-adjusted-police-rating"
						}

            ],
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
				"alfred-deakin-college-mibt-waurn-ponds-campus": int(data[406]),
				"altec-college-melbourne-campus": int(data[407]),
				"angad-australian-institute-of-technology-la-trobe-st-campus": int(data[408]),
				"angad-australian-institute-of-technology-lonsdale-st-campus": int(data[409]),
				"aoi-institute": int(data[410]),
				"ashton-college-footscray-campus": int(data[411]),
				"ashton-college-hallam-campus": int(data[412]),
				"ashton-college-hospitality-campus": int(data[413]),
				"ashton-college-northcote-campus": int(data[414]),
				"australian-academy-of-fashion-design": int(data[415]),
				"australian-careers-education-donald-street-campus-aurora-building-": int(data[416]),
				"australian-careers-education-victoria-street-campus": int(data[417]),
				"australian-catholic-univeristy-melbourne-campus": int(data[418]),
				"australian-catholic-university-ballarat-campus": int(data[419]),
				"australian-centre-of-further-education": int(data[420]),
				"australian-college-of-applied-psychology-acap--melbourne-campus": int(data[421]),
				"australian-college-of-sport-basketball-melbourne-campus": int(data[422]),
				"australian-college-of-theology": int(data[423]),
				"australian-college-of-trade-thornbury-campus": int(data[424]),
				"australian-education-academy-10-blissington-street-springvale": int(data[425]),
				"australian-institute-of-technical-training-aitt-melbourne-campus": int(data[426]),
				"australian-institute-of-trades-institute-of-hotel-management-australia": int(data[427]),
				"australian-institute-of-translation--interpretation-aiti-melbourne-campus": int(data[428]),
				"australian-it--hospitality-institute-footscray-campus": int(data[429]),
				"australian-national-airline-college": int(data[430]),
				"australian-national-college-franklin-street-campus": int(data[431]),
				"australian-national-institute-of-business--technology-anibt-melbourne-campus": int(data[432]),
				"australian-pacific-college-melbourne-campus": int(data[433]),
				"australian-study-link-institute": int(data[434]),
				"aveta-australian-vocational-education-training-academy": int(data[435]),
				"barkly-international-college-city-campus": int(data[436]),
				"barkly-international-college-north-melbourne-campus-automotive-workshop": int(data[437]),
				"barkly-international-college": int(data[438]),
				"baxter-institute-automotive-bakery-campus": int(data[439]),
				"baxter-institute-fabrication-campus": int(data[440]),
				"baxter-institute-hairdressing-and-beauty-campus-flinders-street-": int(data[441]),
				"beaconhills-college": int(data[442]),
				"bendigo-tafe-bendigo": int(data[443]),
				"bendigo-tafe-and-kangan-institute-broadmeadows-campus": int(data[444]),
				"biba-academy-swantson-street-campus": int(data[445]),
				"box-hill-institute-city-campus": int(data[446]),
				"box-hill-institute": int(data[447]),
				"brighton-institute-of-technology": int(data[448]),
				"catholic-theological-college-ctc-melbourne-college-of-divinity-east-melbourne-campus": int(data[449]),
				"central-australian-college-cac-melbourne-campus": int(data[450]),
				"central-melbourne-institute-cmi-city-campus": int(data[451]),
				"central-melbourne-institute": int(data[452]),
				"charles-sturt-university-study-centres-melbourne": int(data[453]),
				"chisholm-institue-chisholm-at-331": int(data[454]),
				"chisholm-institute-bass-coast": int(data[455]),
				"chisholm-institute-cranbourne-campus": int(data[456]),
				"chisholm-institute-dandenong-campus": int(data[457]),
				"chisholm-institute-flinders-lane-campus": int(data[458]),
				"chisholm-institute-melbourne-city-campus": int(data[459]),
				"collarts-australian-college-of-the-arts": int(data[460]),
				"dalton-college": int(data[461]),
				"dance-factory": int(data[462]),
				"deakin-college-mibt-burwood-campus": int(data[463]),
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
				"institute-of-tertiary-and-higher-education-australia-ithea-": int(data[499]),
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
				"la-trobe-university-city-campus-collins-street-city-campus-collins-street-": int(data[510]),
				"la-trobe-university-melbourne-bundoora-campus": int(data[511]),
				"la-trobe-university-mildura-campus": int(data[512]),
				"la-trobe-university-shepparton-campus": int(data[513]),
				"latrobe-college-of-art-and-design": int(data[514]),
				"lawson-college-australia": int(data[515]),
				"lonsdale-institute-eurocentres-melbourne": int(data[516]),
				"marcus-oldham-college": int(data[517]),
				"megt-institute-melbourne-campus": int(data[518]),
				"melbourne-college-of-hair-and-beauty": int(data[519]),
				"melbourne-flight-training": int(data[520]),
				"melbourne-institute-of-technology-federation-university-melbourne-campus": int(data[521]),
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
				"monash-university-parkville-campus-manning-building-": int(data[542]),
				"monash-university-english-language-centre-monash-college-city-campus": int(data[543]),
				"moorabbin-flying-services": int(data[544]),
				"national-theatre-drama--ballet-school-": int(data[545]),
				"navitas-college-of-public-safety-ncps-": int(data[546]),
				"north-melbourne-college": int(data[547]),
				"nova-institute-of-technology": int(data[548]),
				"oceania-polytechnic-institute-of-education-opie-": int(data[549]),
				"orange-international-college": int(data[550]),
				"ozford-college-of-busines": int(data[551]),
				"ozford-college-of-business": int(data[552]),
				"ozford-college": int(data[553]),
				"pax-institute-of-education": int(data[554]),
				"pearson-aviation-essendon-airport": int(data[555]),
				"photography-studies-college-psc-melbourne-campus": int(data[556]),
				"pilgrim-theological-college": int(data[557]),
				"planetshakers-college": int(data[558]),
				"presbyterian-theological-college-box-hill-campus": int(data[559]),
				"rabbinical-college-of-australia-and-n-z-": int(data[560]),
				"rc-rhodes-college-": int(data[561]),
				"reformed-theological-college-geelong-campus": int(data[562]),
				"ridley-college-parkville-campus": int(data[563]),
				"rmit-english-worldwide": int(data[564]),
				"rmit-univeristy-brunswick-campus": int(data[565]),
				"rmit-university-rmit-city-campus": int(data[566]),
				"rmit-university-bundoora-campus": int(data[567]),
				"rmit-university-point-cook-campus": int(data[568]),
				"royal-gurkhas-institute-of-technology-rgit-australia-gurkhas-institute-of-hospitality-management": int(data[569]),
				"royal-gurkhas-institute-of-technology-australia-rgit": int(data[570]),
				"royal-victorian-aero-club": int(data[571]),
				"sae-institute-qantm-college-melbourne-campus": int(data[572]),
				"school-for-f-m-alexander-studies": int(data[573]),
				"south-australian-college-of-english-sace-melbourne-college-of-english": int(data[574]),
				"south-pacific-institute-spi-melbourne-campus": int(data[575]),
				"southern-cross-education-institute-scei-second-campus": int(data[576]),
				"southern-cross-education-institute-scei-third-campus": int(data[577]),
				"southern-school-of-natural-therapies": int(data[578]),
				"st-peters-institute": int(data[579]),
				"st-aerospace-academy-australia-pty-ltd-2-bowral-court-mitchell-park": int(data[580]),
				"st-peter-institute-bourke-street-campus": int(data[581]),
				"st-peter-institute-little-collins-campus": int(data[582]),
				"stott-s-colleges-front-cooking-school-carlton-campus-vet": int(data[583]),
				"stott-s-colleges-box-hill-campus": int(data[584]),
				"stott-s-colleges-melbourne-campus": int(data[585]),
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
				"university-of-canberra-uc-melbourne-chadstone-campus": int(data[607]),
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
				"victorian-academy-of-commerce-and-technology-startups-vacts-": int(data[618]),
				"victorian-institute-of-culinary-arts-technology-main-campus-spotswood": int(data[619]),
				"victorian-institute-of-culinary-arts-technology-regional-campus-1-kerang-scoresby-st": int(data[620]),
				"victorian-institute-of-culinary-arts-technology-regional-campus-2-kerang-wellington-st": int(data[621]),
				"victorian-institute-of-culinary-arts-technology-regional-campus-3-shepparton": int(data[622]),
				"vit-victorian-institute-of-technology-abbotsford-campus": int(data[623]),
				"vit-victorian-institute-of-technology-melbourne-cbd-campus": int(data[624]),
				"whitehouse-institute-of-design-australia": int(data[625]),
				"william-angliss-institute": int(data[626]),
				"yorke-institute": int(data[627])

            }
        }


with open('ITERATION_2_TMP.csv', 'rb') as csvfile:
    readr = csv.reader(csvfile, delimiter=',')
    # readr.next()
    readr.next()
    for line in readr:
        print json.dumps(row_to_obj(line))
		#if(line[0]=="BROWN HILL"):
            #print line
            #print line[620]
#print json.dumps(row_to_obj(line))