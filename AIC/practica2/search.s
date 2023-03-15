	.data
a: 	.dword 9,8,0,1,0,5,3,1,2,0
tam: 	.dword 10 ; Tama ̃no del vector
cont: 	.dword 0 ; N ́umero de componentes == 0

	.text
start:	 dadd r1,$gp,a ; Puntero
	ld r4,tam($gp) ; Tama ̃no lista
	dadd r10,r0,r0 ; Contador de ceros
	
loop:
	dsub r4, r4, #1
	ld r2, 0(r1)
	bneqz r2, noZero
	dadd r10, r10 #1
noZero:
	dadd r1, r1, #4
	bneqz r4, loop
	sd r10, cont($gp)
	trap #0
