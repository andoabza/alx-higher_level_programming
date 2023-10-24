#!/usr/bin/node
/** a script that write to file **/
const fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', function (err) {
  if (err) throw err;
});
