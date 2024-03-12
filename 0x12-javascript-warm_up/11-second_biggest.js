#!/usr/bin/node

function secondLargest (arr) {
  // Sort the array in descending order
  arr.sort((a, b) => b - a);

  // Return the second element if it exists, otherwise return 0
  return arr[1] || 0;
}

// Convert all arguments to integers and store them in an array
const integers = process.argv.slice(2).map(arg => parseInt(arg));

// Print the second largest integer using the secondLargest function
console.log(secondLargest(integers));
