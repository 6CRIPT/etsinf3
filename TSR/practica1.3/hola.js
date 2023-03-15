const ev = require ('events');
const emitter = new ev.EventEmitter
emitter.on ("event1", (x) => console.log(x));
emitter.emit ("event1", "hello");
emitter.emit ("hello");
console.log ("bye")