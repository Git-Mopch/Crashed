from colorama import Fore, Style
import os
import socket
import getpass
from Bdsettings import DatabaseManager 

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
db_manager = DatabaseManager()

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
    db_manager.comprobar_usuario(user01,userPass01)
    
def registrarse():
    print(Fore.LIGHTRED_EX + "[Opción: Registrarse]")  
    print(Style.RESET_ALL)
    print("""Has seleccionado la opción de registrarse, para ello tienes que
    completar el formulario con tus datos.""")
    
    finForm = False
    print(Style.RESET_ALL)

    while not finForm:
        user02 = input(Fore.LIGHTGREEN_EX + "[+] Usuario: ")
        userMail02 = input(Fore.LIGHTGREEN_EX + "[+] Correo: ")
        userPass02 = getpass.getpass('[+] Contraseña: ')
        userVerPass02 = getpass.getpass('[+] Verifica Tu Contraseña: ')
        host = socket.gethostname()
        IPAddr = socket.gethostbyname(host)
        print(Style.RESET_ALL)

        if userPass02 == userVerPass02:
            confReg = input("[?] ¿Estás segur@ " + Fore.LIGHTRED_EX + user02 + 
                            Fore.LIGHTWHITE_EX + " con el correo " + 
                            Fore.LIGHTMAGENTA_EX + userMail02 + 
                            Fore.LIGHTWHITE_EX + ", que tus datos son correctos? [S/N]: ").strip()

            if confReg.lower() == "s":
                db_manager.insertar_usuario(user02,userMail02,userPass02,host,IPAddr)
                finForm = True
            else:
                print("[X] Vuelve a intentarlo de nuevo!")
                limpiar_terminal()
        else:
            print(Fore.LIGHTRED_EX + "[X] Las contraseñas no coinciden. Inténtalo de nuevo.")
            limpiar_terminal()
            print(Style.RESET_ALL)

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
    try:
        respuesta01 = input(Fore.LIGHTWHITE_EX + "[+] Seleccione una opción: ")
        if respuesta01 == "1":
            limpiar_terminal()
            iniciarSesion()
        elif respuesta01 == "2":
            limpiar_terminal()
            registrarse()

        elif respuesta01 == "3":
            limpiar_terminal()
            print(""" En caso de no recordar tu contraseña ponte en contacto conmigo mediante el 
 correo:"""+Fore.LIGHTMAGENTA_EX + """ghostfaceQwerty@proton.me """ + Fore.LIGHTWHITE_EX +
                  """y mandame tu nombre de usuario,ultima 
 contraseña que recuerdes y el Codigo de Registro.""")

        elif respuesta01 == "4":
            limpiar_terminal()
            print("[Opción: Registrarse]")
        else:
            print("[x] Tienes que seleccionar una de las opciones disponibles")
    except KeyboardInterrupt:
        print("\n\nInterrupción del programa. Saliendo...")
        exit(0)

menu()