#! /usr/bin/env Rscript

system("sudo apt install libcurl4-openssl-dev libssl-dev inotify-tools -y")

### Instalando y cargadndo librerias ###

librerias <- c("ggplot2", "dbscan", "factoextra", "fpc", "telegram.bot", "reticulate")
for(i in 1:length(librerias)){
  if(!librerias[i] %in% installed.packages()){install.packages(librerias[i])}
}

system("wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh")
system("chmod +x https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh")
system("./Miniconda3-latest-Linux-x86_64.sh")

library(reticulate)

### Configurando el ambiente de python ###

paquetes <- c("opencv-python", "numpy", "Pillow", "imageio", "pandas")

for(i in 1:length(paquetes)){
  if(py_module_available(paquetes[i])==F){py_install(paquetes[i], pip = TRUE)}
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
system(paste("chmod +x", paste(ruta, "inicio.sh", sep = "/"), sep = " "))

