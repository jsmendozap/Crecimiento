# Medición sistemática de alturas

<p>Esta herramienta desarrollada como parte de un proyecto para el curso de Fertilidad de Suelos en el cual se busca realizar mediciones del crecimiento en altura de las plantas; para este fin se combina el script desarrollado para procesamiento de imágenes con aplicaciones de terceros en busca de realizar mediciones de forma periódica y no asistida, usando como herramienta principal un telefono celular establecido en un lugar de manera permanente y con el cual se toman fotografias cada cierto periodo de tiempo (establecido por el usuario) y posteriormente son enviadas de manera autónoma a un computador para su procesamiento, obteniendo como resultado un archivo en formato txt con la fecha y la medición obtenida en cada fotografía.</p>

La herramienta utiliza el formato HSV para segmentar los colores según un límite inferior y un límite superior en donde se encuentra el color deseado en resaltar (dicho intervalo puede requerir ligeras modificaciones según varien las condiciones de luz). Las lineas 21, 22 y 23 del archivo `procesamiento.R` contiene los intervalos más comunes con los cuales se puede trabajar para resaltar estructuras vegetales, sin embargo, sientase libre de cambiar este intervalo según sus necesidades. Si tiene dudas sobre como escoger los límites para el color de su interés puede leer [esta](https://stackoverrun.com/es/q/2906350) pregunta publicada en stackoverrun, una vez haya fijado los límites de detección asegurese de reemplazarlos en la linea 28 de este script.

# Pasos previos a la instalación

Esta herramienta hace uso de la interfáz de telegram para solicitar acciones en el teléfono que tomará las fotografías a través de un bot. Por lo anterior es necesario que antes de instalar y configurar la aplicación cree un bot, esto es un proceso sencillo que se puede hacer a través de @botfather directamente en la aplicación; al finalizar este proceso, por favor conserve el **token** de su bot ya que se le solicitará en el proceso de instalación, además del token deberá proporcionar el **ID** de su cuenta de telegram (lo puede encontrar en su celular: Ajustes -> Cuentas -> Telegram) y por último debe suministrar la **escala** de la fotografía, para lo cual puede utilizar ImageJ para obtenerla o cualquier otro de su elección.

# Guía de instalación y configuración

Esta herramienta consta de dos partes que serán configuradas a través del proceso de instalación con la información que usted suministre.
* La primera parte corresponde a los arhivos que irán en el computador a donde llegarán (de manera automática) las imágenes tomadas por el teléfono  y posteriormente realizarán el procesamiento de ellas.
* La segunda parte corresponde a los archivos que deben ir en el teléfono para que el bot de telegram funcione adecuadamente y este pueda responder a las acciones que solicite el usuario.

Cada uno de los pasos que se deben seguir para configurar las dos partes se detallan a continuación:

## 1. Computador (Linux)

1. Instalar Git `sudo apt install git`.
2. Clonar el repositorio  con `git clone https://github.com/jsmendozap/Crecimiento`.
3. Otorgue permisos de ejecución al archvo *configuracion.sh* con `chmod +x configuracion.sh`.
4. Ejecute el archivo `./configuracion.sh`.
5. Una vez el script anterior haya terminado su trabajo copie la carpeta teléfono y llevela a la carpeta downloads del teléfono que utilizará para tomar las fotografías.

**Nota:** Cabe mencionar que este teléfono debe permanecer fijo en la posición en donde tomará las fotografías, de lo contrario el valor de escala cambiaría y las mediciones serían erróneas.

## 2. Celular

1. Instale [Termux](https://play.google.com/store/apps/details?id=com.termux&hl=es_CO&gl=US).
2. Dentro de la aplicación, ejecute el comando `termux-setup-storage`
3. Ejecute: `mv /data/data/com.termux/files/home/storage/downloads/telefono/* /data/data/com.termux/files/home/`
4. Otorgue permisos de ejecución con `chmod +x telefono.sh`
5. Ejecute `./telefono.sh`
6. Ejecute el comando `ssh-keygen`, establecer las claves u oprimir enter para dejar vacio este espacio.
7. Ejecutar el comando `ssh-copy-id usuario@ip` cambiando usuario e ip
por el nombre de usuario y la ip del computador.
8. Instale la aplicación [Macrodroid](https://play.google.com/store/apps/details?id=com.arlosoft.macrodroid&hl=es_CO&gl=US), disponible en la play store y siga los pasos mostrados [aquí](https://github.com/jsmendozap/Crecimiento/blob/main/Configuraci%C3%B3n%20Macrodroid.gif) para configurar la macro que tomará la foto cada vez que le indiquemos.
