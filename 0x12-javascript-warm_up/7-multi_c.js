#!/usr/bin/node
let num = process.argv[2]
if (num === undefined || Number.isInterger(num)) {
	console.log("Missing number of occurences");
} else {
	const re = Number(num);
	let i = 0;
	while(i < re) {
		console.log("C is fun");
		i++;
	}
}
