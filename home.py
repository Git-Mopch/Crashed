from colorama import Fore, Back, Style
import os
import getpass

from colorama import Fore, Style

print(Fore.LIGHTYELLOW_EX + r"""
      /$$$$$$                        /$$    /$$        /$$$$$$        /$$
     /$$__  $$                     /$$$$$$ | $$       /$$__  $$      | $$
    | $$  \__/  /$$$$$$  /$$$$$$  /$$__  $$| $$$$$$$ |__/  \ $$  /$$$$$$$
    | $$       /$$__  $$|____  $$| $$  \__/| $$__  $$   /$$$$$/ /$$__  $$
    | $$      | $$  \__/ /$$$$$$$|  $$$$$$ | $$  \ $$  |___  $$| $$  | $$
    | $$    $$| $$      /$$__  $$ \____  $$| $$  | $$ /$$  \ $$| $$  | $$
    |  $$$$$$/| $$     |  $$$$$$$ /$$  \ $$| $$  | $$|  $$$$$$/|  $$$$$$$
    \______/ |__/      \_______/|  $$$$$$/|__/  |__/ \______/  \_______/
                                \_  $$_/                               
                                    \__/   (BY Mopch)                                                                                              
""")
print(Style.RESET_ALL)

def limpiar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def iniciarSesion():
    print(Fore.LIGHTRED_EX + "[Opción: Iniciar Sesión]")
    print(Style.RESET_ALL)
    print("""
#| Has seleccionado la opción de iniciar sesión, por ello vas a tener que
introducir tu usuario y contraseña para """ + Fore.LIGHTBLUE_EX + """Crashed.
              """)
    print(Style.RESET_ALL)
    user01 = input(Fore.LIGHTGREEN_EX + "[?] Usuario: ")
    userPass01 = getpass.getpass('[?] Contraseña:')
    print(Style.RESET_ALL)
    print("USR: " + user01 + " -- Pass: " + userPass01)
    # Llamar a funcion de comprobar en base de datos

def registrarse():
     print(Fore.LIGHTRED_EX + "[Opción: Resgistrarse]")
     print(Style.RESET_ALL)
     print("""
#| Has seleccionado la opción de iniciar sesión, por ello vas a tener que
introducir tu usuario y contraseña para """ + Fore.LIGHTBLUE_EX + """Crashed.
              """)
     print(Style.RESET_ALL)
     user01 = input(Fore.LIGHTGREEN_EX + "[?] Usuario: ")
     userPass01 = getpass.getpass('[?] Contraseña:')
     print(Style.RESET_ALL)
     print("USR: " + user01 + " -- Pass: " + userPass01)
    # Llamar a funcion de comprobar en base de datos
    
def menu():
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
    respuesta01 = input(Fore.LIGHTWHITE_EX + "[+] Seleccione una opción: ")
    if respuesta01 == "1":
        limpiar_terminal()
        iniciarSesion()
    elif respuesta01 == "2":
        limpiar_terminal()
        registrarse()

    elif respuesta01 == "3":
        limpiar_terminal()
        print(""" En caso de no recordar
         tu contraseña ponte en contacto conmigo mediante el correo:
         ghostfaceQwerty@proton.me y mandame tu nombre de usuario,
         ultima contraseña que recuerdes y el Codigo de Registro que se genero
         cuando creaste la cuenta.""")

    elif respuesta01 == "4":
        limpiar_terminal()
        print("[Opción: Registrarse]")
    else:
        print("[x] Tienes que seleccionar una de las opciones disponibles")


menu()


