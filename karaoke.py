#!/usr/bin/python
# -*- coding: utf-8 -*-
#CELIA GARCIA FERNANDEz


from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys




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
    print small.get_tags()
