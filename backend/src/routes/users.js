import userModel from '../models/users';
import { Router } from 'express';

let userRouter = Router();

userRouter.get('/', (req, res) => {
	var promise = userModel.getAll;
	promise().then( data => {
		res.send(data);
	})
});

// userRouter.route('/authenticate')
// 	.post(userModel.authenticateUser);

export default userRouter;