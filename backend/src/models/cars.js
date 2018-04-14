import mongoose from 'mongoose';
mongoose.Promise = global.Promise;

const CarSchema = mongoose.Schema({
    name: {type: String, required: true}
}, {collection : 'cars'});

let carModel = mongoose.model('Car', CarSchema);

carModel.getAll = (req, res) => {
//    return carModel.find({});
  carModel.find({}, function (err, cars) {
    if (err) res.send(err);
    res.send(cars);
  })
}

carModel.addCar = (carToAdd) => {
    return carToAdd.save();
}

carModel.removeCar = (carName) => {
    return carModel.remove({name: carName});
}

export default carModel;