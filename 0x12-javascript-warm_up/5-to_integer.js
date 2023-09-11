#!/usr/bin/node
let num = Number(process.argv[2]);
if (num)
{
	console.log('My number: '.concat(num));
}else {
	console.log('Not a number');
}

