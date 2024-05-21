#!/usr/bin/node
const filestream = require('fs');
filestream.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
