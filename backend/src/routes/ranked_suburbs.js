import suburbModel from '../models/suburbs';
import {
    Router
} from 'express';

let rankedSuburbRouter = Router();

rankedSuburbRouter.post('/', (req, res) => {
    // res.send([1, 2, 3]);
    const preferences = req.body;
    //var promise = suburbModel.aggregate({ $mul: { rating_safety: 1.25} },"rating_safety rating_affordability");

    var user_safety =  (typeof preferences.crimeSafety === "undefined")? 1 :preferences.crimeSafety;;
    var user_affordability = (typeof preferences.affordability === "undefined")?1:preferences.affordability;

    suburbModel.aggregate([{
        $project: {
            name: true,
            shim: true,
            rating_affordability: true,
            rating_safety: true,
            userRating: {
                $sum: [{
                    $multiply: [parseInt(user_affordability), "$rating_affordability"]
                }, {
                    $multiply: [parseInt(user_safety), "$rating_safety"]
                }]
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