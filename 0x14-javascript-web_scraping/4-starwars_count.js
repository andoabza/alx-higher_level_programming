#!/usr/bin/node
/** a script that return title of movie id person **/
const req = require('request');

const uri = process.argv[2];
req.get({
  uri
  // gzip: true
},
function (err, resp, body) {
  if (err) throw (err);
  body = JSON.parse(body).results;
  const moviesWithWedgeAntilles = body.filter((body) =>
    body.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
  const num = moviesWithWedgeAntilles.length;
  console.log(num);
}
);
