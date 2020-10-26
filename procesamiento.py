#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 18:39:15 2020

@author: juan
"""

import cv2
import numpy as np
from PIL import Image
import imageio
import csv
import os
import shutil
from pandas import DataFrame


### Correción de imagen ####


def completa(entrada, bajo, alto):
    ruta = ("/home/juan/Fertilidad/Fotos/" + entrada)
    imagen = cv2.imread(ruta)
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    lista_baja = bajo
    lista_alta = alto
    valor_b = np.array(lista_baja)
    valor_a = np.array(lista_alta)
    mascara = cv2.inRange(hsv, valor_b, valor_a)
    cv2.imwrite(os.path.join("/home/juan/Fertilidad/salidas/", entrada), mascara)
    cv2.waitKey(0)
    shutil.move(ruta, "/home/juan/Fertilidad/Registro/")
   
### Calculando la altura alcanzada por la planta ###

def altura(nombre):
    ruta = ("/home/juan/Fertilidad/salidas/"+ nombre)
    imagen = imageio.imread(ruta)
    coordenadas = list()
    for i in range(imagen.shape[0]):
        for j in range(imagen.shape[1]):
            if imagen[i, j] > 250:
                coordenadas.append((i,j))
    df = DataFrame(coordenadas)
    df.to_csv("/home/juan/Fertilidad/Resultados/coordenadas.csv")
    shutil.move(ruta, "/home/juan/Fertilidad/Registro2/")
