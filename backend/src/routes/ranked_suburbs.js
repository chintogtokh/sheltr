import suburbModel from '../models/suburbs';
import {
    Router
} from 'express';

let rankedSuburbRouter = Router();

rankedSuburbRouter.post('/', (req, res) => {
    // res.send([1, 2, 3]);
    const preferences = req.body;

    for(var key in preferences){
        if (preferences[key]==null){
            delete preferences[key];
        }
    }
    //var promise = suburbModel.aggregate({ $mul: { rating_safety: 1.25} },"rating_safety rating_affordability");

    var crimeSafety =  (typeof preferences.crimeSafety !== "undefined")? preferences.crimeSafety:0;
    var affordability = (typeof preferences.affordability !== "undefined")? preferences.affordability:0;
    var language = (typeof preferences.language !== "undefined")? preferences.language :0;
    var actualLanguage = (typeof preferences.actualLanguage !== "undefined")? preferences.actualLanguage:null;
    var uni = (typeof preferences.uni !== "undefined")?preferences.uni:null;

    var query = [{
        "$match": {}
    },{
        $project: {
            name: true,
            shim: true,
            rating_affordability: true,
            rating_safety: true,
            universities: true,
            ["language." + actualLanguage]: true,
            userRating: {
                $sum: [{
                    $multiply: [parseInt(affordability), "$rating_affordability"]
                }, {
                    $multiply: [parseInt(crimeSafety), "$rating_safety"]
                }, {
                    $multiply: [parseInt(language), "$language." + actualLanguage]
                }
                ]
            }
        }
    }];

    if(uni){
        query[1]['$project']['userRating']['$sum'].push({
                    $multiply: [40, "$universities." + uni + ".number"]
                });

        query[0]['$match']["university_distances."+uni+".number"] = { "$exists": true, "$lt": 10 };

    }

    // if(language && actualLanguage){
    //     query[0]['$match']["language." + actualLanguage] = { "$exists": true, "$ne": 0 };
    // }


    query[0]['$match']["stats.suburb-residents.number"] = { "$exists": true, "$gt": 50 };

    suburbModel.aggregate(query).sort({
        'userRating': -1
    }).limit(16).exec(function(err, docs) {
        if(typeof docs==="undefined"){
            res.send([]);
        }
        else{
            res.send(docs);
        }
    });;

});

export default rankedSuburbRouter;