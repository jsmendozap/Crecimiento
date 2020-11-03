#! /usr/bin/env Rscript

system("sudo apt install libcurl4-openssl-dev libssl-dev -y")

### Instalando y cargadndo librerias ###

librerias <- c("ggplot2", "dbscan", "factoextra", "fpc", "telegram.bot", "reticulate")
for(i in 1:length(librerias)){
  if(!librerias[i] %in% installed.packages()){install.packages(librerias[i])}
}

library(reticulate)

### Configurando el ambiente de python ###

paquetes <- dir("~/.local/share/r-miniconda/envs/r-reticulate/lib/python3.6/site-packages/")
#paquetes <- dir(paste("C:/Users", strsplit(getwd(), "/")[[1]][3], "AppData/Local/r-miniconda/envs/r-reticulate/Lib/site-packages", sep = "/"))
python <- c("opencv-python", "numpy", "Pillow", "imageio", "pandas")

for(i in 1:length(python)){
  if(!python[i] %in% paquetes){py_install(python[i], pip = TRUE)}
}


### Creando carpeta y configurando el sitio de trabajo ###

ruta <- getwd()

dir.create(paste(ruta, "Fotos", sep = "/"))
dir.create(paste(ruta, "Registro", sep = "/"))
dir.create(paste(ruta, "Registro2", sep = "/"))
dir.create(paste(ruta, "Resultados", sep = "/"))
dir.create(paste(ruta, "salidas", sep = "/"))
dir.create(paste(ruta, "imagenes", sep = "/"))

system(paste("chmod +x", paste(ruta, "procesamiento.py", sep = "/"), sep = " "))
system(paste("chmod +x", paste(ruta, "procesamiento.R", sep = "/"), sep = " "))

