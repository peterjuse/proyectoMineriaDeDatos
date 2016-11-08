#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
_____________________________________________________________________________________________________

									PROYECTO DE MINERIA DE DATOS
								  ESTUDIANTE: PEDRO LUIS BOLL LUGO
											CI: 20173376											
_____________________________________________________________________________________________________

La Escuela de Computación de la Universidad Central de Venezuela necesita un método eficiente para
asignar la mención de las TEG que fueron publicadas antes de que existiera el sistema de ficheros y
organización actual. Para ello se han entregado datos de varias TEG que se encuentran en el sistema 
actual de la escuela. Dichas TEG vienen con la siguiente información:
	* Titulo
	* Resumen
	* Palabras Claves
	* Mención
Se desea que dado unicamente el titulo, resumen y palabras claves de una TEG se pueda predecir la 
mención a la que debe pertenecer dicho TEG. En algunas menciones hay pocas apariciones de TEG y no 
proporcionan datos útiles para la mineria, por lo que se limitará la minería a las siguientes 
menciones:
	* Aplicaciones en Internet
	* Base de Datos
	* Inteligencia Artificial
	* Sistemas de Información
	* Tecnologías de Comunicación y Redes de Computadoras

----------------------------------------------------------------------------------------------
FASE 1:
Para la primera fase se requiere que se haga todo el pre-procesamiento de los datos,
esto incluye, limpieza, reducción y transformación de datos. Para esta fase se debe entregar:
	*Un documento que explique todos los pasos tomados para preprocesar los datos.
	*Si se utilizó alguna herramienta para el preprocesamiento, es necesario señalar en el 
	documento que herramienta se utilizó.
	*Si se implemento algún código para preprocesar debe incluirse el codigo fuente.
	*Los archivos resultantes de hacer el preprocesamiento.

Fecha de Entrega: 12/10/2016
-----------------------------------------------------------------------------------------------
"""

#######################################################
#	REQUERIMIENTOS:
#	Para hacer funcionar el proyecto, se debe instalar:
#	* antiword 
#		sudo apt-get install antiword
#	Para los paquetes y librerias de Python usar el 
#	siguiente comando:
#	pip install textract numpy pandas nltk
#	Para pode correr correctamente el nlkt se debe hacer en un python shell
#	los siguientes comandos:
#	import nlkt
#	nlkt.download() y bajar los paquetes de uso 
#######################################################

#	Librerias
import textract
import numpy
import pandas as pd
import csv
import time as t
from pprint import pprint
from utiles import *
#	Nota, si se va imprimir usar .encode('utf-8'))

"""
-----------------------------------------------------------------------
	Proceso de Obtenencion y procesado del texto del documento .doc    
-----------------------------------------------------------------------
"""

#	Se abre el documento con las tesis y se extrae el texto a un string
docWord = textract.process('datos/Datos_proyecto.doc')
#	Se remplazan los fin de linea por caracteres identificables
#	y se tratan los casos especiales de tesis por seeparar.
docWord = docWord.replace("',\n\n'","'\n\n").replace(')\'\n\n\n',')\'~')
docWord = docWord.replace(".\'\n\nT",".\'T").replace("n.\n\nS","n. S")
docWord = docWord.replace("T\'\n\'T","T.\',\'T")
docWord = docWord.replace(')\',\n\n\n',')\'~').replace('\',\n\n','\',')
docWord = docWord.replace('\n\n','~').replace('~\n','~').replace('~~','~')
#   Se remplazan los delimitadores para hacer split posteriormente
docWord = docWord.replace("\n",'').replace("\',",'@').replace('\'','').replace('.TRABA', '.@TRABA')
docWord = docWord.replace("TRABAJO ESPECIAL DE GRADO (","").replace(")","")
#   Remplazando aquellas filas que varien la clasificacion
docWord = docWord.replace("TECNOLOGIA EDUCATIVA","TECNOLOGIAS EDUCATIVAS")
docWord = docWord.replace("TECNOLOGIAS DE LA COMUNICACIÓN Y REDES DECOMPUTADORES","TECNOLOGIAS EN COMUNICACIONES Y REDES DECOMPUTADORAS")
docWord = docWord.replace("INGENIERA DE SOFTWARE","INGENIERIA DE SOFTWARE")
docWord = docWord.replace(" TECNOLOGIAS EN COMUNICACIONES Y REDES DECOMPUTADORAS","TECNOLOGIAS EN COMUNICACIONES Y REDES DECOMPUTADORAS")
docWord = docWord.replace("APLICACIONES EN INTERNET","APLICACIONES INTERNET")
docWord = docWord.replace("BASE DE DATOS","BASES DE DATOS")
docWord = docWord.lower()
docWord = docWord.replace("\'",'#').replace('\"','#').replace(',',' ').replace('.','').replace('-','').replace(';',' ')
#	Se separa el string por el doble salto de linea para obtener cada tesis por separado
#	Se crea una lista con los elementos obtenidos
docWord = docWord.split('~')

# 	Quito la cabecera del titulo, descripcion, palabras claves y el area de la tesis
for i in range(0,4):
	docWord.pop(0)
tesis = []
#	Separo cada una de las tesis que hay en la lista que viene del doc de word
for i in docWord:
	tesis.append(i.split('@'))

#	Elimino las filas que poseen mas de 4 elementos por la dificultad de tratamiento
#	y se agrega un elemento Nulo a aquellos que no poseen palabras clave
for i in tesis:
	if len(i)>4:
		tesis.remove(i)
	if len(i)==3:
		palabras = " ".join(keywords(i[1]))
		#for j in palabras:
		#	print j.encode('utf-8')
		#print "-------------------------------------------------------"
		#print type(palabras)
		i.insert(2,palabras)

"""
-------------------------------------------------------------
	Proceso de procesado de los 4 elementos de cada tesis
-------------------------------------------------------------
"""

#   Opciones para subir dataframes a partir de una lista de lista
headers = ['Titulo de tesis','resumen', 'palabras clave','mencion'] 
df = pd.DataFrame(tesis,columns=headers)
#df.ix[226,'mencion'] = "aplicaciones internet"
#df.ix[226,'palabras clave'] = " ".join(keywords(df.ix[226,'resumen']))
df.to_csv('datos/salida.csv',encoding="utf-8",index=True)


#	Otro procesado de elementos para crear un dataframe transaccional
headers= ['mencion','keyword']
elem = []
for index, row in df.iterrows():
	kw = row['palabras clave'].replace('(','').split(" ")
	mencion = row['mencion'] 
	for i in kw:
		if i!="":
			elem.append([mencion,i])
newdf = pd.DataFrame(elem,columns=headers)
newdf.to_csv('datos/trans.csv',encoding='utf-8',index=False)