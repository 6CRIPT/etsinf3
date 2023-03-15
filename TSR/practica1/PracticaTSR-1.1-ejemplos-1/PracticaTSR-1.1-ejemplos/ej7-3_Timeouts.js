
//Uso de operaciones asíncronas, aquí modeladas con la función setTimeout.
//Note el valor de índice asociado a las ejecuciones de las temporizaciones.


for(var i=0; i<10; i++) {
	var x = 0
  setTimeout (function (índice){
	
	return function(){
		x++
			console.log(x)
	  		console.log("índice: ",índice)
	  }
	}(i), i*1000);
}


console.log("Terminado script, valor de i: " + i);

