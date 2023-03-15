//he borrado los comentarios originales y he puesto alguno mio.
//emisor3.js programado por César Martínez Chico.
const ev = require('events')
const emitter = new ev.EventEmitter()
const e1 = 'e1', e2 = 'e2'
let inc = 0, t
function rand() {
    return Math.floor((Math.random() * (3000) + 2000))
}
//funcion manejadora de eventos.
function handler(e, n) {
    return (inc) => {
        n += inc
        console.log(e + "-->" + n)
    }
}
//los listener para los diferentes eventos.
emitter.on(e1, handler(e1, 0))
emitter.on(e2, handler(e2, ''))
//funcion etapa que se llama a si misma.
function etapa() {
    emitter.emit(e1, inc)
    emitter.emit(e2, inc)
    console.log("Esta etapa se ha ejecutado con: " + t + " milisegundos de retraso.")
    inc++;
    setTimeout(etapa, t = rand())
    //ESTA RECURSION HA DE PARARSE CON CTRL + C
}
//llamada lanzadera.
setTimeout(etapa, t = rand())