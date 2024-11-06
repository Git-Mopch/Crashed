#Aplication Menu Settings
from colorama import Fore, Style
import os
import socket

print(Style.RESET_ALL)

def limpiar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menuUserRegistered(nom):
    limpiar_terminal()
    print(Fore.LIGHTGREEN_EX+ "["+Fore.LIGHTBLUE_EX+"O"+Fore.LIGHTGREEN_EX+"] Bienvenid@ " + nom)
    print(Style.RESET_ALL)
    print("""
    #| Bienvenid@ a Crashed, con esta herramienta seras capaz de monitorizar 
    precios de productos y analizar tu competencia para garantizar una buena 
    gestion de tu negocio. 
          """)
    print("""
    (OPCIONES)
    1. Iniciar Sesión
    2. Registrarse
    3. Olvide Mi Contraseña
    4. Cerrar
          """)

