const express = require('express');
const router = express.Router();
const jwt = require('jsonwebtoken');
const passport = require("passport");

router.post('/login', function(req, res, next) {
    passport.authenticate('local', {
        session: false
    }, (err, user, info) => {
      // console.log({
      //   err: err,
      //   user: user,
      //   info: info
      // });
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
            const token = jwt.sign(user.toJSON(), 'your_jwt_secret');
            return res.json({
                user,
                token
            });
        });
    })(req, res);
});

export default router;