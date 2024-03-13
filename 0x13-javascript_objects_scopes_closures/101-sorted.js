#!/usr/bin/node

const { dict } = require('./101-data');

const usersByOccurrences = {};

for (const userId in dict) {
  const occurrences = dict[userId];
  if (!(occurrences in usersByOccurrences)) {
    usersByOccurrences[occurrences] = [];
  }
  usersByOccurrences[occurrences].push(userId);
}

console.log(usersByOccurrences);
