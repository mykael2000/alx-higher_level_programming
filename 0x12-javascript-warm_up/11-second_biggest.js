#!/usr/bin/node

let biggie = 0;
let i;
const array = [];
for (i = 2; i < process.argv.length; i++) {
  if (Number.isNaN(parseInt(process.argv[i])) === false) {
    array[i - 2] = parseInt(process.argv[i]);
  }
}

if (array.length > 1) {
  biggie = Math.max.apply(null, array);
  i = array.indexOf(biggie);
  array[i] = -Infinity;
  biggie = Math.max.apply(null, array);
}

console.log(biggie);
