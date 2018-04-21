import csv
import json
import random
import re

def row_to_obj(data):
    # print data
    # random.randint(1,101),
    with open('./data/geojson/' + data[2] + "_xaaaa.geojson", 'r') as json_file:
        json_data = json.loads(json_file.read())
        return {
            "name": data[2].title(),
            "shim": re.sub('[^0-9a-zA-Z]+', '-', data[2].lower()),
            "rating_safety": int(data[17]),
            "rating_affordability": int(data[12]),
            "outlinks": {
                "realestate": data[8],
                "domain": data[7]
            },
            "geojson": json_data,
            "coords": {
                "lat": float(data[5]),
                "lng": float(data[4])
            },
            "stats": [
                {
                    "number": random.randint(100,40000),
                    "year": "2016",
                    "desc": "Population"
                },
                {
                    "number": random.randint(100,40000),
                    "year": "2015",
                    "desc": "Crime per 10000 residents"
                }
            ],
            "language": {
                "acholi": random.randint(1,100),
                "african-languages-nec": random.randint(1,100),
                "african-languages-nfd": random.randint(1,100),
                "afrikaans": random.randint(1,100),
                "akan": random.randint(1,100),
                "albanian": random.randint(1,100),
                "amharic": random.randint(1,100),
                "anuak": random.randint(1,100),
                "arabic": random.randint(1,100),
                "armenian": random.randint(1,100),
                "assyrian-neo-aramaic": random.randint(1,100),
                "bengali": random.randint(1,100),
                "bisaya": random.randint(1,100),
                "bosnian": random.randint(1,100),
                "bulgarian": random.randint(1,100),
                "burmese": random.randint(1,100),
                "burmese-and-related-languages-nec": random.randint(1,100),
                "burmese-and-related-languages-nfd": random.randint(1,100),
                "cantonese": random.randint(1,100),
                "catalan": random.randint(1,100),
                "cebuano": random.randint(1,100),
                "chaldean-neo-aramaic": random.randint(1,100),
                "chin-haka": random.randint(1,100),
                "chinese-nfd": random.randint(1,100),
                "creole-nfd": random.randint(1,100),
                "croatian": random.randint(1,100),
                "czech": random.randint(1,100),
                "danish": random.randint(1,100),
                "dari": random.randint(1,100),
                "dhivehi": random.randint(1,100),
                "dinka": random.randint(1,100),
                "dravidian-nec": random.randint(1,100),
                "dutch": random.randint(1,100),
                "english": random.randint(1,100),
                "estonian": random.randint(1,100),
                "fijian": random.randint(1,100),
                "filipino": random.randint(1,100),
                "finnish": random.randint(1,100),
                "french": random.randint(1,100),
                "french-creole-nfd": random.randint(1,100),
                "german": random.randint(1,100),
                "greek": random.randint(1,100),
                "gujarati": random.randint(1,100),
                "hakka": random.randint(1,100),
                "harari": random.randint(1,100),
                "hausa": random.randint(1,100),
                "hazaraghi": random.randint(1,100),
                "hebrew": random.randint(1,100),
                "hindi": random.randint(1,100),
                "hungarian": random.randint(1,100),
                "iban": random.randint(1,100),
                "igbo": random.randint(1,100),
                "ilonggo-hiligaynon-": random.randint(1,100),
                "inadequately-described": random.randint(1,100),
                "indonesian": random.randint(1,100),
                "iranic-nfd": random.randint(1,100),
                "italian": random.randint(1,100),
                "japanese": random.randint(1,100),
                "kannada": random.randint(1,100),
                "karen": random.randint(1,100),
                "khmer": random.randint(1,100),
                "kinyarwanda-rwanda-": random.randint(1,100),
                "kirundi-rundi-": random.randint(1,100),
                "konkani": random.randint(1,100),
                "korean": random.randint(1,100),
                "kurdish": random.randint(1,100),
                "lao": random.randint(1,100),
                "lithuanian": random.randint(1,100),
                "loma-lorma-": random.randint(1,100),
                "luganda": random.randint(1,100),
                "macedonian": random.randint(1,100),
                "malay": random.randint(1,100),
                "malayalam": random.randint(1,100),
                "maltese": random.randint(1,100),
                "mandarin": random.randint(1,100),
                "maori-cook-island-": random.randint(1,100),
                "maori-new-zealand-": random.randint(1,100),
                "marathi": random.randint(1,100),
                "mauritian-creole": random.randint(1,100),
                "min-nan": random.randint(1,100),
                "mongolian": random.randint(1,100),
                "nepali": random.randint(1,100),
                "no-international-students-recorded-as-living-in-this-area-": random.randint(1,100),
                "norwegian": random.randint(1,100),
                "not-stated": random.randint(1,100),
                "nuer": random.randint(1,100),
                "nyanja-chichewa-": random.randint(1,100),
                "oriya": random.randint(1,100),
                "oromo": random.randint(1,100),
                "other-southern-asian-languages": random.randint(1,100),
                "pashto": random.randint(1,100),
                "persian-excluding-dari-": random.randint(1,100),
                "pidgin-nfd": random.randint(1,100),
                "polish": random.randint(1,100),
                "portuguese": random.randint(1,100),
                "punjabi": random.randint(1,100),
                "rohingya": random.randint(1,100),
                "romanian": random.randint(1,100),
                "russian": random.randint(1,100),
                "samoan": random.randint(1,100),
                "serbian": random.randint(1,100),
                "shilluk": random.randint(1,100),
                "shona": random.randint(1,100),
                "sindhi": random.randint(1,100),
                "sinhalese": random.randint(1,100),
                "slovak": random.randint(1,100),
                "slovene": random.randint(1,100),
                "somali": random.randint(1,100),
                "southern-asian-languages-nfd": random.randint(1,100),
                "spanish": random.randint(1,100),
                "swahili": random.randint(1,100),
                "swedish": random.randint(1,100),
                "tagalog": random.randint(1,100),
                "tamil": random.randint(1,100),
                "telugu": random.randint(1,100),
                "tetum": random.randint(1,100),
                "thai": random.randint(1,100),
                "tibetan": random.randint(1,100),
                "tigrinya": random.randint(1,100),
                "tok-pisin-neomelanesian-": random.randint(1,100),
                "tongan": random.randint(1,100),
                "tswana": random.randint(1,100),
                "turkish": random.randint(1,100),
                "tuvaluan": random.randint(1,100),
                "ukrainian": random.randint(1,100),
                "urdu": random.randint(1,100),
                "vietnamese": random.randint(1,100),
                "wu": random.randint(1,100),
                "yoruba": random.randint(1,100),
                "zomi": random.randint(1,100)
            },
            "universities": {
                "box-hill-institute": random.randint(1,100),
                "harvest-bible-college": random.randint(1,100),
                "australian-study-link-institute": random.randint(1,100),
                "the-australian-ballet-school": random.randint(1,100),
                "royal-victorian-aero-club": random.randint(1,100),
                "st-aerospace-academy-australia-pty-ltd-2-bowral-court-mitchell-park": random.randint(1,100),
                "the-academy-of-interactive-entertainment-melbourne-campus": random.randint(1,100),
                "bendigo-tafe-and-kangan-institute-broadmeadows-campus": random.randint(1,100),
                "la-trobe-bundoora-campus": random.randint(1,100),
                "the-academy-of-interactive-entertainment": random.randint(1,100),
                "rabbinical-college-of-australia-and-n-z-": random.randint(1,100),
                "gordon-institute-of-tafe-east-geelong-campus": random.randint(1,100),
                "technical-institute-of-victoria": random.randint(1,100),
                "agb-training-geelong-campus": random.randint(1,100),
                "dance-factory": random.randint(1,100),
                "nova-institute-of-technology": random.randint(1,100),
                "flinders-international-college": random.randint(1,100),
                "elite-training-institute": random.randint(1,100),
                "sunraysia-institute-of-tafe-mildura-campus": random.randint(1,100),
                "federation-university-ballarat-campus": random.randint(1,100),
                "university-of-canberra-uc-melbourne-chadstone-campus": random.randint(1,100),
                "rc-rhodes-college-": random.randint(1,100),
                "marcus-oldham-college": random.randint(1,100),
                "education-training-employment-australia-etea": random.randint(1,100),
                "monash-university-gippsland-campus": random.randint(1,100),
                "gordon-institute-of-tafe-east-geelong-elicos-campus": random.randint(1,100),
                "latrobe-college-of-art-and-design": random.randint(1,100),
                "victorian-academy-of-commerce-and-technology-startups-vacts-": random.randint(1,100),
                "south-australian-college-of-english-sace-melbourne-college-of-english": random.randint(1,100),
                "pax-institute-of-education": random.randint(1,100),
                "alacc-health-college-australia": random.randint(1,100),
                "central-melbourne-institute": random.randint(1,100),
                "dalton-college": random.randint(1,100),
                "australian-catholic-university-ballarat-campus": random.randint(1,100),
                "megt-institute-melbourne-campus": random.randint(1,100),
                "australian-institute-of-technical-training-aitt-melbourne-campus": random.randint(1,100),
                "australian-centre-of-further-education": random.randint(1,100),
                "explore-english": random.randint(1,100),
                "australian-national-airline-college": random.randint(1,100),
                "fusion-enlgish-melbourne-campus": random.randint(1,100),
                "australian-catholic-univeristy-melbourne-campus": random.randint(1,100),
                "holmesglen-holmesglen-institute-chadstone-campus": random.randint(1,100),
                "department-of-education-and-training-victoria": random.randint(1,100),
                "navitas-college-of-public-safety-ncps-": random.randint(1,100),
                "job-training-institute-dandenong-campus": random.randint(1,100),
                "monash-university-city-campus": random.randint(1,100),
                "australian-careers-education-victoria-street-campus": random.randint(1,100),
                "melbourne-polytechnic-brunswick-campus": random.randint(1,100),
                "hospitality-management-institute-of-australia": random.randint(1,100),
                "angad-australian-institute-of-technology-la-trobe-st-campus": random.randint(1,100),
                "barkly-international-college": random.randint(1,100),
                "lonsdale-institute-eurocentres-melbourne": random.randint(1,100),
                "global-business-college-of-australia-": random.randint(1,100),
                "holmesglen-holmesglen-institute-city-campus": random.randint(1,100),
                "melbourne-rudolf-steiner-seminar": random.randint(1,100),
                "institute-of-health-and-nursing-australia": random.randint(1,100),
                "rmit-english-worldwide": random.randint(1,100),
                "everest-institute-of-education": random.randint(1,100),
                "australian-education-academy-10-blissington-street-springvale": random.randint(1,100),
                "william-angliss-institute": random.randint(1,100),
                "aapoly-ami-education": random.randint(1,100),
                "st-peters-institute": random.randint(1,100),
                "greenwich-english-college-melbourne": random.randint(1,100),
                "della-international-college-city-campus": random.randint(1,100),
                "orange-international-college": random.randint(1,100),
                "holmesglen-holmesglen-institute-waverley-campus": random.randint(1,100),
                "the-university-of-melbourne": random.randint(1,100),
                "baxter-institute-fabrication-campus": random.randint(1,100),
                "academia-international-melbourne-campus": random.randint(1,100),
                "aapoly-melbourne-campus": random.randint(1,100),
                "aoi-institute": random.randint(1,100),
                "australian-academy-of-fashion-design": random.randint(1,100),
                "australian-careers-education-donald-street-campus-aurora-building-": random.randint(1,100),
                "australian-college-of-applied-psychology-acap-melbourne-campus": random.randint(1,100),
                "australian-college-of-sport-basketball-melbourne-campus": random.randint(1,100),
                "australian-college-of-sport-basketball-melbourne-campus": random.randint(1,100),
                "australian-college-of-trade-thornbury-campus": random.randint(1,100),
                "australian-institute-of-translation-interpretation-aiti-melbourne-campus": random.randint(1,100),
                "australian-institute-of-technical-training-aitt-melbourne-campus": random.randint(1,100),
                "australian-it-hospitality-institute-footscray-campus": random.randint(1,100),
                "altec-college-melbourne-campus": random.randint(1,100),
                "australian-national-college-franklin-street-campus": random.randint(1,100),
                "australian-national-institute-of-business-technology-anibt-melbourne-campus": random.randint(1,100),
                "australian-national-institute-of-business-technology-anibt-melbourne-campus": random.randint(1,100),
                "australian-pacific-college-melbourne-campus": random.randint(1,100),
                "aveta-australian-vocational-education-training-academy": random.randint(1,100),
                "baxter-institute-hairdressing-and-beauty-campus-flinders-street-": random.randint(1,100),
                "baxter-institute-hairdressing-and-beauty-campus-flinders-street-": random.randint(1,100),
                "beaconhills-college": random.randint(1,100),
                "bendigo-tafe-bendigo": random.randint(1,100),
                "biba-academy-swantson-street-campus": random.randint(1,100),
                "brighton-institute-of-technology": random.randint(1,100),
                "central-australian-college-cac-melbourne-campus": random.randint(1,100),
                "box-hill-institute-city-campus": random.randint(1,100),
                "collarts-australian-college-of-the-arts": random.randint(1,100),
                "della-international-college-sunshine-campus": random.randint(1,100),
                "east-west-college-of-natural-therapies": random.randint(1,100),
                "education-access-australia": random.randint(1,100),
                "education-training-employment-australia-etea": random.randint(1,100),
                "elly-lukas-beauty-therapy-college": random.randint(1,100),
                "elsis-melbourne-campus": random.randint(1,100),
                "endeavour-college-of-natural-health-melbourne-campus": random.randint(1,100),
                "royal-gurkhas-institute-of-technology-australia-rgit-": random.randint(1,100),
                "melbourne-university-hawthorn-english-language-centre": random.randint(1,100),
                "hays-international-college": random.randint(1,100),
                "heading-out-academy": random.randint(1,100),
                "headmasters-advanced-academy-of-training": random.randint(1,100),
                "holmesglen-institute-holmesglen-moorabbin-campus": random.randint(1,100),
                "impact-english-college-melbourne-campus": random.randint(1,100),
                "imperial-college-of-technology-and-management": random.randint(1,100),
                "australian-institute-of-trades-institute-of-hotel-management-australia": random.randint(1,100),
                "inus-australia-education-and-training": random.randint(1,100),
                "jmc-academy": random.randint(1,100),
                "kangan-batman-institute-of-tafe-richmond": random.randint(1,100),
                "kangan-batman-institute-of-tafe-docklands": random.randint(1,100),
                "kangan-institute-moonee-ponds-campus": random.randint(1,100),
                "kaplan-business-school-": random.randint(1,100),
                "la-trobe-university-city-campus-collins-street-city-campus-collins-street-": random.randint(1,100),
                "la-trobe-university-bendigo-campus": random.randint(1,100),
                "la-trobe-university-shepparton-campus": random.randint(1,100),
                "la-trobe-university-mildura-campus": random.randint(1,100),
                "la-trobe-university-albury-wodonga-campus": random.randint(1,100),
                "la-trobe-university-melbourne-bundoora-campus": random.randint(1,100),
                "lawson-college-australia": random.randint(1,100),
                "institute-of-tertiary-and-higher-education-australia-ithea-": random.randint(1,100),
                "central-melbourne-institute-cmi-city-campus": random.randint(1,100),
                "melbourne-college-of-hair-and-beauty": random.randint(1,100),
                "melbourne-flight-training": random.randint(1,100),
                "melbourne-polytechnic-preston-campus": random.randint(1,100),
                "melbourne-school-of-theology": random.randint(1,100),
                "menzies-institute-of-technology-batman-campus": random.randint(1,100),
                "menzies-institute-of-technology-spencer-campus": random.randint(1,100),
                "menzies-institute-of-technology-adderley-campus": random.randint(1,100),
                "melbourne-institute-of-technology-federation-university-melbourne-campus": random.randint(1,100),
                "monash-university-parkville-campus-manning-building-": random.randint(1,100),
                "monash-university-english-language-centre-monash-college-city-campus": random.randint(1,100),
                "monash-college-monash-university-english-language-centre": random.randint(1,100),
                "monash-international-peninsula-campus": random.randint(1,100),
                "monash-university-clayton-campus": random.randint(1,100),
                "monash-international-berwick-campus": random.randint(1,100),
                "monash-university-caulfield-campus": random.randint(1,100),
                "moorabbin-flying-services": random.randint(1,100),
                "national-theatre-drama-ballet-school-": random.randint(1,100),
                "north-melbourne-college": random.randint(1,100),
                "melbourne-polytechnic-preston-tafe-campus": random.randint(1,100),
                "melbourne-polytechnic-heidelberg-campus": random.randint(1,100),
                "melbourne-polytechnic-epping-campus": random.randint(1,100),
                "melbourne-polytechnic-fairfield-campus": random.randint(1,100),
                "nova-institute-of-technology": random.randint(1,100),
                "oceania-polytechnic-institute-of-education-opie-": random.randint(1,100),
                "ozford-college-of-busines": random.randint(1,100),
                "ozford-college": random.randint(1,100),
                "ozford-college-of-business": random.randint(1,100),
                "pearson-aviation-essendon-airport": random.randint(1,100),
                "photography-studies-college-psc-melbourne-campus": random.randint(1,100),
                "planetshakers-college": random.randint(1,100),
                "sae-institute-qantm-college-melbourne-campus": random.randint(1,100),
                "royal-gurkhas-institute-of-technology-rgit-australia-gurkhas-institute-of-hospitality-management": random.randint(1,100),
                "school-for-f-m-alexander-studies": random.randint(1,100),
                "baxter-institute-automotive-bakery-campus": random.randint(1,100),
                "south-pacific-institute-spi-melbourne-campus": random.randint(1,100),
                "southern-school-of-natural-therapies": random.randint(1,100),
                "technical-institute-of-victoria": random.randint(1,100),
                "strathfield-college-melbourne-campus": random.randint(1,100),
                "charles-sturt-university-study-centres-melbourne": random.randint(1,100),
                "sunshine-college-of-management": random.randint(1,100),
                "swinburne-university-of-technology-prahan-campus": random.randint(1,100),
                "swinburne-university-of-technology-hawthorn-campus": random.randint(1,100),
                "tafe-nsw-riverina-institute": random.randint(1,100),
                "the-australian-conservatoire-of-ballet-melbourne-campus": random.randint(1,100),
                "tmg-college": random.randint(1,100),
                "melbourne-university-trinity-college": random.randint(1,100),
                "technical-education-development-institute": random.randint(1,100),
                "universal-institute-of-technology": random.randint(1,100),
                "victoria-university-footscray-park": random.randint(1,100),
                "victoria-university-st-albans": random.randint(1,100),
                "victoria-university-melbourne-campus": random.randint(1,100),
                "victoria-university-werribee": random.randint(1,100),
                "victoria-university-sunshine": random.randint(1,100),
                "victoria-university-city-queen": random.randint(1,100),
                "victoria-university-footscray-nicholson": random.randint(1,100),
                "victoria-university-city-flinders": random.randint(1,100),
                "whitehouse-institute-of-design-australia": random.randint(1,100),
                "yorke-institute": random.randint(1,100),
                "chisholm-institute-dandenong-campus": random.randint(1,100),
                "chisholm-institute-flinders-lane-campus": random.randint(1,100),
                "chisholm-institute-cranbourne-campus": random.randint(1,100),
                "chisholm-institue-chisholm-at-331": random.randint(1,100),
                "chisholm-institute-melbourne-city-campus": random.randint(1,100),
                "chisholm-institute-bass-coast": random.randint(1,100),
                "australian-college-of-theology": random.randint(1,100),
                "presbyterian-theological-college-box-hill-campus": random.randint(1,100),
                "reformed-theological-college-geelong-campus": random.randint(1,100),
                "ridley-college-parkville-campus": random.randint(1,100),
                "pilgrim-theological-college": random.randint(1,100),
                "trinity-college-theological-school": random.randint(1,100),
                "catholic-theological-college-ctc-melbourne-college-of-divinity-east-melbourne-campus": random.randint(1,100),
                "university-of-divinity-yarra-theological-union": random.randint(1,100),
                "univeristy-of-divinity-whitley-college": random.randint(1,100),
                "university-of-divinity-stirling-college": random.randint(1,100),
                "southern-cross-education-institute-scei-melbourne-main-campus": random.randint(1,100),
                "southern-cross-education-institute-scei-second-campus": random.randint(1,100),
                "southern-cross-education-institute-scei-third-campus": random.randint(1,100),
                "st-peter-institute-bourke-street-campus": random.randint(1,100),
                "st-peter-institute-little-collins-campus": random.randint(1,100),
                "turner-english-camberwell-campus": random.randint(1,100),
                "turner-english-melbourne-cbd-campus": random.randint(1,100),
                "turner-english-box-hill-campus": random.randint(1,100),
                "turner-english-dandenong-campus": random.randint(1,100),
                "victorian-institute-of-culinary-arts-technology-regional-campus-2-kerang-wellington-st": random.randint(1,100),
                "victorian-institute-of-culinary-arts-technology-regional-campus-1-kerang-scoresby-st": random.randint(1,100),
                "victorian-institute-of-culinary-arts-technology-main-campus-spotswood": random.randint(1,100),
                "victorian-institute-of-culinary-arts-technology-regional-campus-3-shepparton": random.randint(1,100),
                "vit-victorian-institute-of-technology-melbourne-cbd-campus": random.randint(1,100),
                "vit-victorian-institute-of-technology-abbotsford-campus": random.randint(1,100),
                "ashton-college-footscray-campus": random.randint(1,100),
                "ashton-college-hospitality-campus": random.randint(1,100),
                "ashton-college-hallam-campus": random.randint(1,100),
                "ashton-college-northcote-campus": random.randint(1,100),
                "acumen-institute-of-further-education-cbd-campus": random.randint(1,100),
                "acumen-institute-of-further-education-richmond-campus": random.randint(1,100),
                "stott-s-colleges-front-cooking-school-carlton-campus-vet": random.randint(1,100),
                "stott-s-colleges-melbourne-campus": random.randint(1,100),
                "stott-s-colleges-box-hill-campus": random.randint(1,100),
                "rmit-university-point-cook-campus": random.randint(1,100),
                "rmit-university-bundoora-campus": random.randint(1,100),
                "rmit-university-rmit-city-campus": random.randint(1,100),
                "rmit-univeristy-brunswick-campus": random.randint(1,100),
                "angad-australian-institute-of-technology-la-trobe-st-campus": random.randint(1,100),
                "angad-australian-institute-of-technology-lonsdale-st-campus": random.randint(1,100),
                "torrens-university-flinders-st-campus": random.randint(1,100),
                "torrens-university-fitzroy-campus": random.randint(1,100),
                "barkly-international-college-north-melbourne-campus-automotive-workshop": random.randint(1,100),
                "barkly-international-college-city-campus": random.randint(1,100),
                "deakin-university-burwood-campus": random.randint(1,100),
                "deakin-university-geelong-waterfront-campus": random.randint(1,100),
                "deakin-college-mibt-burwood-campus": random.randint(1,100),
                "alfred-deakin-college-mibt-waurn-ponds-campus": random.randint(1,100),
                "deakin-university-warrnambool-campus": random.randint(1,100),
                "deakin-university-waurn-ponds-campus": random.randint(1,100)
            }
        }


'''
0
1 LOCATION
2 SUBURB_TOWN_NAME
3 SUBURB_RESIDENTS
4 SUBURB_LONG
5 SUBURB_LAT
6 FID
7 DOMAIN_URL
8 REAL_ESTATE_COM_AU_URL
9 SUBURB_MOST_COMMON_EXPENSE_TIER
10 SUBURB_PRICE_RANGE_RANK
11 SUBURB_PRICE_RANK_IN_PERCENTILE
12 SUBURB_RENTAL_PRICE_SCALE_RANK
13 SUBURB_OFFENCES_PER_10000_POPULATION
14 TOTAL_2016_ADJUSTED_OFFENCES_PER_SUBURB_TOWN_NAME
15 SUBURB_TOWN_NAME_2016_ADJUSTED_CRIME_RANK
16 SUBURB_TOWN_NAME_2016_ADJUSTED_CRIME_RANK_PERCENTILE
17 ADJUSTED_CRIME_RANK_SCALE
18 SUBURB_MOST_INT_STUDENT_LANG
19 INT_STUDENT_POPULATION_ARRIVAL_ALL_YEARS
20 TOTAL_INT_STUDENTS_PER_SUBURB
21 TOTAL_INT_STUDENT_PER_LANGUAGE
22 TMP_INT_STUDENT_NATIVE_LANG
23 TMP_SUBURB_STUDENT_POPULATION_SCALE_RANK
24 Acholi
25 African Languages, nec
26 African Languages, nfd
27 Afrikaans
28 Akan
29 Albanian
30 Amharic
31 Anuak
32 Arabic
33 Armenian
34 Assyrian Neo-Aramaic
35 Bengali
36 Bisaya
37 Bosnian
38 Bulgarian
39 Burmese
40 Burmese and Related Languages, nec
41 Burmese and Related Languages, nfd
42 Cantonese
43 Catalan
44 Cebuano
45 Chaldean Neo-Aramaic
46 Chin Haka
47 Chinese, nfd
48 Creole, nfd
49 Croatian
50 Czech
51 Danish
52 Dari
53 Dhivehi
54 Dinka
55 Dravidian, nec
56 Dutch
57 English
58 Estonian
59 Fijian
60 Filipino
61 Finnish
62 French
63 French Creole, nfd
64 German
65 Greek
66 Gujarati
67 Hakka
68 Harari
69 Hausa
70 Hazaraghi
71 Hebrew
72 Hindi
73 Hungarian
74 Iban
75 Igbo
76 Ilonggo (Hiligaynon)
77 Inadequately described
78 Indonesian
79 Iranic, nfd
80 Italian
81 Japanese
82 Kannada
83 Karen
84 Khmer
85 Kinyarwanda (Rwanda)
86 Kirundi (Rundi)
87 Konkani
88 Korean
89 Kurdish
90 Lao
91 Lithuanian
92 Loma (Lorma)
93 Luganda
94 Macedonian
95 Malay
96 Malayalam
97 Maltese
98 Mandarin
99 Maori (Cook Island)
100 Maori (New Zealand)
101 Marathi
102 Mauritian Creole
103 Min Nan
104 Mongolian
105 Nepali
106 No international students recorded as living in this area.
107 Norwegian
108 Not stated
109 Nuer
110 Nyanja (Chichewa)
111 Oriya
112 Oromo
113 Other Southern Asian Languages
114 Pashto
115 Persian (excluding Dari)
116 Pidgin, nfd
117 Polish
118 Portuguese
119 Punjabi
120 Rohingya
121 Romanian
122 Russian
123 Samoan
124 Serbian
125 Shilluk
126 Shona
127 Sindhi
128 Sinhalese
129 Slovak
130 Slovene
131 Somali
132 Southern Asian Languages, nfd
133 Spanish
134 Swahili
135 Swedish
136 Tagalog
137 Tamil
138 Telugu
139 Tetum
140 Thai
141 Tibetan
142 Tigrinya
143 Tok Pisin (Neomelanesian)
144 Tongan
145 Tswana
146 Turkish
147 Tuvaluan
148 Ukrainian
149 Urdu
150 Vietnamese
151 Wu
152 Yoruba
153 Zomi
'''
with open('FINAL_SUBURB_ANALYSIS.csv', 'rb') as csvfile:
    readr = csv.reader(csvfile, delimiter=',')
    initial = readr.next()
    for line in readr:
        print json.dumps(row_to_obj(line))
    # print initial
    # for row in readr:
    #   print ', '.join(row)