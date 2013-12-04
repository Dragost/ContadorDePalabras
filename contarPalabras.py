# coding: utf-8


import sys
import easygui
import os

os.chdir("C:\AppServ\www\cgi-bin\ContadorDePalabras")

f = open('ej30.py')
contenido = f.read()

print "***********************"
print "este es el contenido"
print "***********************"

print contenido

palabras = contenido.split()

print "***************************"
print "estas son las palabras"
print "***************************"

for palabra in palabras:
    print palabra

dicc_pal = {}

for palabra in palabras:
    veces = dicc_pal.get(palabra, 0)
    dicc_pal[palabra] = veces + 1
    
print "******************************************"
print "diccionario de palabras con contador"
print "******************************************"

print dicc_pal
    
print "********************************************************************"
print "diccionario de palabras con contador, solo las que mas se repiten"
print "********************************************************************"

n = 0
for palabra in dicc_pal:
    if veces > 1:
        print dicc_pal.get(palabra, veces)
    