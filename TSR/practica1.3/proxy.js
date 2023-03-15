const net = require('net');
const LOCAL_PORT = 8100;
const LOCAL_IP = '127.0.0.1';
// const REMOTE_PORT = 80;
// const REMOTE_IP = '158.42.4.23'; // www.upv.es
const server = net.createServer(function (socket) {
	const serviceSocket = new net.Socket();
	serviceSocket.connect(parseInt(process.argv[3]), process.argv[2], function () {
		socket.on('data', function (msg) {
			console.log(msg + "");
			serviceSocket.write(msg);
		});
		serviceSocket.on('data', function (data) {
			socket.write(data);
			// console.log(data);
		});
	});
}).listen(LOCAL_PORT, LOCAL_IP);
console.log("TCP server accepting connection on port: " + LOCAL_PORT);