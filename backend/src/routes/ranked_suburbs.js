import suburbModel from '../models/suburbs';
import { Router } from 'express';

let rankedSuburbRouter = Router();

rankedSuburbRouter.get('/', (req, res) => {
    res.send([1,2,3]);
    // var promise = suburbModel.findOne();
    // promise.then(data => {
    //     if (data) {
    //     	res.send(data);
    //     }
    //     else {
    //     	res.status(404).json({
    //             message: "Suburb doesn't exist"
    //         });
    //     }
    // })
});

export default rankedSuburbRouter;