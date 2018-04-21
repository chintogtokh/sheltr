import suburbModel from '../models/suburbs';
import {
    Router
} from 'express';

let rankedSuburbRouter = Router();

rankedSuburbRouter.post('/', (req, res) => {
    // res.send([1, 2, 3]);
    const preferences = req.body;
    //var promise = suburbModel.aggregate({ $mul: { rating_safety: 1.25} },"rating_safety rating_affordability");

    var crimeSafety =  (typeof preferences.crimeSafety !== "undefined")? preferences.crimeSafety:1;
    var affordability = (typeof preferences.affordability !== "undefined")? preferences.affordability:1;
    var language = (typeof preferences.language !== "undefined")? preferences.language :1;
    var actualLanguage = (typeof preferences.actualLanguage !== "undefined")? preferences.actualLanguage:null;
    var uni = (typeof preferences.uni !== "undefined")?preferences.uni:null;

    suburbModel.aggregate([{
        $project: {
            name: true,
            shim: true,
            rating_affordability: true,
            rating_safety: true,
            userRating: {
                $sum: [{
                    $multiply: [parseInt(affordability), "$rating_affordability"]
                }, {
                    $multiply: [parseInt(crimeSafety), "$rating_safety"]
                }, {
                    $multiply: [parseInt(language), "$language." + actualLanguage]
                }, {
                    $multiply: [100, "$universities." + uni]
                }
                ]
            },
        }
    }]).sort({
        'userRating': -1
    }).limit(5).exec(function(err, docs) {
        res.send(docs)
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