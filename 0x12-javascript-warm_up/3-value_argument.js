#!/usr/bin/node
// the below does an argument test
let x = process.argv;
if (x[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
