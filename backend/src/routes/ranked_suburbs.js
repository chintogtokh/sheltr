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

    var language = (typeof preferences.language !== "undefined")? preferences.language :0;
    var uni = (typeof preferences.uni !== "undefined")?preferences.uni:null;
    var filter = (typeof preferences.filter !== "undefined")?preferences.filter:null;
    var distance = (typeof preferences.distance !== "undefined")?preferences.distance:null;


    var query = [{
        "$match": {}
    },{
        $project: {
            name: true,
            shim: true,
            rating_affordability: true,
            coords: true,
            rating_safety: true,
            universities: true,
            ["language." + actualLanguage]: true
        }
    }];

    //distance
    query[0]['$match']["university_distances."+uni+".number"] = { "$exists": true, "$lt": parseFloat(distance) };

    var sorter = "";
    switch(filter){
        case "distance":
            sorter = "university_distances."+uni+".number";
            break;
        case "affordability":
            sorter = "university_distances."+uni+".number";
            break;
        case "safety":
            sorter = "university_distances."+uni+".number";
            break;
        case "language":
            sorter = "university_distances."+uni+".number";
            break;
        default:
            sorter = "university_distances."+uni+".number";
    }

    // query[0]['$match']["stats.suburb-residents.number"] = { "$exists": true, "$gt": 50 };

    suburbModel.aggregate(query).sort({
        [sorter]: -1
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