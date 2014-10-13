#!/usr/bin/python
# -*- coding: utf-8 -*-
#CELIA GARCIA FERNANDEz


from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
import os


class KaraokeLocal():

        def __init__(self, fich):
            parser = make_parser()
            small = smallsmilhandler.SmallSMILHandler()
            parser.setContentHandler(small)
            parser.parse(fich)
            self.lista = small.get_tags()

        def __str__(self):
            salida = ""
            for diccionario in self.lista:
                salida += diccionario["name"]
                for etiqueta in diccionario:
                    if diccionario[etiqueta] and etiqueta != "name":
                        salida += "\t" + etiqueta + '="'
                        salida += diccionario[etiqueta] + '"'
                salida += "\n"
            return salida

        def do_local(self):
            for diccionario in self.lista:
                for etiqueta in diccionario:
                    if diccionario[etiqueta].find("http://") == 0:
                        recurso = diccionario[etiqueta]
                        os.system("wget -q " + recurso)
                        nuevo = diccionario[etiqueta].split('/')[-1]
                        diccionario[etiqueta] = nuevo

if __name__ == "__main__":

    try:
        fich = open(sys.argv[1], 'r')
    except IOError:
        sys.exit("Usage: python karaoke.py file.smil")
    except IndexError:
        sys.exit("Usage: python karaoke.py file.smil")

    karaoke = KaraokeLocal(fich)
    print karaoke
    karaoke.do_local()
    print karaoke
