#!/usr/bin/node
const meth = require('request');
const link = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
meth(link, function (error, response, body) {
  if (!error) {
    const values = JSON.parse(body).characters;
    printCharacters(values, 0);
  }
});

function printCharacters (values, index) {
  meth(values[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < values.length) {
        printCharacters(values, index + 1);
      }
    }
  });
}
