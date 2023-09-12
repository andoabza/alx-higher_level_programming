#!/usr/bin/node
const arg = process.argv[2];
const num = Number(arg);
let i = 0;
if (num) {
  while (i < arg) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
