# Medición de la altura de la planta

Esta herramienta desarrollada para maquinas que corren bajo el sistema operativo linux fue desarrollada como parte de un proyecto para el curso de Fertilidad de Suelos en el cual se busca realizar mediciones del crecimiento en altura de las plantas de forma periódica y no asistida, usando como herramienta un telefono celular establecido en un lugar de manera permanente y con el cual se toman fotografias cada cierto periodo de tiempo (establecido por el usuario) y estas son enviadas de manera autónoma a un computador para su posterior procesamiento, obteniendo como resultado un archivo en formato txt con la fecha y la medición obtenida en cada fotografía.

# Guia de instalación y configuración

1. Instalar Git en la máquina `apt install git`
2. Clonar el repositorio  mediante `git clone https://github.com/jsmendozap/Crecimiento`
3. Conceder permisos de ejecución al script Instalador.R a través del comando `chmod +x Instalador.R` 
4. Ejecutar el script `./Instalador.R`
5. Hallar la escala de la fotografía (puede ser hallada a traves de software como ImageJ)
6. Abrir con cualquier editor de texto el archivo procesamiento.R y en la linea #70 cambiar los numerales por la escala hallada en el punto anterior.
7. Instalar la aplicación Termux en el telefono celular y luego ejecutar el comando `termux-setup-storage` dentro de ella 
8. Mover los archivos `monitoreo.R` e `inicio.sh` a la carpeta downloads del teléfono
9. Otorgar permisos de ejecución a dichos archivos `chmod +x monitorio.R` y  `chmod +x inicio.sh`
10. Editar el archivo `monitoreo.R` y en la linea 4 cambiar usuario por el nombre de usuario del equipo al que se va a compartir la fotografía, la ip, por la ip del equipo y la ruta a la carpeta Fotos creada dentro de la carpeta de la herramienta una vez se ejecutó el script `Instalador.R`
11. Editar el archivo `inicio.sh` y reemplazar el valor de 300 por la cantidad de segundos en que desea que el programa busque nuevas fotografias en la carpeta del teléfono.
12. Ejecutar el archivo `./inicio.sh`

Con los pasos anteriores el programa quedó completamente funcional, sin embargo una extensión de la aplicación es la posibilidad de recibir notificaciones via telegram del resultado obtenido con el script. Si desea hacer uso de esta funcionalidad debe realizar los siguientes pasos:

* Crear un bot en telegram (este proceso se realiza facilmente con @botfather) y obtener el Token
* Hallar el ID de la cuenta de telegram a donde llegarán las notificaciones (Ajustes -> Cuentas -> Telegram)
* Abrir el archivo procesamiento.R y quitarles el # a las lineas 8,9,52,68 y 80
* En la linea 8 reemplazar "xxxxxx" por "token obtenido al crear el bot" y en la linea 9 por "ID de la cuenta de telegram"
* En el archivo `movido.sh` cambiar las lineas 3 y 4 también por el token del bot y el id de la cuenta de telegram
* Otorgar permisos de ejecución `chmod +x movido.sh`

![Macro](https://github.com/jsmendozap/Crecimiento/blob/main/Timelapse_2.png)
