import mongoose from 'mongoose';

const SuburbSchema = mongoose.Schema({
    name: {type: String, required: true},
    population: {type: String},
    shim: {type: String, unique: true},
    rating_safety: {type: Number},
    rating_affordability: {type: Number},
    // most_popular_language: {type: String},
    // amenities: {
    // 	bus: Boolean,
    // 	train: Boolean,
    // 	tram: Boolean
    // },
    outlinks: {
    	realestate: String,
    	domain: String
    },
    coords: {
        lat: Number,
        lng: Number
    }
}, {collection : 'suburbs'});


SuburbSchema.methods.user_rank = function(a,b) {
    return this.rating_safety * a;
};

export default mongoose.model('Suburb', SuburbSchema);