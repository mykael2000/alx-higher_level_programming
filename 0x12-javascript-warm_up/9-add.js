#!/usr/bin/node
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
let num1 = process.argv[2];
let num2 = process.argv[3];

add(num1, num2);
