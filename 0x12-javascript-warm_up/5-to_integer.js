#!/usr/bin/node

const n = Math.floor(process.argv[2]);
if (Number.isInteger(n)) {
  console.log(`My number: ${n}`);
} else {
  console.log('Not a number');
