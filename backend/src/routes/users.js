import userModel from '../models/users';

import {
    Router
} from 'express';

let userRouter = Router();

userRouter.get('/', (req, res) => {
    var promise = userModel.getAll;
    promise().then(data => {
        res.send(data);
    })
});

userRouter.post('/authenticate', (req, res, next) => {

    let {
        username,
        password
    } = req.body;

    var promise = userModel.findOne({'username': username }, (err, user) => {
            if (user == null) {
                let err = new Error("Username or password doesn't exist");
                err.statusCode = 403;
                next(err);
                // promise.reject();
                return { then: function() {} };
            }
        })
        .then( user.checkPassword(password))
        .catch((err) => {
            err.statusCode = 500;
            return next(err);
        });
    // .catch((err) => {
    //     console.log("2");
    //     res.status(401).json({
    //         message: err || "Validation failed. Given email and password aren't matching."
    //     })
    // })
    // .then(data => {
    //     console.log("3");
    //     console.log(data.password);
    // })
    // .catch((err) => {
    //     console.log("4");
    //     res.status(401)
    //         .json({
    //             message: err || "Validation failed. Given email and password aren't matching."
    //     })
    // });
});

export default userRouter;