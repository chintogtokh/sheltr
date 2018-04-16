import passport from 'passport';
import passportJWT from 'passport-jwt';
import {Strategy as LocalStrategy} from 'passport-local';
import userModel from './models/users';
import md5 from 'md5'; //this is temporary!!!
import config from './config/config.dev';

const JWTStrategy   = passportJWT.Strategy;
const ExtractJWT = passportJWT.ExtractJwt;


passport.use(new LocalStrategy({
        usernameField: 'username',
        passwordField: 'password'
    },
    function(username, password, cb) {
        //this one is typically a DB call. Assume that the returned user object is pre-formatted and ready for storing in JWT
        return userModel.findOne({
                username: username
            }).select("+password")
            .then(user => {
                if (!user || (user.password != md5(password))) {
                    return cb(null, false,
                        'Incorrect username or password.'
                    );
                }
                return cb(null, user,
                    'Logged In Successfully'
                );
            })
            .catch(err => cb(err));
    }
));

passport.use(new JWTStrategy({
        jwtFromRequest: ExtractJWT.fromAuthHeaderAsBearerToken(),
        secretOrKey   : config.jwtSecret
    },
    function (jwtPayload, cb) {

        //find the user in db if needed. This functionality may be omitted if you store everything you'll need in JWT payload.
        return UserModel.findOneById(jwtPayload.id)
            .then(user => {
                return cb(null, user);
            })
            .catch(err => {
                return cb(err);
            });
    }
));
