import path from "path";

let config = {};

config.logFileDir = path.join(__dirname, '../../log');
config.logFileName = 'app.log';
config.dbHost = 'localhost';
config.dbPort = '27017';
config.dbName = 'sheltr';
config.dbUser = 'admin';
config.dbPass = 'AnVkgeYGpDV6RaQ8y1duvdh+dD/E4z+dh46MUaU/DkA=';
config.serverPort = 3000;
config.bodyLimit = "100kb";
config.corsHeaders = ["Link"];
config.jwtSecret = "dummysecret";


export default config;