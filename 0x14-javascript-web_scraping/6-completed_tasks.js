#!/usr/bin/node
// Request

const req = require('request');

req.get(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const done = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!done[todo.userId]) {
        done[todo.userId] = 1;
      } else {
        done[todo.userId] += 1;
      }
    }
  });
  console.log(done);
});
