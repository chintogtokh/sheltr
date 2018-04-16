import carModel from '../models/cars';
import { Router } from 'express';

let carRouter = Router();

// carModel Routes
carRouter.route('/')
	.get(carModel.getAll);


export default carRouter;