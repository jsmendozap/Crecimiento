#! /usr/bin/bash

while inotifywait -e create ~Crecimiento/Fotos/;
do
  Rscript ~/Crecimiento/procesamiento.R XXX
done
