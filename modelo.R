setwd("~/Escritorio/UNIVERSIDAD/proyectoMineriaDeDatos/")
library(arules)

diccionario = c('central','consiste','herramienta','manejo','ello','permitan',
                '20','a','adémas','de','manera','en','forma','cada','facultad',
                'más','ser','y','debido','través','mayor','ciencias','también',
                'ucv','uso','cabo','vez','puede','pueden','éL','la','lo','los',
                'las','así','el','del','una','un','desarrollo','trabajo','para',
                'sistema','gran', 'docentes','ejemplo','está','launiversidad',
                'usando','lafacultad','poder','tipo','según','debe','diferentes',
                'dela','profesores','dentro','punto','necesidades','escuela',
                'bajo','hace','utilizando','postgrado','mismos','estudios','hacia',
                'tener','permita','fin','venezuela','presenta','personal',
                'presente','además','grado'
                )

df<- read.csv("datos/trans.csv")
trx <- df
trx <- trx[ ! trx$keyword %in% diccionario,]

trx <- split(trx$mencion,trx$palabras.clave)
trx <- as(trx,"transactions")
inspect(trx)

trx
colnames(trx)

reglas <- apriori(trx, parameter=list(support=0.0005, confidence = 0.0125,minlen=2)) #support = 0.001 y confidence = 0.0125 da bien
summary(reglas)
inspect(reglas)

# imprime las 3 reglas con mayor confianza
reglas <-sort(reglas, by="confidence", decreasing=TRUE) # ordena regla 
inspect(head(reglas,25))


