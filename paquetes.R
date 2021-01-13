#! /usr/bin/env Rscript

message("Por favor, seleccione que desea hacer")
message("1. Instalar paquetes")
message("2. Eliminar monitoreo de carpeta")

cat("Ingrese opción: ")
seleccion <- readLines("stdin", 1)

if (as.numeric(seleccion) == 1){
  message("Comenzando proceso de instalación de paquetes, esto puede tomar varios minutos")

  ### Instalando y cargadndo librerias ###

  librerias <- c("ggplot2", "dbscan", "factoextra", "fpc", "telegram.bot", "reticulate", "cronR")
  for(i in 1:length(librerias)){
    if(!librerias[i] %in% installed.packages()){install.packages(librerias[i])}
  }

  ### Configurando el ambiente de python ###

  library(reticulate)

  reticulate::install_miniconda()

  paquetes <- c("opencv-python", "numpy", "Pillow", "imageio", "pandas")

  for(i in 1:length(paquetes)){
    if(py_module_available(paquetes[i])==F){py_install(paquetes[i], pip = TRUE)}
  }

  ### Configurando escala

  ruta <- getwd()
  cat("Por favor ingrese el valor de la escala: ")
  escala <- readLines("stdin", 1)

  system(paste("rpl -w", "'ESCALA'", paste("'", escala, "'", sep = ""), paste(ruta, "procesamiento.R", sep = "/"), sep = " "))

  ### Configurando bot

  cat("Por favor ingrese el id de su cuenta de telegram: ")
  id <- readLines("stdin", 1)

  cat("Por favor ingrese el nombre de usuario de la cuenta de telegram: ")
  nombre <- readLines("stdin", 1)

  cat("Por favor ingrese el token del bot: ")
  token <- readLines("stdin", 1)

  system(paste("rpl -w", "'TOKENBOT'", paste("'", token, "'", sep = ""), paste(ruta, "telefono", "bot.py", sep = "/"), sep = " "))
  system(paste("rpl -w", "'IDUSER'", paste("'", id, "'", sep = ""), paste(ruta, "telefono", "bot.py", sep = "/"), sep = " "))
  system(paste("rpl -w", "'NOMBRE'", paste("'", nombre, "'", sep = ""), paste(ruta, "telefono", "bot.py", sep = "/"), sep = " "))

  system(paste("rpl -w", "'TOKENBOT'", paste("'", token, "'", sep = ""), paste(ruta, "procesamiento.R", sep = "/"), sep = " "))
  system(paste("rpl -w", "'IDUSER'", paste("'", id, "'", sep = ""), paste(ruta, "procesamiento.R", sep = "/"), sep = " "))

  ### Configurando monitoreo

  usuario <- system("whoami", intern = T)
  ip <- system("hostname -I", intern = T)

  system(paste("rpl -w", "'USUARIO'", paste("'", usuario, "'", sep = ""), paste(ruta, "telefono", "monitoreo.py", sep = "/"), sep = " "))
  system(paste("rpl -w", "'IP'", paste("'", ip, "'", sep = ""), paste(ruta, "telefono", "monitoreo.py", sep = "/"), sep = " "))

  ### Estableciendo tarea en Cron

  system("sudo systemctl enable cron")

  library(cronR)
  cmd = cron_rscript(paste(ruta, "watch.R", sep = "/"))
  cron_add(command = cmd, frequency = '@reboot', id = 'iwatch', description = 'monitorizar carpeta')

  ### Configurando área de instalación

  if (ruta != paste("/home", usuario, "Crecimiento", sep = "/")){
      if (dir.exists("~/Crecimiento") == F){dir.create("~/Crecimiento")}
      archivos <- c("procesamiento.R", "procesamiento.py", "watch.R")
      for (i in 1:3){
        file.copy(from =  paste(ruta, archivos[i], sep = "/"), to = "~/Crecimiento/")
        file.remove(archivos[i])
      }
  }

  dir.create(paste("~/Crecimiento", "Fotos", sep = "/"))
  dir.create(paste("~/Crecimiento", "Registro", sep = "/"))
  dir.create(paste("~/Crecimiento", "Registro2", sep = "/"))
  dir.create(paste("~/Crecimiento", "Resultados", sep = "/"))
  dir.create(paste("~/Crecimiento", "salidas", sep = "/"))
  dir.create(paste("~/Crecimiento", "imagenes", sep = "/"))

  system(paste("chmod +x", paste("~/Crecimiento", "procesamiento.py", sep = "/"), sep = " "))
  system(paste("chmod +x", paste("~/Crecimiento", "procesamiento.R", sep = "/"), sep = " "))

}else if(as.numeric(seleccion) == 2){
  library(cronR)
  cron_rm(id = "iwatch")
}else{
   message("Ingresó una opción no válida")
}
