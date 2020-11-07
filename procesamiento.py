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
    ruta = (entrada)
    imagen = cv2.imread(ruta)
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    valor_b = np.array(bajo)
    valor_a = np.array(alto)
    mascara = cv2.inRange(hsv, valor_b, valor_a)
    cv2.imwrite(os.path.join("~/Crecimiento/salidas/", entrada), mascara)
    cv2.waitKey(0)
    shutil.move(ruta, "~/Crecimiento/Registro/")
   
### Calculando la altura alcanzada por la planta ###

def altura(nombre):
    ruta = ("~/Crecimiento/salidas/"+ nombre)
    imagen = imageio.imread(ruta)
    coordenadas = list()
    for i in range(imagen.shape[0]):
        for j in range(imagen.shape[1]):
            if imagen[i, j] > 250:
                coordenadas.append((i,j))
    df = DataFrame(coordenadas)
    df.to_csv("~/Crecimiento/Resultados/coordenadas.csv")
    shutil.move(ruta, "~/Crecimiento/Registro2/")
