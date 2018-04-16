import mongoose, {Schema} from 'mongoose';
import md5 from 'md5';

const UserSchema = Schema({
    username: {
        type: String,
        required: true,
        unique: true
    },
    password: {
        type: String,
        select: false,
        required: true
    },
    first_name: {
        type: String,
        required: true
    },
    last_name: {
        type: String,
        required: true
    }
}, {
    collection: 'users'
});

UserSchema.pre('save', function () {
    var user = this;

    // only hash the password if it has been modified (or is new)
    if (!user.isModified('password')) return next();

    //md5 here, see http://devsmash.com/blog/password-authentication-with-mongoose-and-bcrypt
    user.password = md5(user.password);
    next();
});

export default mongoose.model('User', UserSchema);