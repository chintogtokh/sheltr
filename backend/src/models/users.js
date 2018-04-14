import mongoose from 'mongoose';

const UserSchema = mongoose.Schema({
        name:{
            type: String,
            required: true
        }
    },
    {
        collection : 'users'
    }
);

let userModel = mongoose.model('User', UserSchema);

userModel.getAll = (req, res) => {
    userModel.find({}, function (err, users) {
        if (err) res.send(err);
        res.send(users);
    })
};

userModel.authenticate = (req, res) => {
    // return function ( req, res ) {
        res.send({'a':'aa'});
    // }
};

export default userModel;