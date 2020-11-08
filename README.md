# Medición sistemática de alturas

Esta herramienta desarrollada para computadores con linux como sistema operativo, fue desarrollada como parte de un proyecto para el curso de Fertilidad de Suelos en el cual se busca realizar mediciones del crecimiento en altura de las plantas; para este fin se combina el script desarrollado para procesamiento de imágenes con aplicaciones de terceros en busca de realizar mediciones de forma periódica y no asistida, usando como herramienta principal un telefono celular establecido en un lugar de manera permanente y con el cual se toman fotografias cada cierto periodo de tiempo (establecido por el usuario) y posteriormente son enviadas de manera autónoma a un computador para su procesamiento, obteniendo como resultado un archivo en formato txt con la fecha y la medición obtenida en cada fotografía.

La herramienta utiliza el formato HSV para segmentar los colores según un límite inferior y un límite superior en donde se encuentra el color deseado en resaltar y este intervalo puede requerir ligeras modificaciones según varien las condiciones de luz. Las lineas 22, 23 y 24 del archivo `procesamiento.R` contiene los intervalos más comunes con los cuales se puede trabajar para resaltar estructuras vegetales, sin embargo, sientase libre de cambiar este intervalo según sus necesidades y teniendo en cuenta la siguiente [imagen](https://github.com/jsmendozap/Crecimiento/blob/main/HSV.png) para el color deseado en resaltar y reemplazando los límites deseados en la linea 28 de este script.

**Nota:** Esta herramienta por defecto viene configurada para ser ejecutada desde la carpeta `/home/usuario/` del computador y usando la carpeta Camera del teléfono (la cual debe estar totalmente vacía al momento de empezar a usar la aplicación), si desea utilizar rutas distintas a las mencionadas para la ejecución de la herramienta asegurese de modificar dichos campos en los script `monitorio.R`, `procesamiento.R` y `procesamiento.py`

# Guía de instalación y configuración en Linux

1. Instalar R `sudo apt install r-base` 
2. Instalar Git `sudo apt install git`
3. Clonar el repositorio  con `git clone https://github.com/jsmendozap/Crecimiento`
4. Conceder permisos de ejecución al script Paquetes.R con el comando `chmod +x Paquetes.R` 
5. Ejecute el instalador de paquetes con `sudo ./Paquetes.R`
6. Halle la escala de la fotografía (puede ser hallada a traves de software como ImageJ)
7. Ejecutar el script `procesamiento.R` para iniciar la aplicación poniendo como argumento el valor obtenido en el punto anterior así: `./procesamiento.R valor`

**Nota:** Si desea realizar el proceso de manera repetitiva y no asistida debe hacer uso del archivo `inicio.sh`, para esto, debe editar dicho archivo y en la linea 5 cambiar `XXX` por el valor obtenido de escala, además haga que este script se vuelva ejecutable al inicio siguiendo cualquiera de los métodos presentados en esta [guía](https://computernewage.com/2019/03/09/scripting-linux-bash-ejecutar-script-arranque/) (Crontab es el más fácil).

# Guía de instalación y configuración para Termux (celular)

1. Instalar [Termux](https://play.google.com/store/apps/details?id=com.termux&hl=es_CO&gl=US) desde la play store
2. Actualizar paquetes con `pkg update`
3. Instalar R siguiendo [esta](https://conr.ca/post/installing-r-on-android-via-termux/) guia
4. Dentro de la aplicación, ejecutar el comando `termux-setup-storage` 
5. Instalar el servicio ssh mediante el comando `pkg install openssh`
6. Ejecutar el comando `ssh-keygen -t rsa -b 4096`, establecer las claves u oprimir enter para dejar vacio este espacio 
7. Ejecutar el comando `ssh-copy-id usuario@ip` cambiando usuario e ip por el nombre de usuario y la ip del computador
8. Mover el archivo `monitoreo.R` a la carpeta downloads del teléfono.
9. Otorgar permisos de ejecución a dicho archivo `chmod +x /data/data/com.termux/files/home/storage/downloads/monitoreo.R` 
10. Moverse a la carpeta downloads en Termux con `cd /data/data/com.termux/files/home/storage/downloads/` 
11. Ejecutar el script monitoreo.R con los siguientes argumentos: 
- El primero es el usuario de la máquina con linux
- El segundo es la ip del computador
- El tercero es el intervalo de tiempo en segundos durante el cual este script buscará una nueva fotografía para ser enviada al computador para su procesamiento.

Ej: `./monitoreo.R juan 192.123.1.23 30` El anterior comando buscará una nueva fotografía en la carpeta camera del teléfono cada `30 segundos` y esta será enviada al usuario `juan` del computador con dirección ip `192.123.1.23` 

una extensión de la aplicación es la posibilidad de recibir notificaciones via telegram del resultado obtenido con el script. Si desea hacer uso de esta funcionalidad debe realizar los siguientes pasos:

* Crear un bot en telegram (este proceso se realiza facilmente con @botfather) y obtener el Token.
* Hallar el ID de la cuenta de telegram a donde llegarán las notificaciones (en el celular: Ajustes -> Cuentas -> Telegram).
* Abrir el archivo `procesamiento.R` y quitarles el # a las lineas 10,11,54,70 y 82.
* En la linea 10 reemplazar "xxxxxx" por "token obtenido al crear el bot" y en la linea 11 por "ID de la cuenta de telegram"
* En el archivo `movido.sh` cambiar las lineas 3 y 4 también por el token del bot y el id de la cuenta de telegram y en la linea 17 eliminar el numeral.
* Otorgar permisos de ejecución `chmod +x /data/data/com.termux/files/home/storage/downloads/movido.sh` (se hace en Termux).
* En el archivo `monitoreo.R` quitar el numeral de la linea numero 21.

Recomiento usar esta herramienta en combinación con la aplicación [Macrodroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid&hl=es_CO&gl=US) disponible en la play store ya que permite realizar macros y automatizar procesos del teléfono, que para este caso es un timelapse de fotografias cada cierto periodo de tiempo y de este modo automatizar completamente la herramienta. [Aquí](https://github.com/jsmendozap/Crecimiento/blob/main/Timelapse_2.png) se puede encontrar una plantilla de como configurar una macro en esta aplicación para que el teléfono tome 1 fotografía cada día. 

Advertencia: La posición de interacción puede variar dependiendo de la marca y modelo del dispositivo.

