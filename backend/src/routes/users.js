import userModel from '../models/users';
import { Router } from 'express';

let userRouter = Router();

userRouter.route('/')
	.get(userModel.getAll);

userRouter.route('/authenticate')
	.post(userModel.authenticate);

export default userRouter;