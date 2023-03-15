const fs = require('fs')
function afterRead(n) {
    return function (err, data) {
        if (err) console.error(n, 'not found')
        else console.log(data.toString())
    }
}
function startReading(n) {
    return function () { fs.readFile(n, afterRead(n)) }
}
function f(){
    console.log(i)
for (var i= 1; i <= 2; i++) {
    fs.writeFileSync('data' + i + '.txt', 'Hello' + i)
}

}
f();
for (let i = 1; i <= 3; i++) {
    var filename = 'data' + i + '.txt'
    var time = 100 - 10 * i
    console.log(i)
    setTimeout(startReading(filename), time)
}
// console.log("root(" + i + ") =", Math.sqrt(i))