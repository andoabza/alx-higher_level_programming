#!/usr/bin/node
/** a script thatread content of file**/
const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (err) throw err;
  console.log(data);
});
