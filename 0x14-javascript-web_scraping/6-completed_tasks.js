#!/usr/bin/node
const req = require('request');
req(process.argv[2], function (error, response, body) {
  if (!error) {
    const list = JSON.parse(body);
    const done = {};
    list.forEach((todo) => {
      if (todo.done && done[todo.userId] === undefined) {
        done[todo.userId] = 1;
      } else if (todo.done) {
        done[todo.userId] += 1;
      }
    });
    console.log(done);
  }
});
