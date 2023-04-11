#!/usr/bin/node 
exports.addMeMaybe = function (num, action){
	action.call(this, num + 1);
}
