import universityModel from '../models/universities';
import languageModel from '../models/languages';
import suburbModel from '../models/suburbs';

import {
    Router
} from 'express';

let searchRouter = Router();

searchRouter.get('/universities', (req, res) => {

    let searchText = req.query.q;

    universityModel.find({'name': {'$regex': searchText, '$options': 'i'}}).limit(10).exec(function(err, docs) {
        res.send(docs)
    });;

});

searchRouter.get('/languages', (req, res) => {

    let searchText = req.query.q;

    languageModel.find({'name': {'$regex': searchText, '$options': 'i'}}).limit(10).exec(function(err, docs) {
        res.send(docs)
    });;

});



searchRouter.get('/suburbs', (req, res) => {

    let searchText = req.query.q;
    // console.log(req.query);

    suburbModel.find({'name': {'$regex': searchText, '$options': 'i'}},"name shim").limit(10).exec(function(err, docs) {
        res.send(docs)
    });;

});

export default searchRouter;