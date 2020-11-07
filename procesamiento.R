#! /usr/bin/env Rscript

args <- commandArgs(trailingOnly = TRUE)

library(dbscan)
library(factoextra)
library(fpc)
library(telegram.bot)
library(reticulate)
#bot <- Bot(token = "XXXXXX") 
#chat_id <- "XXXXXX"  

#py_install("<Paquete>", pip = TRUE)
ps <- import_from_path(module =  "procesamiento", path = getwd(), convert = T)

Sys.sleep(15)
ruta <- getwd()
archivo <- dir(paste(ruta,"Fotos", sep = "/"))
archivo <- archivo[1]
archivo <- paste(ruta, "Fotos", archivo, sep = "/")

#[30,120,40], [70,255,255] 
#[40,40,40], [70,255,255]  
#[20,50,59], [30,200,250] 

### Aplicando el primer procesamiento (binarización) ###

imagen <- ps$completa(archivo, c(30,35,40), c(70,255,255))

procesado <- dir(paste(ruta,"salidas", sep = "/"))
procesado <- procesado[1]
procesado <- paste(ruta, "salidas", sep = "/")

ps$altura(procesado)

### Aplicando el segundo procesamiento (Eliminación de ruido) ###

datos <- read.csv(paste(ruta, "/Resultados/coordenadas.csv", sep = "/"), sep = ",")
colnames(datos) = c("Ind", "Y", "X")
datos <- datos[,c(2,3)]
datos <- datos[,c(2,1)]

cluster <- fpc::dbscan(data = datos, eps = 30, MinPts = 50)
#Epsilon (ϵ): radio que define la región vecina a una observación, también llamada ϵ-neighborhood.
#Minimum points (minPts): número mínimo de observaciones dentro de la región epsilon.

jpeg(paste(ruta, "imagenes/cluster.jpeg", sep = "/"))
fviz_cluster(object = cluster, data = datos, stand = FALSE,
             geom = "point", ellipse = FALSE, show.clust.cent = FALSE,
             pallete = "jco") +
  theme_bw() +
  theme(legend.position = "bottom")
dev.off()
#bot$send_photo(chat_id = chat_id, photo = paste(ruta, "imagenes/cluster.jpeg", sep = "/"))

total <- vector()
longitud <- unique(cluster$cluster)
for (i in 1:length(longitud)){
  total[i] <- length(which(i == cluster$cluster))
}

indices <- which(cluster$cluster == which(total == max(total)))
datos2 <- datos[indices,]

jpeg(paste(ruta, "imagenes/corregida.jpeg", sep = "/"))
ggplot(datos2)+
  geom_point(mapping = aes(X, Y))+
  theme_bw()
dev.off()
#bot$send_photo(chat_id = chat_id, photo = paste(ruta, "imagenes/corregida.jpeg", sep = "/"))

altura <- (abs(min(datos2$Y)-max(datos2$Y)))/as.numeric(args[1])
fecha <- Sys.Date()
inf <- paste(altura, fecha, sep = ",")

### Actualizando información en BD ###

write.table(x = inf, file = paste(ruta, "Resultados/Datos.txt", sep = "/") , append = T, sep = ",", row.names = F, col.names = F, quote = F)
file.remove(paste(getwd(), "Resultados/coordenadas.csv", sep = "/"))

Mensaje <- paste("la altura calculada fue de", round(altura,2), "cm", sep = " ")
#bot$sendMessage(chat_id = chat_id, text = Mensaje)

