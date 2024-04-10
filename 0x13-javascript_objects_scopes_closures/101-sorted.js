#!/usr/bin/node

// imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const a in valsUniq) {
  const list = [];
  for (const b in totalist) {
    if (totalist[b][1] === valsUniq[a]) {
      list.unshift(totalist[b][0]);
    }
  }
  newDict[valsUniq[a]] = list;
}
console.log(newDict);
