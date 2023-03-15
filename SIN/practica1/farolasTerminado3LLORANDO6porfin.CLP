;;Programa hecho en grupo por César Martínez Chico y Jaime Candel Martínez
(defglobal ?*nod-gen* = 0)


(deffacts datosDin
	(robot 1 1 0 farolas far 7 2 2 far 2 1 3 far 5 5 2 prof 0)
)

(deffacts datosStatic
	(altura 5)
	(anchura 5)
	(almacen 2 3)
	(puedeCoger 1 2 3)
	(cestoMax 3)
	
)


(defrule moverArriba 
	(robot ?xR ?yR ?bomb farolas $?farolas prof ?nivel)
	(profundidadMax ?prof)
	(altura ?altura)
	(test (< ?nivel ?prof))
	(test (< ?yR ?altura))
	(test (not(member$(create$ far ?xR (+ ?yR 1)) $?farolas)))
	=>
	(assert (robot ?xR (+ ?yR 1) ?bomb farolas $?farolas  prof (+ ?nivel 1)))
	(bind ?*nod-gen* (+ ?*nod-gen* 1))
)

(defrule moverAbajo 
	(robot ?xR ?yR ?bomb farolas $?farolas prof ?nivel)
	(profundidadMax ?prof)
	(test (< ?nivel ?prof))
	(test (> ?yR 1))
	(test (not(member$(create$ far ?xR (- ?yR 1)) $?farolas)))
	=>
	(assert (robot ?xR (- ?yR 1) ?bomb farolas $?farolas prof (+ ?nivel 1)))
	(bind ?*nod-gen* (+ ?*nod-gen* 1))
)

(defrule moverDerecha 
	(robot ?xR ?yR ?bomb farolas $?farolas prof ?nivel)
	(profundidadMax ?prof)
	(anchura ?ancho)
	(test (< ?nivel ?prof))
	(test (< ?xR ?ancho))
	(test (not(member$(create$ far (+ ?xR 1) ?yR ) $?farolas)))
	=>
	(assert (robot (+ ?xR 1) ?yR ?bomb farolas $?farolas prof (+ ?nivel 1)))
	(bind ?*nod-gen* (+ ?*nod-gen* 1))
)

(defrule moverIzquierda 
	(robot ?xR ?yR ?bomb farolas $?farolas prof ?nivel)
	(profundidadMax ?prof)
	(test (< ?nivel ?prof))
	(test (> ?xR 1))
	(test (not(member$(create$ far (- ?xR 1) ?yR) $?farolas)))
	=>
	(assert (robot (- ?xR 1) ?yR ?bomb farolas $?farolas prof (+ ?nivel 1)))
	(bind ?*nod-gen* (+ ?*nod-gen* 1))

)
(defrule rellenar
	
	(robot ?xR ?yR ?bomb farolas $?farolas prof ?nivel)
	(profundidadMax ?prof)
	(test (< ?nivel ?prof))
	(almacen ?xA ?yA)
	(cestoMax ?cestoMax)
	(test(and(eq ?xR ?xA)(eq ?yR ?yA)))
	(puedeCoger $?no1 ?bombillas $?no2)
	(test (<= (+ ?bomb ?bombillas) ?cestoMax ) )
	=>
	(assert (robot ?xR ?yR (+ ?bomb ?bombillas) farolas $?farolas prof (+ ?nivel 1)))
	(bind ?*nod-gen* (+ ?*nod-gen* 1))
)
(defrule reparar 
	
	(robot ?xR ?yR ?bomb farolas $?resto1 far ?xF ?yF ?numB $?resto2 prof ?nivel)
	(profundidadMax ?prof)
	(test (< ?nivel ?prof))
	(test(or
		(and(eq ?xR ?xF)(eq ?yR (+ ?yF 1)))
		(and(eq ?xR ?xF)(eq ?yR (- ?yF 1)))
		(and(eq ?xR (+ ?xF 1))(eq ?yR ?yF))
		(and(eq ?xR (- ?xF 1))(eq ?yR ?yF))
	))
	(test(<= ?numB ?bomb))
	=>
	(assert (robot ?xR ?yR (- ?bomb ?numB) farolas $?resto1 $?resto2 prof (+ ?nivel 1)))
	(bind ?*nod-gen* (+ ?*nod-gen* 1))
)	

(deffunction inicio ()
    (reset)
	(printout t "Profundidad Maxima:= " crlf)
    (bind ?prof (read))
	(printout t "Tipo de Busqueda " crlf "    1.- Anchura" crlf "    2.- Profundidad" crlf )
	(bind ?a (read))
	(if (= ?a 1)
	       then    (set-strategy breadth)
	       else   (set-strategy depth))
	(assert (profundidadMax ?prof))
        
)

(defrule final
	(declare (salience 100))
	(robot ?xR ?yR 0 farolas prof ?nivel)
	
	=>
	(printout t "Se llego al final" crlf)
	(printout t "nodos generados: " ?*nod-gen* crlf)
	(printout t "Solucion encontrada en la profundidad: " ?nivel crlf)
	(halt)
)
(defrule noFinal
	(declare (salience -150))
	(robot ?xR ?yR ?bomb farolas $?far prof ?nivel)
	=>
	(printout t "No se ha llegado a un final correcto" crlf)
	(printout t "nodos generados: " ?*nod-gen* crlf)
	(halt)
	
)