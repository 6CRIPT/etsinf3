(defglobal ?*nod-gen* = 0)


(deffacts datosDin
	(robot 1 1 0 farolas far 3 3 1 far 4 3 2 far 5 5 3 prof 0)
	
)

(deffacts datosStatic
	(altura 5)
	(anchura 5)
	(almacen 2 3)
	(puedeCoger 1 2 3)
	;;no defino la capacidad maxima porque en rellenar hago un test que compruebe que 	;;nunca pase de 3
)


(defrule moverArriba 
	(robot ?xR ?yR ?bomb farolas $?farolas prof ?nivel)
	(profundidadMax ?prof)
	(altura ?altura)
	(test (< ?nivel ?prof))
	(test (< ?yR ?altura))
	(test (not(member$(create$ ?xR (+ ?yR 1)) $?farolas)))
	=>
	(assert (robot ?xR (+ ?yR 1) ?bomb farolas $?farolas  prof (+ ?nivel 1)))
	(bind ?*nod-gen* (+ ?*nod-gen* 1))
)

(defrule moverAbajo 
	(robot ?xR ?yR ?bomb farolas $?farolas prof ?nivel)
	(profundidadMax ?prof)
	(test (< ?nivel ?prof))
	(test (> ?yR 1))
	(test (not(member$(create$ ?xR (- ?yR 1)) $?farolas)))
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
	(test (not(member$(create$ (+ ?xR 1) ?yR) $?farolas)))
	=>
	(assert (robot (+ ?xR 1) ?yR ?bomb farolas $?farolas prof (+ ?nivel 1)))
	(bind ?*nod-gen* (+ ?*nod-gen* 1))
)

(defrule moverIzquierda 
	(robot ?xR ?yR ?bomb farolas $?farolas prof ?nivel)
	(profundidadMax ?prof)
	(test (< ?nivel ?prof))
	(test (> ?xR 1))
	(test (not(member$(create$ (- ?xR 1) ?yR) $?farolas)))
	=>
	(assert (robot (- ?xR 1) ?yR ?bomb farolas $?farolas prof (+ ?nivel 1)))
	(bind ?*nod-gen* (+ ?*nod-gen* 1))

)
(defrule rellenar
	
	(robot ?xR ?yR ?bomb farolas $?farolas prof ?nivel)
	(profundidadMax ?prof)
	(test (< ?nivel ?prof))
	(almacen ?xA ?yA)
	(test(and(eq ?xR ?xA)(eq ?yR ?yA)))
	(puedeCoger $?no1 ?bombillas $?no2)
	(test (< (+ ?bomb ?bombillas) 4 ) )
	=>
	(assert (robot ?xR ?yR (+ ?bomb ?bombillas) farolas $?farolas prof (+ ?nivel 1)))
	(bind ?*nod-gen* (+ ?*nod-gen* 1))
)
(defrule reparar 
	
	(robot ?xR ?yR ?bomb farolas $?resto1 far ?xF ?yF ?numB $?resto2 prof ?nivel)
	(profundidadMax ?prof)
	(test (< ?nivel ?prof))
	(or
		(test (and(eq ?xR ?xF)(eq ?yR (+ ?yF 1))))
		(test (and(eq ?xR ?xF)(eq ?yR (- ?yF 1))))
		(test (and(eq ?xR (+ ?xF 1))(eq ?yR ?yF)))
		(test (and(eq ?xR (- ?xF 1))(eq ?yR ?yF)))
	)
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
	(robot ?x1 ?x2 0 farolas prof $?prof)
	
	=>
	(printout t "Se llego al final")
	(halt)
)