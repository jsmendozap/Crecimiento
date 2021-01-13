#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 17:59:14 2021

@author: Juan
"""

import os, sys
from os import remove

usuario = "USUARIO"
ip = "IP".strip()

destino = usuario + "@" + ip + ":~/Crecimiento/Fotos/"

nombre = os.listdir("/data/data/com.termux/files/home/storage/dcim/Crecimiento/")
ruta = "/data/data/com.termux/files/home/storage/dcim/Crecimiento/" + nombre[0]
envio = "#!/usr/bin/bash \nscp" + " " + ruta + " " + destino
f = open("envio.sh", "w")
f.write(envio)
f.close()
os.popen("chmod +x envio.sh")
os.popen("./envio.sh")
os.popen("rm envio.sh")
remove(ruta)
