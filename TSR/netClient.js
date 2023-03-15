const net = require('net');
const args = process.argv.slice(2)
const client = net.connect({port:8000, host:args[0]}, function() { //connect listener
	console.log(args[0])
	console.log('client connected');
	// client.write('world!\r\n');
	client.write(JSON.stringify(args[1]))
});

client.on('data', function(data) {
 	console.log(JSON.parse(data));
 	client.end();
	 //no more data written to the stream
});

client.on('end', function() {
	console.log('client disconnected');
});
