import suburbModel from '../models/suburbs';
import {
    Router
} from 'express';

let rankedSuburbRouter = Router();

rankedSuburbRouter.get('/', (req, res) => {
    // res.send([1, 2, 3]);

    //var promise = suburbModel.aggregate({ $mul: { rating_safety: 1.25} },"rating_safety rating_affordability");

    var user_safety = 1;
    var user_affordability = 10;

    suburbModel.aggregate([{
        $addFields: {
            userRating: {
                $sum: [{
                    $multiply: [user_affordability, "$rating_affordability"]
                }, {
                    $multiply: [user_safety, "$rating_safety"]
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