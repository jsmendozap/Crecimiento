#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 18:39:15 2020

@author: juan
"""

import cv2
import numpy as np
import imageio
import os
import shutil
from pandas import DataFrame


### Correción de imagen ####


def completa(entrada, bajo, alto):
    imagen = cv2.imread(entrada)
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    valor_b = np.array(bajo)
    valor_a = np.array(alto)
    mascara = cv2.inRange(hsv, valor_b, valor_a)
    archivo = entrada.split("/")
    archivo = archivo[4]
    procesado = [os.getcwd(), "Crecimiento/salidas", archivo]
    procesado = "/".join(procesado)
    cv2.imwrite(procesado, mascara)
    cv2.waitKey(0)
    registro = [os.getcwd(), "Crecimiento/Registro/"]
    registro = "/".join(registro)
    shutil.move(entrada, registro)
   
### Calculando la altura alcanzada por la planta ###

def altura(archivo):
    imagen = imageio.imread(archivo)
    coordenadas = list()
    for i in range(imagen.shape[0]):
        for j in range(imagen.shape[1]):
            if imagen[i, j] > 250:
                coordenadas.append((i,j))
    df = DataFrame(coordenadas)
    ruta = [os.getcwd(), "Crecimiento/Resultados/coordenadas.csv"]
    ruta = "/".join(ruta)
    df.to_csv(ruta)
    registro = [os.getcwd(), "Crecimiento/Registro2"]
    registro = "/".join(registro)
    shutil.move(archivo, registro)
