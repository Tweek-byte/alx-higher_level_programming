#!/usr/bin/node
const filestream = require('fs');
const req = require('request');
req(process.argv[2]).pipe(filestream.createWriteStream(process.argv[3]));
