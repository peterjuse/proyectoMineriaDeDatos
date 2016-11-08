setwd("~/Escritorio/UNIVERSIDAD/proyectoMineriaDeDatos/")
library(arules)

df<- read.csv("datos/trans.csv")
trx <- df
trx <- split(trx$mencion,trx$palabras.clave)
trx <- as(trx,"transactions")
inspect(trx)

trx
colnames(trx)

reglas <- apriori(trx, parameter=list(support=0.01, confidence = 0.025))
summary(reglas)
inspect(reglas)
