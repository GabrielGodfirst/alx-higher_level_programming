#!/usr/bin/node

exports.converter = function (base) {
  return function convertToBase (num) {
    if (num === 0) {
      return '';
    } else {
      return convertToBase(Math.floor(num / base)) + (num % base);
    }
  };
};
