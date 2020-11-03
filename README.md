# Medición Sistemática de Alturas

Esta herramienta fue desarrollada como parte de un proyecto para el curso de Fertilidad de Suelos en el cual se busca realizar mediciones del crecimiento en altura de las plantas; para este fin se combina el script desarrollado para procesamiento de imágenes con aplicaciones de terceros en busca de realizar mediciones de forma periódica y no asistida, usando como herramienta principal un telefono celular establecido en un lugar de manera permanente y con el cual se toman fotografias cada cierto periodo de tiempo (establecido por el usuario) y posteriormente son enviadas de manera autónoma a un computador para su procesamiento, obteniendo como resultado un archivo en formato txt con la fecha y la medición obtenida en cada fotografía.

La herramienta utiliza el formato HSV para segmentar los colores según un límite inferior y un límite superior en donde se encuentra el color deseado en resaltar y este intervalo puede requerir ligeras modificaciones según varien las condiciones de luz. Las lineas 19, 20 y 21 del archivo `procesamiento.R` contiene los intervalos más comunes con los cuales se puede trabajar para resaltar estructuras vegetales, sin embargo, sientase libre de cambiar este intervalo según sus necesidades y teniendo en cuenta la siguiente [imagen](https://github.com/jsmendozap/Crecimiento/blob/main/HSV.png) para el color deseado en resaltar y reemplazando los límites deseados en la linea 25 de este script.

# Requisitos

- R 3.6.3 o superior
- Python 3.6 o superior
- Termux (celular)

**Nota:** Esta herramienta ha sido diseñada para ser usada en linux, sin embargo, se ofrece una guía para que los usuarios de windows puedan hacer uso de ella a través del sub sitema de linux en windows 10. 

# Guía de instalación y configuración en Windows

1. Utilice [esta](https://ubunlog.com/wsl-como-instalar-y-usar-el-susbistema-ubuntu-en-windows-10/) guía para habilitar el subsistema de linux en windows 10 e instalar ubuntu.
2. Una vez tenga linux funcionando en windows siga con las intrucciones de uso para este sistema operativo.

# Guia de instalación y configuración en Linux

1. Instalar Git en la máquina `apt install git`
2. Clonar el repositorio  mediante `git clone https://github.com/jsmendozap/Crecimiento`
3. Conceder permisos de ejecución al script Instalador.R a través del comando `chmod +x Instalador.R` 
4. Halle la escala de la fotografía (puede ser hallada a traves de software como ImageJ)
5. Editar el archivo `procesamiento.R` y en la linea #68 cambiar los numerales por el valor hallado en el punto anterior.
6. Instalar la aplicación Termux en el telefono celular y luego ejecutar el comando `termux-setup-storage` dentro de ella. 
7. Instalar el servicio ssh mediante el comando `pkg install openssh` en termux y `apt install openssh` en el computador
8. En termux ejecutar el comando `ssh-keygen -t rsa -b 4096` y oprimir 3 veces enter hasta que aparezco el signo dolar de nuevo.
9. En termux ejecutar el comando `ssh-copy-id usuario@ip -p 22` cambiando usuario por el nombre de usuario de la máquina y la ip por la ip del computador.
10. Mover los archivos `monitoreo.R` e `inicio.sh` a la carpeta downloads del teléfono.
11. Otorgar permisos de ejecución a dichos archivos `chmod +x /data/data/com.termux/files/home/storage/downloads/monitoreo.R` y  `chmod +x /data/data/com.termux/files/home/storage/downloads/inicio.sh`.
12. Editar el archivo `monitoreo.R` y en la linea 4 cambiar usuario por el nombre de usuario del equipo al que se va a compartir la fotografía, la ip, por la ip del equipo y la ruta a la carpeta Fotos creada dentro de la carpeta de la herramienta una vez se ejecutó el script `Instalador.R`.
13. Editar el archivo `inicio.sh` y reemplazar el valor de 300 por la cantidad de segundos en que desea que el programa busque nuevas fotografias en la carpeta del teléfono.
14. Moverse a la carpeta downloads en Termux con `cd /data/data/com.termux/files/home/storage/downloads/` y ejecutar el archivo con `./inicio.sh` para iniciar las mediciones.

Con los pasos anteriores el programa quedó completamente funcional (la herramienta únicamente realizar procesamiento de imagen), sin embargo existen algunas configuraciones adicionales para optimizar más al proceso: 

una extensión de la aplicación es la posibilidad de recibir notificaciones via telegram del resultado obtenido con el script. Si desea hacer uso de esta funcionalidad debe realizar los siguientes pasos:

* Crear un bot en telegram (este proceso se realiza facilmente con @botfather) y obtener el Token.
* Hallar el ID de la cuenta de telegram a donde llegarán las notificaciones (en el celular: Ajustes -> Cuentas -> Telegram).
* Abrir el archivo procesamiento.R y quitarles el # a las lineas 8,9,50,66 y 78.
* En la linea 8 reemplazar "xxxxxx" por "token obtenido al crear el bot" y en la linea 9 por "ID de la cuenta de telegram"
* En el archivo `movido.sh` cambiar las lineas 3 y 4 también por el token del bot y el id de la cuenta de telegram y en la linea 17 eliminar el numeral.
* Otorgar permisos de ejecución `chmod +x /data/data/com.termux/files/home/storage/downloads/movido.sh` (se hace en Termux).


Usar en combinación con la herramienta incron para ejecutar esta herramienta una vez la fotografía llegue a la máquina en donde se realizará el procesamiento (disponible unicamente en Linux)

* Instalar incron con el comando `apt install incron`
* Modificar el archivo `/etc/incron.allow` para permitir a un usuario hacer uso de la herramienta (agregar el nombre del usuario)
* utilice el comando `ìncrontab -e` para crear una nueva regla
* La plantilla de la regla debe ser similar a esta `/ruta/carpeta/Fotos/de/la/herramienta/    IN_CREATE       ~/Crecimiento/procesamiento.R $@/$#`
* Puede encontrar una referencia mas completa en esta [página](https://www.xn--linuxenespaol-skb.com/tutoriales/monitorear-archivos-y-carpetas-en-tu-linux-con-incron-incrontab/)


Usarla en combinación con la aplicación Macrodroid (disponible en la play store) ya que permite realizar macros y automatizar procesos del teléfono, que para este caso es un timelapse de fotografias cada cierto periodo de tiempo y de este modo automatizar completamente la herramienta. [Aquí](https://github.com/jsmendozap/Crecimiento/blob/main/Timelapse_2.png) se puede encontrar una plantilla de como configurar una macro en esta aplicación para que el teléfono tome 1 fotografía cada día. 

Advertencia: La posición de interacción puede variar dependiendo de la marca y modelo del dispositivo.

