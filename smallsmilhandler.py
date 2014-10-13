#!/usr/bin/python
# -*- coding: utf-8 -*-
#CELIA GARCIA FERNANDEz

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.lista = []
        self.etiquetas = [
            'root-layout', 'region', 'img', 'audio', 'textstream']
        self.attributosD = {
            'root-layout': ['width', 'height'],
            'region': ['id', 'top', 'left'],
            'img': ['scr', 'region', 'begin', 'dur'],
            'audio': ['src', 'begin', 'dur'],
            'textstream': ['src', 'region']
            }

    def startElement(self, name, attrs):

        diccionario = {}

        if name in self.etiquetas:
            diccionario["name"] = name
            for key in self.attributosD[name]:
                diccionario[key] = attrs.get(key, "")
            self.lista.append(diccionario)

    def get_tags(self):
        return self.lista

if __name__ == "__main__":

    parser = make_parser()
    small = SmallSMILHandler()
    parser.setContentHandler(small)
    parser.parse(open('karaoke.smil'))

    print small.get_tags()
