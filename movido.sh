#!/bin/bash

TOKEN="######"
ID="#####"
MENSAJE="Fotografia movida con exito"
URL="https://api.telegram.org/bot$TOKEN/sendMessage"

curl -s -X POST $URL -d chat_id=$ID -d text="$MENSAJE"
