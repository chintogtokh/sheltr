import { version } from '../../package.json';
import { Router } from 'express';
import cars from './cars';
import users from './users';

let api = Router();

api.use('/cars', cars);
api.use('/users', users);

// perhaps expose some API metadata at the root
api.get('/', (req, res) => {
	res.json({ version });
});

export default api;