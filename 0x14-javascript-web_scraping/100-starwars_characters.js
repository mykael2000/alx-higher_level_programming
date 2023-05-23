#!/usr/bin/node

require('request').get('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const info = JSON.parse(body);
  const dc = info.characters;
  for (const i of dc) {
    require('request').get(i, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const informa = JSON.parse(body1);
      console.log(informa.name);
    });
  }
});
