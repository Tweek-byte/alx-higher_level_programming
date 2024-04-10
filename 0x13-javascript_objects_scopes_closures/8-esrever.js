#!/usr/bin/node

exports.esrever = function (list) {
	let len = list.length - 1;
	let a = 0;
	while (a - len < 0) {
		const aux = list[len];
		list[len] = list[a];
		list[a] = aux;
		a++;
		len--;
	}
	return list;
};
