#!/usr/bin/env python
# encoding: utf-8

#Hacer un programa que copie las primeras dos líneas del archivo de (a)
#"a otro archivo "dos.txt"

#Modo leectura
f = open('/home/andres/Dropbox/Curso programacion/archivos/archivo.py', 'r')
#Modo escritura
o = open('/home/andres/Dropbox/Curso programacion/archivos/2.py', 'w')
# Lee las primeras 2 lineas

r = f.readline()
r1 = f.readline()
#Escribe las dos lineas
o.write (r1)
o.write (r)

f.close()
o.close()

