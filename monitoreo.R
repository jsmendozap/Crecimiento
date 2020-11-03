#! /usr/bin/env Rscript

archivos <- length(dir("/data/data/com.termux/files/home/storage/dcim/Camera"))
destino <- "usuario@ip:~/Crecimiento/Fotos/"

if (archivos == 1){
  nombre <- dir("/data/data/com.termux/files/home/storage/dcim/Camera")
  ruta1 <- paste("/data/data/com.termux/files/home/storage/dcim/Camera", nombre, sep = "/")
  envio <- paste("#! /usr/bin/bash \nscp", ruta1, destino, sep = " ")
  system("echo '#! /usr/bin/bash' > prueba.sh")
  writeLines(envio, con = "prueba.sh", sep = "\n")
  system("chmod +x prueba.sh")
  system("./prueba.sh")
  system("rm prueba.sh")
  borrar <- paste("rm", ruta1, sep = " ")
  system(borrar)
  #system("./movido.sh")
}


