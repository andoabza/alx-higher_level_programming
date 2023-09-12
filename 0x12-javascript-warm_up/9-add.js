#!/usr/bin/node
const fir = process.argv[2];
const sec = process.argv[3];
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
add(fir, sec);
