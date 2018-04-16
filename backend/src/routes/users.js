import userModel from '../models/users';

import {Router } from 'express';

let userRouter = Router();

userRouter.get('/', (req, res) => {
    var promise = userModel.getAll;
    promise().then(data => {
        res.send(data);
    })
});

export default userRouter;