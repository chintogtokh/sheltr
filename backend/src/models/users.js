import mongoose, {Schema} from 'mongoose';
mongoose.Promise = global.Promise;

const UserSchema = Schema({
    username: {
        type: String,
        required: true
    },
    password: {
        type: String,
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

let userModel = mongoose.model('User', UserSchema);

userModel.getAll = () => {
    var query = userModel.find({}, 'username first_name last_name');
    var promise = query.exec();
    return promise;
};

// userModel.authenticateUser = (req, res) => {
//     let {
//         email,
//         password
//     } = req.body

//     db.User.findByEmail(email)
//         .then((user) => (!user) ? Promise.reject("User not found.") : user)
//         .then((user) => user.comparePassword(password))
//         .then((user) => user.publicParse(user))
//         .then((user) => {
//             res.status(200)
//                 .json({
//                     success: true,
//                     token: createJWToken({
//                         sessionData: user,
//                         maxAge: 3600
//                     })
//                 })
//         })
//         .catch((err) => {
//             res.status(401)
//                 .json({
//                     message: err || "Validation failed. Given email and password aren't matching."
//                 })
//         })
// };

userModel.registerNewUser = (req, res) => {
    console.log(req.body);
    res.send({
        'a': 'aa'
    });
};

export default userModel;