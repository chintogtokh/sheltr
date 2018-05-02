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
                    $multiply: [50, "$universities." + uni]
                });
    }

    if(language && actualLanguage){
        query[0]['$match']["language."+actualLanguage] = { "$exists": true, "$ne": 0 };
    }

    query[0]['$match']["universities."+uni] = { "$exists": true, "$gt": 80 };

    suburbModel.aggregate(query).sort({
        'userRating': -1
    }).limit(8).exec(function(err, docs) {
        console.log(err);
        if(typeof docs==="undefined"){
            res.send([]);
        }
        else{
            res.send(docs);
        }
    });;

    // promise.then(data => {
    //     if (data) {
    //      res.send(data);
    //     }
    //     else {
    //      res.status(404).json({
    //             message: "Suburb doesn't exist"
    //         });
    //     }
    // })

});

export default rankedSuburbRouter;