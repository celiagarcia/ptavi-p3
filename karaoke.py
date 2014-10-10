#!/usr/bin/python
# -*- coding: utf-8 -*-
#CELIA GARCIA FERNANDEz


from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
import os


if __name__ == "__main__":

    parser = make_parser()
    small = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(small)
    
    try:
        fich = open(sys.argv[1],'r')       
    except IOError:
	    print "Usage: python karaoke.py file.smil"
	    raise SystemExit
	        
    parser.parse(fich)
    lista = small.get_tags()
                    
    #de romoto a local                
                    
    for diccionario in lista:              
        for etiqueta in diccionario:
            if diccionario[etiqueta].find("http://") == 0:
                recurso = diccionario[etiqueta]
                os.system("wget -q " + recurso)
                nuevo = diccionario[etiqueta].split('/')[-1]
                diccionario[etiqueta] = nuevo

            
                    
    #imprimir lista                
    for diccionario in lista:
        print diccionario["name"],
        for etiqueta in diccionario:
            if diccionario[etiqueta] and etiqueta != "name":
                 print "\t" + etiqueta + '="' + diccionario[etiqueta] + '"',
        print            
            
            
            
            
            
            

