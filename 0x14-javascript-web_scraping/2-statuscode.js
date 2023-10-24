#!/usr/bin/node
/** a script that print status code **/
const req = require('request');

req
  .get(process.argv[2])
  .on('response', function (response){

  console.log("code: ", response.statusCode);
  });
