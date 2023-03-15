function generateRandomInt(min,max){
    return Math.floor((Math.random() * (max+1 -min)) +min) * 1000;
}
console.log(generateRandomInt(2,5))