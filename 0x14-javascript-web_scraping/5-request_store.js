#!/usr/bin/node
/** a script that save url content to file **/
const req = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
req(url, function (err, resp, body) {
  if (err) throw (err);
  fs.writeFile(filePath, body, function (err) {
    if (err) throw (err);
  });
});
