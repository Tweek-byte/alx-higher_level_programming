#!/usr/bin/node

const num = process.argv[2];
if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let n = 0; n < num; n++) {
    console.log('C is fun');
  }
}
