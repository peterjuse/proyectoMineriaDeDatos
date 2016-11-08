#!/usr/bin/2env python
# -*- coding: utf-8 -*-

"""
_____________________________________________________________________________________________________

									PROYECTO DE MINERIA DE DATOS
								  ESTUDIANTE: PEDRO LUIS BOLL LUGO
											CI: 20173376											
_____________________________________________________________________________________________________

FUNCIONES UTILES PARRA EL PROYECTO

Este archivo es para colocar aquellas funciones utiles para el proyecto, incluyendo ambas fases del
mismo permitiendo la correcta ejecucion del mismo.

"""

#	Nota, si se va imprimir usar .encode('utf-8')
import nltk 
from nltk.corpus import stopwords


def keywords(descripcion):
	"""
	Funcion que recibe un string con la descripcion de una tesis. Retorna las palabras mas utilizadas
	para agregarlas al dataframe

	"""
	stop = set(stopwords.words('spanish'))	
	simbolos = {'(',':','#','d','8','10', '6','[',']','n°'}

	diccion = { 'central','consiste','herramienta','manejo','ello','permitan','20','a','adémas','de','manera','en',
	'forma','cada','facultad','más','ser','y','debido',u'trav\xe9s','mayor','ciencias','tambiÉn','ucv','uso','cabo','vez',
	'puede','pueden',u'\xe9l','la','lo','los','las','así','el'
		} 
	
	descripcion = [i for i in descripcion.lower().split() if i not in stop]
	descripcion = " ".join(descripcion)
	descripcion = nltk.tokenize.word_tokenize(descripcion.decode('utf-8'))
	
	frecuencia =  nltk.FreqDist(descripcion)
	keywords = frecuencia.most_common(50)	
	keywords = [w[0] for w in keywords if w[0] not in simbolos]
	keywords = [x for x in keywords if x not in diccion]
	print keywords
	print "\n"
	return keywords
