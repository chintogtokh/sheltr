import { version } from '../../package.json';
import { Router } from 'express';
import cars from './cars';
import users from './users';
import auth from './auth';
import suburbs from './suburbs';
import passport from 'passport';

let api = Router();

api.use('/cars', passport.authenticate('jwt', {session: false}), cars);
api.use('/users', users);
api.use('/auth', auth);
api.use('/suburbs', suburbs);

// perhaps expose some API metadata at the root
api.get('/', (req, res) => {
	res.json({ version });
});

api.get('*', function(req, res) {
    res.redirect('/');
});

export default api;