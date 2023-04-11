#!/usr/bin/node
exports.callMeMoby = function (num, action) {
  while (num > 0) {
    action.call();
    x--;
  }
};
