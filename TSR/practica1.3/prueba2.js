const fs = require('fs')
const names = ['data1.txt', 'data2.txt']
const str = 'Hola'

for (let i = 0; i < names.length; i++)
   
    fs.readFile(names[i], (e, x) => {
        if (e) return
        let lines = (x +'').split('\n')
    for (var j = 0; j < lines.length; j++)
    if (lines[j].includes(str))
        console.log(names[i],':', lines[j])
})