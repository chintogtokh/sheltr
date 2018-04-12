import { version } from '../../package.json';
import { Router } from 'express';
import cars from './cars';

export default ({ config, db }) => {
	let api = Router();

	// mount the cars resource
	api.use('/cars', cars({ config, db }));

	// perhaps expose some API metadata at the root
	api.get('/', (req, res) => {
		res.json({ version });
	});

	return api;
}
