#!/usr/bin/node
const filestream = require('fs');
filestream.writeFile(process.argv[2], process.argv[3], (error) => {
	if (error) console.log(error);
});
