#!/usr/bin/node
const process = require('process');
var argv = process.argv;

if (argv.length === 2)
{
	console.log("No argument");
}
if (argv.length === 3)
{
        console.log("Argument found");
}
else
{
        console.log("Arguments found");
}
