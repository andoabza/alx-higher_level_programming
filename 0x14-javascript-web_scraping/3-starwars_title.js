#!/usr/bin/node
/** a script that return title of movie id **/
const req = require('request');
const uri = 'https://swapi-api.alx-tools.com/api/films/';

const url = uri.concat('', process.argv[2]);
req.get({
  uri: url,
  encoding: 'utf-8',
  gzip: true
},
function (err, resp, body) {
  if (err) throw (err);
  body = JSON.parse(body);
  console.log(body.title);
}
);
