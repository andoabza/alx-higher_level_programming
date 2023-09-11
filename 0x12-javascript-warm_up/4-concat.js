#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('undefined is undefined');
} else if (process.argv.length === 3) {
  console.log(process.argv[2].concat(' is undefined'));
} else {
  console.log(process.argv[2].concat(' is ', process.argv[3]));
}
