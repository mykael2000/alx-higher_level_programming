#!/usr/bin/node

require('request')(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const done = {};
    const events = JSON.parse(body);
    for (const i in events) {
      const event = events[i];
      if (event.completed === true) {
        if (done[event.userId] === undefined) {
          done[event.userId] = 1;
        } else {
          done[event.userId]++;
        }
      }
    }
    console.log(done);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
