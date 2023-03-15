const net = require('net');
const IP = '127.0.0.1';
const client = net.connect({port:8000}, IP, function() { //connect listener
	console.log('client connected');
	client.write('world!\r\n');
});

client.on('data', function(data) {
 	console.log(data.toString());
 	client.end(); //no more data written to the stream
});

client.on('end', function() {
	console.log('client disconnected');
});
