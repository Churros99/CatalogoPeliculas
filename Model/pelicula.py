from .conexion_db import ConexionDB
from tkinter import messagebox

def crear_tabla():
    conexion = ConexionDB()
    try:
        sql = 'CREATE TABLE IF NOT EXISTS PELICULAS (Id_pelicula integer, Nombre varchar(100), Duracion varchar(10), Genero varchar(100), PRIMARY KEY (Id_pelicula AUTOINCREMENT))'
        conexion.cursor.execute(sql)
        conexion.cerrar()
        messagebox.showinfo(title ='Crear Tabla', message = 'Se creo la tabla en la base de datos')
    except:
        messagebox.showerror('Crear Tabla', message = 'No se pudo crear la tabla')

def borrar_tabla():
    conexion = ConexionDB()
    try:
        sql = 'DROP TABLE IF EXISTS PELICULAS'
        conexion.cursor.execute(sql)
        conexion.cerrar()
        messagebox.showinfo(title ='Eliminar Tabla', message = 'Se elimino la tabla en la base de datos')
    except:
        messagebox.showerror('Eliminar Tabla', message = 'No se pudo eliminar la tabla')
        

class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.IdPelicula = None
        self.Nombre = nombre
        self.Duracion = duracion
        self.Genero = genero
    
    def __str__(self) -> str:
        return f'Pelicula[{self.Nombre}, {self.Duracion}, {self.Genero}]'
    
def Guardar(pelicula: Pelicula):
    conexion = ConexionDB()
    try:
        sql = f"insert into PELICULAS (Nombre,Duracion,Genero) values('{pelicula.Nombre}', '{pelicula.Duracion}', '{pelicula.Genero}')"
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        messagebox.showerror('Guardar Pelicula', f'Ocurrio un error al guardar la pelicula {pelicula.Nombre}')

def listar():
    conexion = ConexionDB()
    lista_pelicula = []
    sql = 'select * from PELICULAS'
    
    try:
        conexion.cursor.execute(sql)
        lista_pelicula = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        messagebox.showerror('Obtener los registros', 'No se pudieron obtener las peliculas')
    
    return lista_pelicula

def Editar(pelicula: Pelicula, id_pelicula: int):
    conexion = ConexionDB()
    sql = f"UPDATE PELICULAS SET nombre='{pelicula.Nombre}', duracion='{pelicula.Duracion}', genero = '{pelicula.Genero}' where id_pelicula = {id_pelicula}"
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        messagebox.showerror('Modificar pelicula','Ocurrio un error al modificar la pelicula {pelicula.Nombre}, intentelo mas tarde.')
        
def Eliminar(id_pelicula: int):
    conexion = ConexionDB()
    sql = f"delete from PELICULAS where id_pelicula = {id_pelicula}"
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        messagebox.showerror('Eliminar Pelicula','Ocurrio un error al eliminar la pelicula, intentelo mas tarde.')