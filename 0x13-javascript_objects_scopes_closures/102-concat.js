#!/usr/bin/node

const F = require('fs');

const fArg = F.readFileSync(process.argv[2]).toString();
const sArg = F.readFileSync(process.argv[3]).toString();
F.writeFileSync(process.argv[4], fArg + sArg);
