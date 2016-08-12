#!/usr/bin/env python
# -*- coding: utf-8 -*-

# instalar antiword y el paquete de python textract
import textract
import pprint

docWord = textract.process('datos/Datos_proyecto.doc')
docWord = docWord.split(',')
for i in range(0,4):
	docWord.pop(0)
print docWord