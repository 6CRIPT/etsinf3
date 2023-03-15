#!/usr/bin/env python
#! -*- encoding: utf8 -*-

# 1.- Pig Latin

#Hecho por César Martínez Chico, grupo 3CO11
import re
import sys
from typing import Optional, Text
from os.path import isfile

consonantes = set("bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ") #conjunto de consonantes
vocales = set("aeiouyAEIOUY") # conjunto de vocales (y es una vocal en este caso)

class Translator():

    def __init__(self, punt:Optional[Text]=None):
        """
        Constructor de la clase Translator

        :param punt(opcional): una cadena con los signos de puntuación
                                que se deben respetar
        :return: el objeto de tipo Translator
        """
        if punt is None:
            punt = ".,;?!"
        self.re = re.compile(r"(\w+)([" + punt + r"]*)")

    def translate_word(self, palabra:Text) -> Text:
        """
        Recibe una palabra en inglés y la traduce a Pig Latin

        :param word: la palabra que se debe pasar a Pig Latin
        :return: la palabra traducida
        """
        
        aux = list(palabra) #la paso a lista para poder manejar la palabra mejor y poder iterarla.
        mayuscula = False # boolean para mas tarde comprobar si la primera letra es mayuscula.
        res = aux[:] #copia para guardar el resultado. Esto lo hago porque iterar aux a la vez que se modifica es peligroso.
        primeraLetra = aux[0] #obtengo la primera letra
        if(primeraLetra.isupper()): #compruebo que sea mayuscula
            mayuscula = True
        if(primeraLetra in vocales):
            res = res + ['y', 'a', 'y'] #si la primera letra es vocal, sencillamente concateno 'yay' y perfecto
            #print(res)
        elif(primeraLetra in consonantes):
            for letra in range(len(aux)): #si es consonante, itero para mover todas las consonantes hasta la primera vocal al final.
                if(aux[letra] in consonantes): 
                    mover = res.pop(0) #obtengo la palabra. Esta orden es la razon de que haya creado la lista res.
                    #print(mover)
                    res.append(mover)#lo pongo al final de la palabra
                    #print(res)
                elif(aux[letra] in vocales):
                    res = res + ['a', 'y']
                    #print(res)
                    break #si llego a la vocal dejo de iterar la palabra
                else: #si no es ni consonante ni vocal
                    pass
        res = ''.join(res) #ahora la lista res la paso a cadena.
        if(mayuscula):
            res = res.capitalize() #si la primera letra era mayuscula, pues la palabra resultado tambien debe ir en mayuscula
        new_word = res # SUSTITUIR ESTA PARTE
        
        return new_word

    def translate_sentence(self, sentence:Text) -> Text:
        """
        Recibe una frase en inglés y la traduce a Pig Latin

        :param sentence: la frase que se debe pasar a Pig Latin
        :return: la frase traducida
        """
        
         #si todo esta en mayusuculas, utilizare este bool para pasarlo todo a mayusculas al final
        
        lista = sentence.split() #muy importante, quito los espacis al principio y al final, esto evita errores si la cadena por ejemplo es "   hola"
        #print(lista)
        final = lista[:] #igual que antes, la creo para iterar la lista sin miedo a errores por ir modificandola
        finalIndice = 0 #indice
        for palabra in lista:
            todoMayusculas = False #boolean que usare para ver si toda la palabra estaba en mayuscula
            if (palabra.isupper()):
                todoMayusculas = True #todo mayuscula -> True
            palabra = self.re.findall(palabra) #expresion regular
            try:
                nuevaP = self.translate_word(palabra[0][0]) #traduzco la primera palabra
            except(IndexError):
                pass
            if (todoMayusculas):
                nuevaP = nuevaP.upper() #si la palabra estaba en mayusculas, entonces la palabra resultado la pongo todo a mayuscula
            try:
                final[finalIndice] = nuevaP + palabra[0][1] #concateno los caracteres de puntuacion ?!., etc
            except(IndexError):
                pass
            
            
            finalIndice+=1 #incremento
        final = ' '.join(final) #convierto el resultado final a cadena
        

        new_sentence = final # SUSTITUIR ESTA PARTE

        return new_sentence

    def translate_file(self, filename:Text):
        """
        Recibe un fichero y crea otro con su tradución a Pig Latin

        :param filename: el nombre del fichero que se debe traducir
        :return: None
        """
        
        if not isfile(filename):
            print(f'{filename} no existe o no es un nombre de fichero', file=sys.stderr)
        else:
            with open (filename, encoding='utf-8') as f:
                lineas = f.readlines() #me abro el archivo en lineas.
            nuevoF = list(filename) #me creo una lista 
            nuevoNombre = "" #aqui guardare el nuevo nombre del archivo
            for i, char in enumerate(nuevoF):
                if(nuevoF[i] == '.'): #busco el formato
                    nuevoNombre = nuevoF[:i] #a partir del . va el formato, entonces, me guardo todo lo que va antes como el nuevo nombre
            nuevoNombre = ''.join(nuevoNombre) + "_latin.txt" # y aqui le concateno el nuevo prefijo.
            
            with open (nuevoNombre, 'w') as nF:
                for linea in lineas: #itero las lineas
                    nLinea = self.translate_sentence(linea) #y las voy traduciendo frase a frase.
                    nF.write(nLinea + '\n') #por utlimo la guardo en el archivo resultado.
        

        

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print(f'Syntax: python {sys.argv[0]} [filename]')
        exit()
    t = Translator()
    if len(sys.argv) == 2:
        t.translate_file(sys.argv[1])
    else:
        sentence = input("ENGLISH: ")
        while len(sentence) > 1:
            print("PIG LATIN:", t.translate_sentence(sentence))
            sentence = input("ENGLISH: ")
