#!/usr/bin/node
require('request')(process.argv[2], function (error, response, body) {
  if (!error) {
    const output = JSON.parse(body).results;
    console.log(output.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
