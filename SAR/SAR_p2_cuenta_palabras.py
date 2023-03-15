#! -*- encoding: utf8 -*-

## Nombres: César Martínez Chico

########################################################################
########################################################################
###                                                                  ###
###  Todos los métodos y funciones que se añadan deben documentarse  ###
###                                                                  ###
########################################################################
########################################################################

import argparse
import os
import re
from typing import Optional
import pathlib
import operator
from collections import defaultdict
import sys

def sort_dic_by_values(d:dict) -> list:
    return sorted(d.items(), key=lambda a: (-a[1], a[0]))

class WordCounter:

    def __init__(self):
        """
           Constructor de la clase WordCounter
        """
        self.clean_re = re.compile('\W+')

    def write_stats(self, filename:str, stats:dict, use_stopwords:bool, full:bool):
        """
        Este método escribe en fichero las estadísticas de un texto
            
        :param 
            filename: el nombre del fichero destino.
            stats: las estadísticas del texto.
            use_stopwords: booleano, si se han utilizado stopwords
            full: boolean, si se deben mostrar las stats completas
        """

        with open(filename, 'w', encoding='utf-8', newline='\n') as fh:
            #lineas para escribir las estadisticas en el file
            fh.write('Lineas: '+str(stats['nlines'])+'\n')
            fh.write('Numero de palabras incluyendo stopwords: '+str(stats['nwords'])+'\n')
            if use_stopwords: #si elegimos la opcion de sin stopwords...
                fh.write('Numero de palabras sin stopwords): ' + str(stats['vocab']) + '\n')
            fh.write('Tamaño del vocabulario:' + str(stats['vocabs'])+'\n')
            fh.write('Número de símbolos' + str(stats['nsymbols'])+'\n')
            fh.write('Número de símbolos diferentes' + str(stats['nsymbolsd'])+'\n')


            fh.write('Palabras en orden alfabetico: '+'\n')
            dicw = sorted(stats['word'].items(), key=operator.itemgetter(0), reverse=False) #creamos la lista de palabras ordenada
            j = 0
            for a in dicw: #iteramos la lista
                fh.write("\t" + str(a[0]) + ": " + str(a[1]) + '\n') #escribimos la palabra 
                j = j + 1
                if not full and j >= 20:
                    break

            fh.write('Palabras ordenadas por frecuencia: ' + '\n') 
            dicw = sorted(stats['word'].items(), key=lambda a:(-a[1],a[0])) #otro diccionario, para las palabras ordenadas por frecuencia
            j = 0
            for a in dicw: #lo iteramos
                fh.write("\t" + str(a[0]) + ": " + str(a[1]) + '\n') #escribimos... no comentare más porque es igual para todas las estadisticas
                #abrir en un diccionario, iterarlo y escribir.
                j = j + 1
                if not full and j >= 20:
                    break
                
            fh.write('Simbolos ordenados en orden alfabetico: ' + '\n')
            dics = sorted(stats['symbol'].items(), key=operator.itemgetter(0), reverse=False)
            j = 0
            for a in dics:
                fh.write("\t" + str(a[0]) + ": " + str(a[1]) + '\n')
                j = j + 1
                if not full and j >= 20:
                    break

            fh.write('Simbolos ordenados por frecuencia ' + '\n')
            dics = sorted(stats['symbol'].items(), key=lambda a:(-a[1],a[0]))
            j = 0
            for a in dics:
                fh.write("\t" + str(a[0]) + ": " + str(a[1]) + '\n')
                j = j + 1
                if not full and j >= 20:
                    break
            
            if stats['bi']: #comprobamos que teniamos marcada la opcion de bigramas y procedemos de forma basicamente analoga a lo anterior, para escribir simbolos y palabras
                fh.write('Bigramas por orden alfabetico): ' + '\n')
                dicw = sorted(stats['biword'].items(), key=operator.itemgetter(0), reverse=False)
                j = 0
                for a in dicw:
                    fh.write("\t" + str(a[0]) + ": " + str(a[1]) + '\n')
                    j = j + 1
                    if not full and j >= 20:
                        break

                fh.write('Bigramas por frecuencia: ' + '\n')
                dicw = sorted(stats['biword'].items(), key=lambda a:(-a[1],a[0])) 
                j = 0
                for a in dicw:
                   fh.write("\t" + str(a[0]) + ": " + str(a[1]) + '\n')
                   j = j + 1
                   if not full and j >= 20:
                       break
                   
                fh.write('Pares de simbolos en orden alfabetico: ' + '\n')
                dics = sorted(stats['bisymbol'].items(), key=operator.itemgetter(0), reverse=False)
                j = 0
                for a in dics:
                    fh.write("\t" + str(a[0][0]) + str(a[0][1]) + ": " + str(a[1]) + '\n')
                    j = j + 1
                    if not full and j >= 20:
                        break

                fh.write('Pares de simbolos por frecuncia: ' + '\n')
                dics = sorted(stats['bisymbol'].items(), key=lambda a:(-a[1],a[0]))
                j = 0
                for a in dics:
                    fh.write("\t" + str(a[0][0]) + str(a[0][1]) + ": " + str(a[1]) + '\n')
                    j = j + 1
                    if not full and j >= 20:
                        break


    def file_stats(self, fullfilename:str, lower:bool, stopwordsfile:Optional[str], bigrams:bool, full:bool):
        """
        Este método calcula las estadísticas de un fichero de texto

        :param 
            fullfilename: el nombre del fichero, puede incluir ruta.
            lower: booleano, se debe pasar todo a minúsculas?
            stopwordsfile: nombre del fichero con las stopwords o None si no se aplican
            bigram: booleano, se deben calcular bigramas?
            full: booleano, se deben montrar la estadísticas completas?
        """

        stopwords = [] if stopwordsfile is None else open(stopwordsfile, encoding='utf-8').read().split()

        # variables for results

        estad = { #todas las estadisticas
                'nwords': 0, #numero de palabras incluyendo stpowords
                'vocab': 0, #numero de palabras sin stopwords.
                'vocabs' : 0, #tamaño del vocabulario
                'nsymbols' : 0, #numero de simbolos
                'nsymbolsd' : 0, #numero de simbolos diferentes.
                'nlines': 0, #numero de lineas
                'word': {}, #palabras
                'symbol': {}, #simbolos
                'bi' : False #la opcion que detectara si queremos bigramas o no, por defecto false, se pone a true en if bigramas
                }
        estadW = {} #diccionario vacio

        estadS = {} #diccionario vacio

        if bigrams:
            estad['biword'] = {}
            estad['bisymbol'] = {}
            estad['bi'] = True
        biw = {} 
        bis = {} 
        
        ultimaP = "$"
        pd = []
        sd = []  
        
        archivo = open(fullfilename, 'r', encoding='utf8')

        for lin in archivo: #recorremos las lineas del archivo en bucle para ir analizando 1 a 1 cada linea
            if lower:
                lin = lin.lower() 
            #lin = ''.join(filter(str.isalnum, lin)) #quitamos los noo alfanumericos
            lin = self.clean_re.sub(' ', lin)
            ultimaP = "$"

            for palabra in lin.split(): #ahora iteremos las palabras de cada linea
                if stopwords != [] and stopwords.count(palabra) != 0:  
                    estad['vocabs'] -= 1

                if palabra not in pd:
                    estad['vocabs'] += 1  #incrementamos contador 
                    
                estadW[palabra] = estadW.get(palabra,0) + 1   #añadimos la palabra al diccionario correspondiente, si ya estuviera incrementamos... 
                pd.append(palabra)
                estad['nwords'] += 1 #incrementamos el numero de palabras
                estad['vocab'] += 1  #incrementamos las palabras sin las stopwords. 
                 

                if bigrams: #si hemos elegido bigramas...
                    biw[ultimaP + " " + palabra] = biw.get(ultimaP + " " + palabra,0) + 1 
                    ultimaP = palabra

                    #contamos los bigramas...
                for letra in palabra: #iteramos las letras dentro de cada palabra.
                    if letra not in sd:
                        estad['nsymbolsd'] += 1  #incrementamos contador de simbolos distintos.
                    estadS[letra] = estadS.get(letra,0) + 1 #añadimos al diccionario, si no estuviera, y si está: incrementamos, como antes
                    sd.append(letra)
                    #contar letras 
                    estad['nsymbols'] += 1
                if bigrams: #bigramas
                    for i in range(len(palabra) - 1):
                        w1, w2 = palabra[i : i + 2]
                        bis[(w1,w2)] = bis.get((w1,w2), 0) + 1
                    #obtener los bigramas (pares de simbolos)

            if ultimaP != "$": #si no tiene el simbolo $
                biw[ultimaP + " $"] = biw.get(ultimaP + " $", 0) + 1
                
            estad['nlines'] += 1 #incrementamos 

        estad['word'] =estadW
        estad['symbol'] = estadS
        estad['biword']  = biw  
        estad['bisymbol']  = bis     

       
        # completar
        exten = pathlib.Path(fullfilename).suffix
        nuevonom = fullfilename[:len(fullfilename) - len(exten)] + "_" 
        stop = False
        if stopwordsfile:
            stop = True
         
        count = 0
        
        if lower:
            nuevonom = nuevonom + 'l'
            count = count + 1
        if stop:
            nuevonom = nuevonom + 's'
            count = count + 1
        if bigrams:
            nuevonom = nuevonom + 'b'
            count = count + 1
        if full:
            nuevonom = nuevonom + 'f'
            count = count + 1
        if count > 0:
            nuevonom = nuevonom + '_stats' + exten
        else: 
            nuevonom = nuevonom + 'stats' + exten
        
        new_filename =  open(nuevonom, "w", encoding="utf8")# cambiar
        self.write_stats(nuevonom, estad, stopwordsfile is not None, full)


    def compute_files(self, filenames:str, **args):
        """
        Este método calcula las estadísticas de una lista de ficheros de texto

        :param 
            filenames: lista con los nombre de los ficheros.
            args: argumentos que se pasan a "file_stats".

        :return: None
        """

        for filename in filenames:
            self.file_stats(filename, **args)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Compute some statistics from text files.')
    parser.add_argument('file', metavar='file', type=str, nargs='+',
                        help='text file.')

    parser.add_argument('-l', '--lower', dest='lower',
                        action='store_true', default=False, 
                        help='lowercase all words before computing stats.')

    parser.add_argument('-s', '--stop', dest='stopwords', action='store',
                        help='filename with the stopwords.')

    parser.add_argument('-b', '--bigram', dest='bigram',
                        action='store_true', default=False, 
                        help='compute bigram stats.')

    parser.add_argument('-f', '--full', dest='full',
                        action='store_true', default=False, 
                        help='show full stats.')

    args = parser.parse_args()
    wc = WordCounter()
    wc.compute_files(args.file,
                     lower=args.lower,
                     stopwordsfile=args.stopwords,
                     bigrams=args.bigram,
                     full=args.full)
