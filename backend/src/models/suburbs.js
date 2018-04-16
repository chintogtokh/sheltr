import mongoose from 'mongoose';

const SuburbSchema = mongoose.Schema({
    name: {type: String, required: true},
    population: {type: String},
    shim: {type: String, unique: true},
    average_rental: {type: String},
    most_popular_language: {type: String},
    amenities: {
    	bus: Boolean,
    	train: Boolean,
    	tram: Boolean
    },
    outlinks: {
    	realestate: String,
    	domain: String
    }
}, {collection : 'suburbs'});

export default mongoose.model('Suburb', SuburbSchema);