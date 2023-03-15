'''
NOTAS:
1)Al final de cada ejercicio hay un comentario con una llamada a la ejecucion de ese ejercicio, para pruebas. 
2)Casi todos los ejercicios tienen valores por defecto en los argumentos, menos el 4
3)Suelo modificar los argumentos pero copiandolos en otra variable (ejemplo: cadena -> cadena2 = cadena.loquesea()) esto lo hago para los print,
lo entenderá con el primer ejercicio lo que quiero decir con esto.
4)Aunque en algun ejercicio especifican como ha de llamarse la funcion, a todas les he llamado ejerX, siendo X el numero del ejercicio, por simplicidad.

Hecho por César Martínez Chico, grupo 3CO11
'''
from collections import Counter
import string

def ejer1 (cadena="The quick brown fox jumps over the lazy dog"): #valor por defecto simplemente para hacer pruebas, por si se invoca sin argumentos.
    cadena2 = set(cadena.lower()) #paso la cadena a minusculas y la convierto en un conjunto
    #la unica razon por la que creo una cadena2 es para el print del final, que no imprima una coleccion sino la cadena
    comprobar = set(string.ascii_lowercase) #me convierto en un conjunto todas las letras del abecedario inglés
    res = (cadena2 & comprobar == comprobar) #explicacion debajo
    '''
    Primero hago la interseccion entre ambos conjuntos. Para que esto devuelva True
    a cadena deberá contener todos los elementos del abecedario alguna vez.
     Como los espacios no estan en el abecedario, al hacer la interseccion se descartan automaticamente
    '''
    print("---------------------------------------------------------")
    print()
    print(f"¿La cadena '{cadena}' es un pangrama? --> {res} ")
    print()
    print("---------------------------------------------------------")
    return res
#ejer1()


def ejer2(cadena="zbcdefghijklmnopqrstuvwxya"):
    cadena2 = cadena.lower().replace(" ", "") #paso a minusculas y quito espacios
    fin = {} #diccionario vacio para comprobar que letras estan y cuales no, y cuantas veces aparecen

    comprobar = set(string.ascii_lowercase)

    for char in cadena2:
        if char in comprobar:
            fin[char] = fin.get(char, 0) + 1 #para cada letra de la cadena tiene su propia entrada, por cada vez que aparezca, le sumo 1 al valor de esa clave.
            
    res = all(fin.get(letra, 0)==1 for letra in comprobar)
    '''
    la idea que he tenido es una vez creado mi diccionario con todas las apariciones de cada letra
    mirar que para cada letra (si aparece tendra un valor <=1, y si no, por defecto 0, para evitar errores)
    el numero de apariciones es exactamente 1. Notese que utilizo la cadena 'comprobar' porque esa si 100% contiene todas
    entonces al comprobar cada letra del abecedario si esta o no en el diccionario no nos saltarmeos ninguna.
    '''
     

    print("---------------------------------------------------------")
    print()
    print(f"¿La cadena '{cadena}' es un pangrama perfecto? --> {res} ")
    print()
    print("---------------------------------------------------------")
    return res
#ejer2()

def ejer3(cadena1="Life, . on mars", cadena2="alieN   , . - forms"):
    cadena3 = cadena1.lower().translate(str.maketrans({key: None for key in string.punctuation})).replace(" ","")
    cadena4 = cadena2.lower().translate(str.maketrans({key: None for key in string.punctuation})).replace(" ","")
    #elimino de ambas cadenas, los espacios, los signos de puntuacion y las paso a minusculas.

    print(cadena3)
    print(cadena4)
    
    fin1 = {}
    fin2 = {} 
    #2 diccionarios, esta vez 1 para cada cadena

    for char in cadena3:
        fin1[char] = fin1.get(char, 0) + 1 #añadimos al diccionario una entrada para cada letra de la primera cadena, y contamos cuantas hay.
        
    
    for char in cadena4:
        fin2[char] = fin2.get(char, 0) + 1 #igual, contamos que letras tiene la cadena2 (transformada) y cuantas veces aparece cada letra.

    #print(fin1)  
    #print(fin2)
    #print (len(fin1), len(fin2))

    if len(fin1) == len(fin2):
        res = True
        #si el numero de entradas no fuera igual, no hay nada que hacer, puesto que una palabra tiene una letra que la otra no por tanto -> else: False 
        #se que pueda parecer que si las cadenas tienen igual longitud pero diferentes caracteres (podria ser) pasaria este if, y es verdad,
        #pero entonces las comprobaciones de abajo no las pasaria., asi que no importa realmente
        #por ejemplo para "hola" y "xola" el numero seria el mismo pero cuando comprobara el numero de entradas de la h, en la cadena 2 seria 0 entonces False.
        for char in cadena3:
            #como ya sabemos que ambas cadenas tienen el mismo numero de letras, da igual cual de las 2 iterar, 
            #porque necesitamos la letra (clave de los diccionarios)
            if (fin1.get(char, 0) != fin2.get(char, 0)):
                res = False
                break
                #comparo que si para cualquier letra el numero de apariciones es diferente, entonces ya es false.
                #la idea es que compruebe que todas son iguales, y nunca ejecute el res = False, entonces res = True.
    else:
        res = False

    
    print("---------------------------------------------------------")
    print()
    print(f"¿La cadena '{cadena1}' es un anagrama de la cadena '{cadena2}' ? --> {res} ")
    print()
    print("---------------------------------------------------------")
    return res
#ejer3("hola", "xola")

def ejer4(ruta, cadena):
    with open (ruta, encoding='utf-8') as fichero:
        lineas = fichero.readlines() #abrimos el archivo con with open y volcamos las lineas.
    res = [] #lista de resultados inicialmente vacia
    for linea in lineas:
        if cadena in linea:
            res.append(linea.strip()) #si la cadena está en la linea, la metemos en los resultados.
    print("---------------------------------------------------------")
    print()
    print(f"La cadena '{cadena}' esta en las siguientes lineas del archivo '{ruta}'  --> {res} ")
    print()
    print("---------------------------------------------------------")
    
    return res
#ejer4()

def ejer5(cadena="abbabcbd  babdbdbabababcbcbab xxy ZZZ zz"):
    cadena2 = cadena.replace(" ","") #quito espacios en blanco 
    dic = Counter(cadena2) #counter hace todo el trabajo, te saca una lista de frecuencias de las letras simplemente pasandole la cadena.
    #en este caso, he decidido diferenciar entre caracteres en mayuscula y en minuscula, ya que como no especifica, por variar.
    #en cualquier caso, si quisiera que ignorase mayusculas, como siempre, .lower() y ya.
    print("---------------------------------------------------------")
    print()
    print(f"La lista de frecuencias de la cadena '{cadena}' es -> {dic}")
    print()
    print("---------------------------------------------------------")
#ejer5()

def ejer6(cadena="[hola]"):
    contador = 0
    notFail = True
    for caracter in cadena:
        if caracter == '[':
            contador += 1
        elif caracter == ']':
            if contador == 0:
                notFail = False
            contador -= 1
    if (contador == 0):
        if (notFail):
            res = "OK"
        else: 
            res ="NOT OK"
    else: res = "NOT OK"
    print("---------------------------------------------------------")
    print()
    print(f"La lista de frecuencias de la cadena '{cadena}' es -> {res}")
    print()
    print("---------------------------------------------------------")
ejer6("[]][[]")
        
