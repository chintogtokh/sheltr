import {
    verifyJWTToken
} from './libs/auth'

// export function verifyJWT_MW(req, res, next) {
//     let token = (req.method === 'POST') ? req.body.token : req.query.token

//     verifyJWTToken(token)
//         .then((decodedToken) => {
//             req.user = decodedToken.data
//             next()
//         })
//         .catch((err) => {
//             res.status(401)
//                 .json({
//                     error: "Invalid auth token provided."
//                 })
//         })
// }

export function errorHandler(err, req, res, next) {
    console.info(err.message);
    if (typeof err.statusCode == 'undefined'){
        err.statusCode = 500;
    }
    res.status(err.statusCode).send({
        error: err.message
    });
    return;
}