(defglobal ?*nod-gen* = 0)
(defglobal ?*prof* = 60)

(deffacts datosDin
	(robot 1 1 0 farolas far 2 3 1 far 4 3 2 far 5 5 3 prof 0)
	
)

(deffacts datosStatic
	(altura 5)
	(anchura 5)
	(almacen 2 3)
)


(defrule moverArriba 
	(robot ?x1 ?x2 ?x3 farolas $?farolas prof ?nivel)
	(profundidadMax ?prof)
	(altura ?altura)
	(test (< ?nivel ?prof))
	(test (neq x2 ?altura))
	(test (not(member$(create$ ?x1 (+ ?x2 1)) $?farolas)
	=>
	(assert (robot ?x1 (+ ?x2 1) ?x3 $?farolas  (+ ?nivel 1)))
	(bind ?*nod-gen* (+ ?*nod-gen* 1))
)

(defrule moverAbajo 
	(robot ?x1 ?x2 ?x3 farolas $?farolas prof ?nivel)
	(profundidadMax ?prof)
	(test (< ?nivel ?prof))
	(test (neq x2 0))
	(test (not(member$(create$ ?x1 (- ?x2 1)) $?farolas)
	=>
	(assert robot ?x1 (- ?x2 1) ?x3 $?farolas (+ ?nivel 1))
	(bind ?*nod-gen* (+ ?*nod-gen* 1))
)

(defrule moverDerecha 
	(robot ?x1 ?x2 ?x3 farolas $?farolas prof ?nivel)
	(profundidadMax ?prof)
	(anchura ?ancho)
	(test (< ?nivel ?prof))
	(test (neq x1 ?ancho))
	(test (not(member$(create$ (+ ?x1 1) ?x2) $?farolas)
	=>
	(assert robot (+ ?x1 1) ?x2 ?x3 $?farolas (+ ?nivel 1))
	(bind ?*nod-gen* (+ ?*nod-gen* 1))
)

(defrule moverIzquierda 
	(robot ?x1 ?x2 ?x3 farolas $?farolas prof ?nivel)
	(profundidadMax ?prof)
	(test (< ?nivel ?prof))
	(test (neq x1 0))
	(test (not(member$(create$ (- ?x1 1) ?x2) $?farolas)
	=>
	(assert robot (- ?x1 1) ?x2 ?x3 $?farolas (+ ?nivel 1))
	(bind ?*nod-gen* (+ ?*nod-gen* 1))

)
(defrule rellenar
	(declare (salience 15))
	(robot ?x1 ?x2 ?bomb farolas $?farolas prof ?nivel)
	(almacen ?x1 ?x2)
	(profundidadMax ?prof)
	(test (< ?nivel ?prof))
	=>
	(assert (robot ?x1 ?x2 3 farolas $?farolas prof (+ ?nivel 1)))
	(bind ?*nod-gen* (+ ?*nod-gen* 1))
)
(defrule reparar 
	(declare (salience 30))
	(robot ?x1 ?x2 ?bomb farolas $?farolas prof ?nivel)
	(profundidadMax ?prof)
	(test (< ?nivel ?prof))
	;;(test (member$(create$ ?x1 (+ ?x2 1) $?farolas)))
	(or
	(robot ?x1 ?x2 ?bomb farolas $?resto1 far ?x1 (+ ?x2 1) ?bombFar $?resto2)
	(robot ?x1 ?x2 ?bomb farolas $?resto1 far ?x1 (- ?x2 1) ?bombFar $?resto2)
	(robot ?x1 ?x2 ?bomb farolas $?resto1 far (+ ?x1 1) ?x2 ?bombFar $?resto2)
	(robot ?x1 ?x2 ?bomb farolas $?resto1 far (- ?x2 1) ?x2 ?bombFar $?resto2)
	)
	(test(<= ?bomb ?bombFar))
	=>
	(assert (robot ?x1 ?x2 (- ?bomb ?bombFar) farolas $?resto1 $?resto2))
	(bind ?*nod-gen* (+ ?*nod-gen* 1))
)	

(defrule inicio 
        (reset)
	(printout t "Profundidad Maxima:= " )
    	(bind ?prof (read))
	(printout t "Tipo de Busqueda " crlf "    1.- Anchura" crlf "    2.- Profundidad" crlf )
	(bind ?a (read))
	(if (= ?a 1)
	       then    (set-strategy breadth)
	       else   (set-strategy depth))
	(assert profundidadMax ?prof)
        
	)

(defrule final
	(declare (salience 100))
	(robot ?x1 ?x2 0 farolas)
	=>
	(printout t "Se llego al final")
	(halt)
)