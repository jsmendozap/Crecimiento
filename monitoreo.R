#! /usr/bin/env Rscript

args <- commandArgs(trailingOnly = TRUE)

usuario <- args[1]
ip <- args[2]
destino <- paste(usuario,"@",ip,":~/Crecimiento/Fotos/", sep = "")
archivos <- length(dir("/data/data/com.termux/files/home/storage/dcim/Camera"))

while (archivos == 1){
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
  Sys.sleep(as.numeric(args[3]))
  archivos <- length(dir("/data/data/com.termux/files/home/storage/dcim/Camera"))
}


