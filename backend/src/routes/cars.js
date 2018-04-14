import carModel from '../models/cars';
import { Router } from 'express';
import { verifyJWT_MW } from '../middleware'

let carRouter = Router();

carRouter.all('*', verifyJWT_MW);

// carModel Routes
carRouter.route('/')
	.get(carModel.getAll);


export default carRouter;