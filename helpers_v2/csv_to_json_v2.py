import csv
import json
import random
import re

def row_to_obj(data):
    # print data
    # random.randint(1,101),
    with open('./data/geojson/' + data[0] + "_xaaaa.geojson", 'r') as json_file:
        json_data = json.loads(json_file.read())
        return {
            "name": data[0].title(),
            "shim": re.sub('[^0-9a-zA-Z]+', '-', data[0].lower()),
            "rating_safety": int(data[8]),
            "rating_affordability": int(data[25]),
            # "outlinks": {
            #     "realestate": data[28],
            #     "domain": data[27]
            # },
            "geojson": json_data,
            "coords": {
                "lat": float(data[3]),
                "lng": float(data[2])
            },
            "stats": [
                {
                    "number": data[17],
                    "year": "2016",
                    "desc": "Population"
                },
                {
                    "number": data[9],
                    "year": "2015",
                    "desc": "Offenses per 10'000 residents"
                }
            ],
            "language": {
                "acholi": int(data[39]),
                "african-languages-nec": int(data[40]),
                "african-languages-nfd": int(data[41]),
                "afrikaans": int(data[42]),
                "akan": int(data[43]),
                "albanian": int(data[44]),
                "amharic": int(data[45]),
                "anuak": int(data[46]),
                "arabic": int(data[47]),
                "armenian": int(data[48]),
                "assyrian-neo-aramaic": int(data[49]),
                "bengali": int(data[50]),
                "bisaya": int(data[51]),
                "bosnian": int(data[52]),
                "bulgarian": int(data[53]),
                "burmese": int(data[54]),
                "burmese-and-related-languages-nec": int(data[55]),
                "burmese-and-related-languages-nfd": int(data[56]),
                "cantonese": int(data[57]),
                "catalan": int(data[58]),
                "cebuano": int(data[59]),
                "chaldean-neo-aramaic": int(data[60]),
                "chin-haka": int(data[61]),
                "chinese-nfd": int(data[62]),
                "creole-nfd": int(data[63]),
                "croatian": int(data[64]),
                "czech": int(data[65]),
                "danish": int(data[66]),
                "dari": int(data[67]),
                "dhivehi": int(data[68]),
                "dinka": int(data[69]),
                "dravidian-nec": int(data[70]),
                "dutch": int(data[71]),
                "english": int(data[72]),
                "estonian": int(data[73]),
                "fijian": int(data[74]),
                "filipino": int(data[75]),
                "finnish": int(data[76]),
                "french": int(data[77]),
                "french-creole-nfd": int(data[78]),
                "german": int(data[79]),
                "greek": int(data[80]),
                "gujarati": int(data[81]),
                "hakka": int(data[82]),
                "harari": int(data[83]),
                "hausa": int(data[84]),
                "hazaraghi": int(data[85]),
                "hebrew": int(data[86]),
                "hindi": int(data[87]),
                "hungarian": int(data[88]),
                "iban": int(data[89]),
                "igbo": int(data[90]),
                "ilonggo-hiligaynon-": int(data[91]),
                "inadequately-described": int(data[92]),
                "indonesian": int(data[93]),
                "iranic-nfd": int(data[94]),
                "italian": int(data[95]),
                "japanese": int(data[96]),
                "kannada": int(data[97]),
                "karen": int(data[98]),
                "khmer": int(data[99]),
                "kinyarwanda-rwanda-": int(data[100]),
                "kirundi-rundi-":int(data[101]),
                "konkani": int(data[102]),
                "korean": int(data[103]),
                "kurdish": int(data[104]),
                "lao": int(data[105]),
                "lithuanian": int(data[106]),
                "loma-lorma-": int(data[107]),
                "luganda": int(data[108]),
                "macedonian": int(data[109]),
                "malay": int(data[110]),
                "malayalam": int(data[111]),
                "maltese": int(data[112]),
                "mandarin": int(data[113]),
                "maori-cook-island-": int(data[114]),
                "maori-new-zealand-": int(data[115]),
                "marathi": int(data[116]),
                "mauritian-creole": int(data[117]),
                "min-nan": int(data[118]),
                "mongolian": int(data[119]),
                "nepali": int(data[120]),
                "norwegian": int(data[121]),
                "not-stated": int(data[122]),
                "nuer": int(data[123]),
                "nyanja-chichewa-": int(data[124]),
                "oriya": int(data[125]),
                "oromo": int(data[126]),
                "other-southern-asian-languages": int(data[127]),
                "pashto": int(data[128]),
                "persian-excluding-dari-": int(data[129]),
                "pidgin-nfd": int(data[130]),
                "polish": int(data[131]),
                "portuguese": int(data[132]),
                "punjabi": int(data[133]),
                "rohingya": int(data[134]),
                "romanian": int(data[135]),
                "russian": int(data[136]),
                "samoan": int(data[137]),
                "serbian": int(data[138]),
                "shilluk": int(data[139]),
                "shona": int(data[140]),
                "sindhi": int(data[141]),
                "sinhalese": int(data[142]),
                "slovak": int(data[143]),
                "slovene": int(data[144]),
                "somali": int(data[145]),
                "southern-asian-languages-nfd": int(data[146]),
                "spanish": int(data[147]),
                "swahili": int(data[148]),
                "swedish": int(data[149]),
                "tagalog": int(data[150]),
                "tamil": int(data[151]),
                "telugu": int(data[152]),
                "tetum": int(data[153]),
                "thai": int(data[154]),
                "tibetan": int(data[155]),
                "tigrinya": int(data[156]),
                "tok-pisin-neomelanesian-": int(data[157]),
                "tongan": int(data[158]),
                "tswana": int(data[159]),
                "turkish": int(data[160]),
                "tuvaluan": int(data[161]),
                "ukrainian": int(data[162]),
                "urdu": int(data[163]),
                "vietnamese": int(data[164]),
                "wu": int(data[165]),
                "yoruba": int(data[166]),
                "zomi": int(data[167])
            },
            "universities": {
                "aapoly-ami-education": int(data[481]),
"aapoly-melbourne-campus": int(data[482]),
"academia-international-melbourne-campus": int(data[483]),
"acumen-institute-of-further-education-cbd-campus": int(data[484]),
"acumen-institute-of-further-education-richmond-campus": int(data[485]),
"agb-training-geelong-campus": int(data[486]),
"alacc-health-college-australia": int(data[487]),
"alfred-deakin-college-mibt-waurn-ponds-campus": int(data[488]),
"altec-college-melbourne-campus": int(data[489]),
"angad-australian-institute-of-technology-la-trobe-st-campus": int(data[490]),
"angad-australian-institute-of-technology-lonsdale-st-campus": int(data[491]),
"aoi-institute": int(data[492]),
"ashton-college-footscray-campus": int(data[493]),
"ashton-college-hallam-campus": int(data[494]),
"ashton-college-hospitality-campus": int(data[495]),
"ashton-college-northcote-campus": int(data[496]),
"australian-academy-of-fashion-design": int(data[497]),
"australian-careers-education-donald-street-campus-aurora-building-": int(data[498]),
"australian-careers-education-victoria-street-campus": int(data[499]),
"australian-catholic-univeristy-melbourne-campus": int(data[500]),
"australian-catholic-university-ballarat-campus": int(data[501]),
"australian-centre-of-further-education": int(data[502]),
"australian-college-of-applied-psychology-acap-melbourne-campus": int(data[503]),
"australian-college-of-sport-basketball-melbourne-campus": int(data[504]),
"australian-college-of-theology": int(data[505]),
"australian-college-of-trade-thornbury-campus": int(data[506]),
"australian-education-academy-10-blissington-street-springvale": int(data[507]),
"australian-institute-of-technical-training-aitt-melbourne-campus": int(data[508]),
"australian-institute-of-trades-institute-of-hotel-management-australia": int(data[509]),
"australian-institute-of-translation-interpretation-aiti-melbourne-campus": int(data[510]),
"australian-it-hospitality-institute-footscray-campus": int(data[511]),
"australian-national-airline-college": int(data[512]),
"australian-national-college-franklin-street-campus": int(data[513]),
"australian-national-institute-of-business-technology-anibt-melbourne-campus": int(data[514]),
"australian-pacific-college-melbourne-campus": int(data[515]),
"australian-study-link-institute": int(data[516]),
"aveta-australian-vocational-education-training-academy": int(data[517]),
"barkly-international-college-city-campus": int(data[518]),
"barkly-international-college-north-melbourne-campus-automotive-workshop": int(data[519]),
"barkly-international-college": int(data[520]),
"baxter-institute-automotive-bakery-campus": int(data[521]),
"baxter-institute-fabrication-campus": int(data[522]),
"baxter-institute-hairdressing-and-beauty-campus-flinders-street-": int(data[523]),
"beaconhills-college": int(data[524]),
"bendigo-tafe-bendigo": int(data[525]),
"bendigo-tafe-and-kangan-institute-broadmeadows-campus": int(data[526]),
"biba-academy-swantson-street-campus": int(data[527]),
"box-hill-institute-city-campus": int(data[528]),
"box-hill-institute": int(data[529]),
"brighton-institute-of-technology": int(data[530]),
"catholic-theological-college-ctc-melbourne-college-of-divinity-east-melbourne-campus": int(data[531]),
"central-australian-college-cac-melbourne-campus": int(data[532]),
"central-melbourne-institute-cmi-city-campus": int(data[533]),
"central-melbourne-institute": int(data[534]),
"charles-sturt-university-study-centres-melbourne": int(data[535]),
"chisholm-institue-chisholm-at-331": int(data[536]),
"chisholm-institute-bass-coast": int(data[537]),
"chisholm-institute-cranbourne-campus": int(data[538]),
"chisholm-institute-dandenong-campus": int(data[539]),
"chisholm-institute-flinders-lane-campus": int(data[540]),
"chisholm-institute-melbourne-city-campus": int(data[541]),
"collarts-australian-college-of-the-arts": int(data[542]),
"dalton-college": int(data[543]),
"dance-factory": int(data[544]),
"deakin-college-mibt-burwood-campus": int(data[545]),
"deakin-university-burwood-campus": int(data[546]),
"deakin-university-geelong-waterfront-campus": int(data[547]),
"deakin-university-warrnambool-campus": int(data[548]),
"deakin-university-waurn-ponds-campus": int(data[549]),
"della-international-college-city-campus": int(data[550]),
"della-international-college-sunshine-campus": int(data[551]),
"department-of-education-and-training-victoria": int(data[552]),
"east-west-college-of-natural-therapies": int(data[553]),
"education-access-australia": int(data[554]),
"education-training-employment-australia-etea": int(data[555]),
"elite-training-institute": int(data[556]),
"elly-lukas-beauty-therapy-college": int(data[557]),
"elsis-melbourne-campus": int(data[558]),
"endeavour-college-of-natural-health-melbourne-campus": int(data[559]),
"everest-institute-of-education": int(data[560]),
"explore-english": int(data[561]),
"federation-university-ballarat-campus": int(data[562]),
"flinders-international-college": int(data[563]),
"fusion-enlgish-melbourne-campus": int(data[564]),
"global-business-college-of-australia": int(data[565]),
"gordon-institute-of-tafe-east-geelong-campus": int(data[566]),
"gordon-institute-of-tafe-east-geelong-elicos-campus": int(data[567]),
"greenwich-english-college-melbourne": int(data[568]),
"harvest-bible-college": int(data[569]),
"hays-international-college": int(data[570]),
"heading-out-academy": int(data[571]),
"headmasters-advanced-academy-of-training": int(data[572]),
"holmesglen-holmesglen-institute-chadstone-campus": int(data[573]),
"holmesglen-holmesglen-institute-city-campus": int(data[574]),
"holmesglen-holmesglen-institute-waverley-campus": int(data[575]),
"holmesglen-institute-holmesglen-moorabbin-campus": int(data[576]),
"hospitality-management-institute-of-australia": int(data[577]),
"impact-english-college-melbourne-campus": int(data[578]),
"imperial-college-of-technology-and-management": int(data[579]),
"institute-of-health-and-nursing-australia": int(data[580]),
"institute-of-tertiary-and-higher-education-australia-ithea-": int(data[581]),
"inus-australia-education-and-training": int(data[582]),
"jmc-academy": int(data[583]),
"job-training-institute-dandenong-campus": int(data[584]),
"kangan-batman-institute-of-tafe-docklands": int(data[585]),
"kangan-batman-institute-of-tafe-richmond": int(data[586]),
"kangan-institute-moonee-ponds-campus": int(data[587]),
"kaplan-business-school": int(data[588]),
"la-trobe-bundoora-campus": int(data[589]),
"la-trobe-university-albury-wodonga-campus": int(data[590]),
"la-trobe-university-bendigo-campus": int(data[591]),
"la-trobe-university-city-campus-collins-street-city-campus-collins-street-": int(data[592]),
"la-trobe-university-melbourne-bundoora-campus": int(data[593]),
"la-trobe-university-mildura-campus": int(data[594]),
"la-trobe-university-shepparton-campus": int(data[595]),
"latrobe-college-of-art-and-design": int(data[596]),
"lawson-college-australia": int(data[597]),
"lonsdale-institute-eurocentres-melbourne": int(data[598]),
"marcus-oldham-college": int(data[599]),
"megt-institute-melbourne-campus": int(data[600]),
"melbourne-college-of-hair-and-beauty": int(data[601]),
"melbourne-flight-training": int(data[602]),
"melbourne-institute-of-technology-federation-university-melbourne-campus": int(data[603]),
"melbourne-polytechnic-brunswick-campus": int(data[604]),
"melbourne-polytechnic-epping-campus": int(data[605]),
"melbourne-polytechnic-fairfield-campus": int(data[606]),
"melbourne-polytechnic-heidelberg-campus": int(data[607]),
"melbourne-polytechnic-preston-campus": int(data[608]),
"melbourne-polytechnic-preston-tafe-campus": int(data[609]),
"melbourne-rudolf-steiner-seminar": int(data[610]),
"melbourne-school-of-theology": int(data[611]),
"melbourne-university-hawthorn-english-language-centre": int(data[612]),
"melbourne-university-trinity-college": int(data[613]),
"menzies-institute-of-technology-adderley-campus": int(data[614]),
"menzies-institute-of-technology-batman-campus": int(data[615]),
"menzies-institute-of-technology-spencer-campus": int(data[616]),
"monash-college-monash-university-english-language-centre": int(data[617]),
"monash-international-berwick-campus": int(data[618]),
"monash-international-peninsula-campus": int(data[619]),
"monash-university-caulfield-campus": int(data[620]),
"monash-university-city-campus": int(data[621]),
"monash-university-clayton-campus": int(data[622]),
"monash-university-gippsland-campus": int(data[623]),
"monash-university-parkville-campus-manning-building-": int(data[624]),
"monash-university-english-language-centre-monash-college-city-campus": int(data[625]),
"moorabbin-flying-services": int(data[626]),
"national-theatre-drama-ballet-school-": int(data[627]),
"navitas-college-of-public-safety-ncps-": int(data[628]),
"north-melbourne-college": int(data[629]),
"nova-institute-of-technology": int(data[630]),
"oceania-polytechnic-institute-of-education-opie-": int(data[631]),
"orange-international-college": int(data[632]),
"ozford-college-of-busines": int(data[633]),
"ozford-college-of-business": int(data[634]),
"ozford-college": int(data[635]),
"pax-institute-of-education": int(data[636]),
"pearson-aviation-essendon-airport": int(data[637]),
"photography-studies-college-psc-melbourne-campus": int(data[638]),
"pilgrim-theological-college": int(data[639]),
"planetshakers-college": int(data[640]),
"presbyterian-theological-college-box-hill-campus": int(data[641]),
"rabbinical-college-of-australia-and-n-z-": int(data[642]),
"rc-rhodes-college-": int(data[643]),
"reformed-theological-college-geelong-campus": int(data[644]),
"ridley-college-parkville-campus": int(data[645]),
"rmit-english-worldwide": int(data[646]),
"rmit-univeristy-brunswick-campus": int(data[647]),
"rmit-university-rmit-city-campus": int(data[648]),
"rmit-university-bundoora-campus": int(data[649]),
"rmit-university-point-cook-campus": int(data[650]),
"royal-gurkhas-institute-of-technology-rgit-australia-gurkhas-institute-of-hospitality-management": int(data[651]),
"royal-gurkhas-institute-of-technology-australia-rgit-": int(data[652]),
"royal-victorian-aero-club": int(data[653]),
"sae-institute-qantm-college-melbourne-campus": int(data[654]),
"school-for-f-m-alexander-studies": int(data[655]),
"south-australian-college-of-english-sace-melbourne-college-of-english": int(data[656]),
"south-pacific-institute-spi-melbourne-campus": int(data[657]),
"southern-cross-education-institute-scei-second-campus": int(data[658]),
"southern-cross-education-institute-scei-third-campus": int(data[659]),
"southern-school-of-natural-therapies": int(data[660]),
"st-peters-institute": int(data[661]),
"st-aerospace-academy-australia-pty-ltd-2-bowral-court-mitchell-park": int(data[662]),
"st-peter-institute-bourke-street-campus": int(data[663]),
"st-peter-institute-little-collins-campus": int(data[664]),
"stott-s-colleges-front-cooking-school-carlton-campus-vet": int(data[665]),
"stott-s-colleges-box-hill-campus": int(data[666]),
"stott-s-colleges-melbourne-campus": int(data[667]),
"strathfield-college-melbourne-campus": int(data[668]),
"sunraysia-institute-of-tafe-mildura-campus": int(data[669]),
"sunshine-college-of-management": int(data[670]),
"swinburne-university-of-technology-hawthorn-campus": int(data[671]),
"swinburne-university-of-technology-prahan-campus": int(data[672]),
"technical-education-development-institute": int(data[673]),
"technical-institute-of-victoria": int(data[674]),
"the-academy-of-interactive-entertainment-melbourne-campus": int(data[675]),
"the-academy-of-interactive-entertainment": int(data[676]),
"the-australian-ballet-school": int(data[677]),
"the-australian-conservatoire-of-ballet-melbourne-campus": int(data[678]),
"the-university-of-melbourne": int(data[679]),
"tmg-college": int(data[680]),
"torrens-university-fitzroy-campus": int(data[681]),
"torrens-university-flinders-st-campus": int(data[682]),
"trinity-college-theological-school": int(data[683]),
"turner-english-box-hill-campus": int(data[684]),
"turner-english-camberwell-campus": int(data[685]),
"turner-english-dandenong-campus": int(data[686]),
"turner-english-melbourne-cbd-campus": int(data[687]),
"univeristy-of-divinity-whitley-college": int(data[688]),
"universal-institute-of-technology": int(data[689]),
"university-of-canberra-uc-melbourne-chadstone-campus": int(data[690]),
"university-of-divinity-stirling-college": int(data[691]),
"university-of-divinity-yarra-theological-union": int(data[692]),
"victoria-university-city-flinders": int(data[693]),
"victoria-university-city-queen": int(data[694]),
"victoria-university-footscray-nicholson": int(data[695]),
"victoria-university-footscray-park": int(data[696]),
"victoria-university-melbourne-campus": int(data[697]),
"victoria-university-st-albans": int(data[698]),
"victoria-university-sunshine": int(data[699]),
"victoria-university-werribee": int(data[700]),
"victorian-academy-of-commerce-and-technology-startups-vacts-": int(data[701]),
"victorian-institute-of-culinary-arts-technology-main-campus-spotswood": int(data[702]),
"victorian-institute-of-culinary-arts-technology-regional-campus-1-kerang-scoresby-st": int(data[703]),
"victorian-institute-of-culinary-arts-technology-regional-campus-2-kerang-wellington-st": int(data[704]),
"victorian-institute-of-culinary-arts-technology-regional-campus-3-shepparton": int(data[705]),
"vit-victorian-institute-of-technology-abbotsford-campus": int(data[706]),
"vit-victorian-institute-of-technology-melbourne-cbd-campus": int(data[707]),
"whitehouse-institute-of-design-australia": int(data[708]),
"william-angliss-institute": int(data[709]),
"yorke-institute": int(data[710])
            }
        }


with open('it2.csv', 'rb') as csvfile:
    readr = csv.reader(csvfile, delimiter=',')
    # readr.next()
    readr.next()
    for line in readr:
        if(line[0]=="BROWN HILL"):
            print line
            print line[620]
        #print json.dumps(row_to_obj(line))