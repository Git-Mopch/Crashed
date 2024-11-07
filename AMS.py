from colorama import Fore, Style
import os
from Bdsettings import DatabaseManager  

db_manager = DatabaseManager()

def limpiar_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def menuUserRegistered(nombre, rol):
    limpiar_terminal()
    print(Fore.LIGHTGREEN_EX + f"Bienvenido {nombre}")
    print(Style.RESET_ALL)
    if(rol == "gh"):
        limpiar_terminal()
        print(f"""{Fore.LIGHTWHITE_EX}
#| Bienvenid@ {Fore.LIGHTCYAN_EX + nombre + Fore.LIGHTWHITE_EX}(Admin), un placer tenerte de nuevo, ¿con que te puedo
ayudar en el dia de hoy?
            """)
        print(f"""
{Fore.LIGHTMAGENTA_EX}(OPCIONES){Fore.LIGHTWHITE_EX}
        1. Seleccionar sesión activa.
        2. Crear una nueva sesión.
        3. Eliminar sesión
        4. Buscar usuario.
        5. Añadir usuario.
        6. Eliminar usuario.
        7. Salir
            """)
        #Añadir funcionalidades de Admin
        
    elif(rol =="gt" or rol == "bs"):
        limpiar_terminal()
        print(f"""{Fore.LIGHTWHITE_EX}
#| Bienvenid@ {Fore.LIGHTCYAN_EX + nombre + Fore.LIGHTWHITE_EX}, un placer tenerte de nuevo, ¿con que te puedo
ayudar en el dia de hoy?
            """)
        print(f"""
{Fore.LIGHTMAGENTA_EX}(OPCIONES){Fore.LIGHTWHITE_EX}
    1. Seleccionar sesión activa.
    2. Crear una nueva sesión.
    3. Eliminar sesión
    4. Salir
            """)
    
    #Añadir funcionalidades de User


def menuUserSesActv():
        limpiar_terminal()
        print(f"""
{Fore.LIGHTMAGENTA_EX}(OPCIONES){Fore.LIGHTWHITE_EX}
        1. Ver ultimos productos almacenados.
        2. Generar nuevos productos.
        3. Obtener asesoramiento
            """)
        #Añadir funcionalidades de Admin
        decision = input("[+] Opcion Seleccionada: ")
        
        if(decision == "1"):
            print("")
        elif(decision == "2"):
            print("")
        elif(decision == "3"):
            print(f"""
    {Fore.LIGHTMAGENTA_EX}(OPCIONES){Fore.LIGHTWHITE_EX}
            1. Compras.
            2. Ventas.
                """)
            #Aquí se mostrara el sitio donde este más barato en el caso de compras, o el más caro en caso de ventas