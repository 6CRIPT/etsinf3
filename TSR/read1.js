const fs = require('fs');
//ejer 1.3
function readFilePromise(filename) {
    return new Promise((resolve, reject) => {
        fs.readFile(filename, (err, data) => {
            if (err) reject(err + '')
            else resolve(data + '')
        })
    })
}
readFilePromise('C:\\Users\\César\\TODO\\UNIVERSIDAD\\TSR\\PRACTICAS\\practica1\\PracticaTSR-1.1-ejemplos-1\\PracticaTSR-1.1-ejemplos\\respuestas').then(console.log, console.error)
    //'C:\\Users\\César\\TODO\\UNIVERSIDAD\\TSR\\PRACTICAS\\practica1\\PracticaTSR-1.1-ejemplos-1\\PracticaTSR-1.1-ejemplos\\respuestas'
    //archivo a leer, este si existe en mi PC