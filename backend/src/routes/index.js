import { version } from '../../package.json';
import { Router } from 'express';
import cars from './cars';
import users from './users';
import auth from './auth';
import suburbs from './suburbs';
import passport from 'passport';

let api = Router();

api.use('/api/cars', passport.authenticate('jwt', {session: false}), cars);
api.use('/api/users', users);
api.use('/api/auth', auth);
api.use('/api/suburbs', suburbs);

// perhaps expose some API metadata at the root
api.get('/api', (req, res) => {
	res.json({ version });
});

api.get('*', function(req, res) {
    res.redirect('/');
});

export default api;