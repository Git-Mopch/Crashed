import psycopg2  # type: ignore
from colorama import Fore, Style
from AMS import menuUserRegistered


class DatabaseManager:
    def __init__(self):
        self.connection = self.conectar()

    def conectar(self):
        """Establece una conexión a la base de datos PostgreSQL."""
        try:
            connection = psycopg2.connect(
                database="crashed",
                user="postgres",
                password="032003",
                host="localhost",
                port="5432"
            )
            return connection
        except Exception as e:
            print("Error al conectar a PostgreSQL:", e)
            return None

    def mostrar_usuarios(self):
        """Muestra todos los usuarios en la base de datos."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM usuarios;")
            usuarios = cursor.fetchall()
            print("Usuarios:")
            for usuario in usuarios:
                print(usuario)
        except Exception as e:
            print("Error al mostrar usuarios:", e)
        finally:
            cursor.close()

    def insertar_usuario(self, username, email, password, ip, devName):
        """Inserta un nuevo usuario en la base de datos."""
        try:
            cursor = self.connection.cursor()
            insert_query = """
            INSERT INTO us00rs_cr4sh3d (nombreUsuario, email, password, ip, deviceName, RolUserMainCreate)
            VALUES (%s, %s, %s, %s, %s, %s);
            """
            cursor.execute(insert_query, (username, email, password, ip, devName, "bs"))
            self.connection.commit()
            print(f"Usuario '{username}' insertado correctamente.")
        
        except psycopg2.IntegrityError:
            print(Fore.LIGHTRED_EX + f"[X] DETAIL: Ya existe laun usuario con el correo ({email}).")
            self.connection.rollback()
    
        except Exception as e:
            print(Fore.LIGHTRED_EX + "\n[X] Error inesperado al insertar usuario:", e)
            self.connection.rollback()
        
        finally:
            cursor.close()

    def comprobar_usuario(self, nombre, passwd):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM us00rs_cr4sh3d where nombreUsuario = '" +
                           nombre + "' and password = '" + passwd + "';")
            usuarios = cursor.fetchall()
            if not usuarios:
                print(Fore.LIGHTRED_EX+ "[x] Error: No se encontró ningún usuario con ese nombre y contraseña.")
                print(Style.RESET_ALL)
            else:
                menuUserRegistered(nombre)
        except Exception as e:
            print("Error al mostrar usuarios:", e)
        finally:
            cursor.close()

    def cerrar_conexion(self):
        """Cierra la conexión a la base de datos."""
        if self.connection:
            self.connection.close()
            print("Conexión cerrada.")
