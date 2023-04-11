#!/usr/bin/node
let num1 = Number.isInteger(process.argv[2]);
let num2 = Number.isInteger(process.argv[2]);

if(num1 || num2 === "false") {
	console.log("Not a number");
} else {
	console.log("My number:", parseInt(process.argv[2]));
}

