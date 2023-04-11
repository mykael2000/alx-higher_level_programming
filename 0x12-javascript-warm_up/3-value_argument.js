#!/usr/bin/node
// the below does an argument test
let x = process.argv;
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
