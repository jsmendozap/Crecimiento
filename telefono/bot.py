#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 12:01:17 2020

@author: juan
"""
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
import os
from datetime import datetime
import subprocess
from crontab import CronTab
from getpass import getuser

archivos = os.listdir()

permitido = [IDUSER]

if "registro.txt" and "usuarios.txt" not in archivos:
    registro = open("registro.txt", "w")
    usuarios = open("usuarios.txt", "w")
    usuarios.write("NOMBRE" + ": " + str(permitido[0]))
    usuarios.close()

#Cargando usuarios
archivo = open("usuarios.txt", "r")
usuarios = archivo.read().splitlines()
for i in range(len(usuarios)):
    usuario = usuarios[i].split()
    if int(usuario[1]) not in permitido:
       permitido.append(int(usuario[1]))

#Token del BOT
TOKEN = 'TOKENBOT'

#Directorios de registros
log_dir = os.getcwd() + "/registro.txt"

#Configurando Crontab
cron = CronTab(user = getuser())

#Comandos del bot

commands = {
        'inicio': 'Iniciar el bot',
        'cd': 'Cambia el directorio actual',
        'exec': 'Ejecuta un comando',
        'terminar': 'Termina el proceso del bot en el servidor',
	'bateria': 'Estado de la bateria',
        'foto': 'Tomar una fotografia',
        'intervalo': 'Inicia la toma de fotografias cada cierto intervalo de tiempo',
        'configuracion': 'Configurar herramienta en servidor',
        'usuarios': 'Añada a un usuario que pueda hacer uso de este bot'
        }

markup = types.ReplyKeyboardMarkup()
markup.row('/inicio', '/terminar',)
markup.row('/bateria', '/foto')
markup.row('/usuarios', '/intervalo')
markup.row('/configuracion')

def gen_markup():
    markup1 = InlineKeyboardMarkup()
    markup1.row_width = 2
    markup1.add(InlineKeyboardButton("Usuario", callback_data="usuario"),
                InlineKeyboardButton("Ip", callback_data="ip"),
                InlineKeyboardButton("Puerto", callback_data="puerto")
                )
    return markup1

def int_markup():
    markup2 = InlineKeyboardMarkup()
    markup2.row_width = 2
    markup2.add(InlineKeyboardButton("Activar intervalo", callback_data="on"),
                InlineKeyboardButton("Desactivar intervalo", callback_data="off")
                )
    return markup2

def usuario_markup():
    markup3 = InlineKeyboardMarkup()
    markup3.row_width = 2
    markup3.add(InlineKeyboardButton("Listar usuarios", callback_data="lista"),
                InlineKeyboardButton("Añadir usuarios", callback_data="añadir"),
                InlineKeyboardButton("Eliminar usuarios", callback_data="eliminar"),
                )
    return markup3

#Escucha de solicitudes del bot
def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            fecha = datetime.fromtimestamp(m.json['date'])
            registro = open(log_dir, "a+")
            registro.write(str(m.chat.first_name) + " [" + str(m.chat.id) + "]" +
                           " [" + str(fecha) + "] : " + m.text + "\n")
            registro.close()

bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)

# Manejo de eventos para los comandos establecidos

@bot.message_handler(commands=['inicio'])
def command_start(m):
    cid = m.chat.id
    if cid in permitido:
        bot.send_message(cid, "¡Bienvenido/a!".format(m.chat.first_name), reply_markup = markup)
    else:
        bot.send_message(cid, "Lo siento, usted no se encuentra autorizado para operar este bot")

@bot.message_handler(commands=['terminar'])
def terminar(m):
    bot.send_message(m.chat.id, "¡Adios!")
    apagar = os.popen("pidof python3").read()
    apagar = "kill " + apagar
    os.popen(apagar)

@bot.message_handler(commands=['exec'])
def ejecutar(m):
    cid = m.chat.id
    if cid in permitido:
        bot.send_message(cid, "Ejecutando: " + m.text[len("/exec") :])
        bot.send_chat_action(cid, 'typing')
        time.sleep(2)
        f = os.popen(m.text[len("/exec"):])
        resultado = f.read()
        bot.send_message(cid, "Resultado: " + resultado)
    else:
        bot.send_message(cid, "Lo sentimos, usted no está autorizado para operar este bot")

@bot.message_handler(commands=['cd'])
def cambio(m):
    cid = m.chat.id
    if cid in permitido:
        os.chdir(m.text[len("/cd"):].strip())
        f = os.popen("pwd")
        resultado = f.read()
        bot.send_message(cid, "Directorio actual: " + resultado)
    else:
        bot.send_message(cid, "Lo sentimos, usted no esta autorizado para operar este bot")

@bot.message_handler(commands=['bateria'])
def bateria(m):
    cid = m.chat.id
    if cid in permitido:
        f = os.popen("termux-battery-status")
        resultado = f.read()
        bot.send_message(cid, resultado)
    else:
        bot.send_message(cid, "Lo sentimos, usted no esta autorizado para operar este bot")

@bot.message_handler(commands=['foto'])
def foto(m):
    cid = m.chat.id
    if cid in permitido:
        os.popen("termux-clipboard-set foto")
        time.sleep(5)
        subprocess.run('python monitoreo.py', shell = True)
        bot.send_message(cid, "Comando ejecutado con exito")
    else:
        bot.send_message(cid, "Lo sentimos, usted no esta autorizado para operar este bot")


@bot.callback_query_handler(func=lambda call: True)
def callback_query(query):
    if query.data == "usuario":
        msg = bot.send_message(query.from_user.id, "Ingrese el nombre de usuario del dispositivo")
        bot.register_next_step_handler(msg, callback = ingreso_usuario)
    elif query.data == "ip":
        msg = bot.send_message(query.from_user.id, "Ingrese la ip del dispositivo")
        bot.register_next_step_handler(msg, callback = ingreso_ip)
    elif query.data == "puerto":
        msg = bot.send_message(query.from_user.id, "Ingrese el número de puerto para conexión ssh, por defecto se encuentra el 22")
        bot.register_next_step_handler(msg, callback = puerto)
    elif query.data == "on":
        msg = bot.send_message(query.from_user.id, "Ingrese el intervalo de tiempo en minutos en el que desea que la cámara tome fotografías")
        bot.register_next_step_handler(msg, callback = intervalo_on)
        bot.send_chat_action(query.from_user.id, 'tipyng')
    elif query.data == "off":
        msg = bot.send_message(query.from_user.id, "La función por intervalo se está desactivando, por favor espere")
        os.popen("crontab -r")
        bot.send_message(query.from_user.id, "La tarea se deshabilitó exitosamente")
    elif query.data == "lista":
        f = open("usuarios.txt", "r")
        users = f.read().splitlines()
        for i in range(len(users)):
            bot.send_message(query.from_user.id, users[i])
    elif query.data == "añadir":
        msg = bot.send_message(query.from_user.id, "Ingrese la información del nuevo usuario así:\nNombre: ID telegram")
        bot.register_next_step_handler(msg, callback = ingreso_user)
    elif query.data == "eliminar":
        msg = bot.send_message(query.from_user.id, "Ingrese la información del usuario a eliminar así:\nNombre: ID telegram")
        bot.register_next_step_handler(msg, callback = eliminar_user)

@bot.message_handler(commands=['usuarios'])
def intervalo(m):
    cid = m.chat.id
    if cid in permitido:
        bot.send_message(cid, "¿Que desea hacer?", reply_markup=usuario_markup())
    else:
        bot.send_message(cid, "Lo sentimos, usted no está autorizado para operar este bot")

@bot.message_handler(commands=['intervalo'])
def intervalo(m):
    cid = m.chat.id
    if cid in permitido:
        bot.send_message(cid, "¿Que desea hacer?", reply_markup=int_markup())
    else:
        bot.send_message(cid, "Lo sentimos, usted no está autorizado para operar este bot")

def intervalo_on(m):
   tiempo = m.text
   intervalo = cron.new(command = 'termux-clipboard-set foto', comment = 'foto')
   intervalo.minute.every(tiempo)
   time.sleep(10)
   monitoreo = cron.new(command = 'Rscript /data/data/com.termux/files/home/monitoreo.py', comment = 'foto')
   monitoreo.minute.every(tiempo)
   cron.write()
   os.popen("sv-enable crond")
   bot.send_message(m.chat.id, "La tarea se ejecutará cada {} minutos".format(tiempo))
   bot.send_message(m.chat.id, "Tarea programada exitosamente")

@bot.message_handler(commands=['configuracion'])
def configuracion(m):
    cid = m.chat.id
    if cid in permitido:
        bot.send_message(cid, "Estos datos se tomaron de manera automática del dispositivo en donde se descargó la herramienta, si realizó algún cambio, por favor actualice la información diligenciando la información abajo solicitada.", reply_markup=gen_markup())
    else:
        bot.send_message(cid, "Lo sentimos, usted no está autorizado para operar este bot")

def ingreso_usuario(m):
    f = open(os.getcwd() + "/monitoreo.py", "r")
    contenido = f.read().splitlines()
    contenido[11] = "usuario = '" + str(m.text) + "'"
    nuevo = []
    for i in range(len(contenido)):
        elemento = contenido[i] + "\n"
        nuevo.append(elemento)
    j = open(os.getcwd() + "/monitoreo.py", "w")
    for i in range(0,len(nuevo)):
        j.writelines(nuevo[i])
    j.close()
    bot.send_message(m.chat.id, "Información de usuario actualizada exitosamente")

def ingreso_ip(m):
    f = open(os.getcwd() + "/monitoreo.py", "r")
    contenido = f.read().splitlines()
    contenido[12] = "ip = '" + str(m.text) + "'"
    nuevo = []
    for i in range(len(contenido)):
        elemento = contenido[i] + "\n"
        nuevo.append(elemento)
    j = open(os.getcwd() + "/monitoreo.py", "w")
    for i in range(0,len(nuevo)):
        j.writelines(nuevo[i])
    j.close()
    bot.send_message(m.chat.id, "Dirección ip actualizada exitosamente")

def puerto(m):
    f = open(os.getcwd() + "/monitoreo.py", "r")
    contenido = f.read().splitlines()
    contenido[18] = 'envio = "#! /usr/bin/bash \nscp "' + "'-P '" + str(m.text) + " " + "ruta" + " " + "destino"
    nuevo = []
    for i in range(len(contenido)):
        elemento = contenido[i] + "\n"
        nuevo.append(elemento)
    j = open(os.getcwd() + "/monitoreo.py", "w")
    for i in range(0,len(nuevo)):
        j.writelines(nuevo[i])
    j.close()
    bot.send_message(m.chat.id, "número puerto actualizada exitosamente")

def ingreso_user(m):
    f = open(os.getcwd() + "/usuarios.txt", "a")
    mensaje = str(m.text)
    f.write("\n" + mensaje)
    f.close()
    id = mensaje.split()
    permitido.append(int(id[1]))
    bot.send_message(m.chat.id, "Usuario agregado exitosamente")

def eliminar_user(m):
    mensaje = str(m.text)
    archivo = open(os.getcwd() + "/usuarios.txt", "r")
    usuarios = archivo.read().splitlines()
    if mensaje in usuarios:
        usuarios.remove(mensaje)
        f = open(getcwd() + "/usuarios.txt", "w")
        for i in range(len(usuarios)):
            f.writelines(usuarios[i] + "\n")
        f.close()
        id = mensaje.split()
        permitido.remove(int(id[1]))
        bot.send_message(m.chat.id, "Usuario eliminado exitosamente")
    else:
        bot.send_message(m.chat.id, "La información ingresada no se encuentra en la lista de usuarios permitidos")

# Manteniendo activo el estado del bot
bot.polling()
