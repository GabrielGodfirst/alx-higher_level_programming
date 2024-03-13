#!/usr/bin/node

exports.converter = function (base) {
  return function convertToBase (num) {
    const alphabet = 'ABCDEF';
    if (num === 0) {
      return '';
    } else {
      let remainder = num % base;
      if (base === 16 && remainder >= 10) {
        remainder = alphabet[remainder - 10];
      }
      return convertToBase(Math.floor(num / base)) + remainder;
    }
  };
};
