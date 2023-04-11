#!/usr/bin/node
function factorialfunc (num) {
	if ((Number.isNaN(num)) || (num === 1)) {
		return 1;
	}
	return factorialfunc(num-1) * num;
}
console.log(factorialfunc(parseInt(process.argv[2])));
