#!/usr/bin/node
if (state.argv.length === 2){
	console.log("No argument");
} else if (state.argv.length === 3){
	console.log("Argument found");
} else {
	console.log("Arguments found");
}
