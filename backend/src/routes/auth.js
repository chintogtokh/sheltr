import User from '../models/users';
import express from 'express';
import jwt from 'jsonwebtoken';
import passport from 'passport';
import sanitize from 'mongo-sanitize';
import config from '../config/config.dev';

const router = express.Router();

router.post('/login', function(req, res, next) {
    passport.authenticate('local', {
        session: false
    }, (err, user, info) => {
        if (err) {
            return res.status(400).json({
                message: 'Something is not right',
                user: user
            });
        }
        else if(!user){
            return res.status(400).json({
                message: info
            });
        }
        req.login(user, {
            session: false
        }, (err) => {
            if (err) {
                res.send(err);
            }
            // generate a signed son web token with the contents of user object and return it in the response
            const token = jwt.sign(user.toJSON(), config.jwtSecret);
            // convert to object coz mongoose is a clingy mofo
            user = user.toObject()
            delete user.password; //delete the password from the response
            return res.json({
                user,
                token
            });
        });
    })(req, res);
});

router.post('/register', function(req, res, next) {
    var username = sanitize(req.body.username);
    var password = sanitize(req.body.password);
    var first_name = sanitize(req.body.first_name);
    var last_name = sanitize(req.body.last_name);

    var user = new User({username: username, password: password, first_name: first_name, last_name: last_name});
    user.save()
    .then(function(user){
        return res.json({
            'message': 'Registered successfully'
        });
    }).catch(function(error){
        return res.status(500).json({
            'message': 'Username already exists or is invalid'
        });
    });

});

export default router;