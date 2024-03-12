#!/usr/bin/node

function factorial (n) {
  // Base case: if n is NaN or 0, return 1
  if (isNaN(n) || n === 0) {
    return 1;
  } else {
    // Recursive case: compute factorial recursively
    return n * factorial(n - 1);
  }
}

const num = parseInt(process.argv[2]);
console.log(factorial(num));
