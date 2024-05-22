#!/usr/bin/node
const req = require('request');
const ad = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
req(ad, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
