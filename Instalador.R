#! /usr/bin/env Rscript

### Instalando y cargadndo librerias ###

librerias <- c("ggplot2", "dbscan", "factoextra", "fpc", "telegram.bot", "reticulate")
for(i in 1:length(librerias)){
  if(!librerias[i] %in% installed.packages()){install.packages(librerias[i])}
}

### Configurando el ambiente de python ###

paquetes <- dir("~/.local/share/r-miniconda/envs/r-reticulate/lib/python3.6/site-packages/")
python <- c("cv2", "numpy", "PIL", "imageio", "shutil", "pandas", "csv")

for(i in 1:length(python)){
  if(!python[i] %in% paquetes){py_install(python[i], pip = TRUE)}
}


### Creando carpeta y configurando el sitio de trabajo ###

ruta <- getwd()

dir.create(paste(ruta, "Fotos", sep = "/"))
dir.create(paste(ruta, "Registro", sep = "/"))
dir.create(paste(ruta, "Registro2", sep = "/"))
dir.create(paste(ruta, "Resultados", sep = "/"))
dir.create(paste(ruta, "Salidas", sep = "/"))
dir.create(paste(ruta, "imagenes", sep = "/"))

system(paste("chmod +x", paste(ruta, "procesamiento.py", sep = "/"), sep = " "))
system(paste("chmod +x", paste(ruta, "procesamiento.R", sep = "/"), sep = " "))

