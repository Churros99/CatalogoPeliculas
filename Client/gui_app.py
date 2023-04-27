import tkinter as tk
from tkinter import ttk
from Model.pelicula import crear_tabla, borrar_tabla, Pelicula, Guardar, listar, Editar, Eliminar
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu, width=300, height=300)
    
    menu_inicio = tk.Menu(barra_menu, tearoff= 0)
    barra_menu.add_cascade(label='Inicio', menu= menu_inicio)
    menu_inicio.add_command(label='Crear Tabla', command= crear_tabla)
    menu_inicio.add_command(label='Eliminar tabla', command= borrar_tabla)
    menu_inicio.add_command(label='Salir', command=root.destroy)
    
    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Configuración')
    barra_menu.add_cascade(label='Ayuda')
    
class Frame(tk.Frame):
    def __init__(self,root = None):
        super().__init__(root, width=600, height=480)
        self.root = root
        self.pack()
        self.config(bg='Green')
        
        self.id_pelicula = None
        self.campos_pelicula()
        self.deshabilitar_campos()
        self.tabla_peliculas()
    
    def campos_pelicula(self):
        # Labels
        self.label_nombre = tk.Label(self, text='Nombre: ')
        self.label_nombre.config(font=('Arial',12,'bold'), bg='green')
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        
        self.label_duracion = tk.Label(self, text='Duración: ')
        self.label_duracion.config(font=('Arial',12,'bold'), bg='green')
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10)
        
        self.label_genero = tk.Label(self, text='Genero: ')
        self.label_genero.config(font=('Arial',12,'bold'), bg='green')
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)
        
        # Entrys
        self.mi_nombre = tk.StringVar(self)
        self.entry_nombre = tk.Entry(self, textvariable = self.mi_nombre)
        self.entry_nombre.config(width=50, font=('Arial',12,'bold'))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan= 2)
        
        self.mi_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable=self.mi_duracion)
        self.entry_duracion.config(width=50, font=('Arial',12,'bold'))
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan= 2)
        
        self.mi_genero = tk.StringVar(self)
        self.entry_genero = tk.Entry(self, textvariable= self.mi_genero)
        self.entry_genero.config(width=50, font=('Arial',12,'bold'))
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10, columnspan= 2)
        
        # Botones
        self.boton_nuevo = tk.Button(self, text='Nuevo')
        self.boton_nuevo.config(width=20, font=('Arial',12,'bold'), fg='#DAD5D6',bg='#158645', cursor='hand2', activebackground='#35bd6f', command = self.habilitar_campos)
        self.boton_nuevo.grid(row=3, column=0, padx=10, pady=10)
        
        self.boton_guardar = tk.Button(self, text='Guardar')
        self.boton_guardar.config(width=20, font=('Arial',12,'bold'), fg='#DAD5D6',bg='#1658A2', cursor='hand2', activebackground='#3586DF', command= self.Guardar_datos)
        self.boton_guardar.grid(row=3, column=1, padx=10, pady=10)
        
        self.boton_cancelar = tk.Button(self, text='Cancelar')
        self.boton_cancelar.config(width=20, font=('Arial',12,'bold'), fg='#DAD5D6',bg='#BD152E', cursor='hand2', activebackground='#E15370', command = self.deshabilitar_campos)
        self.boton_cancelar.grid(row=3, column=2, padx=10, pady=10)
        
    def tabla_peliculas(self):
        self.tabla = ttk.Treeview(self, columns=('Nombre', 'Duración', 'Genero'))
        self.tabla.grid(row=4, column= 0, columnspan=4, sticky='nse')
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Duración')
        self.tabla.heading('#3', text='Genero')
        self.lista_peliculas = listar()
        self.lista_peliculas.reverse()
        
        self.boton_editar = tk.Button(self, text='Editar')
        self.boton_editar.config(width=20, font=('Arial',12,'bold'), fg='#DAD5D6',bg='#158645', cursor='hand2', activebackground='#35bd6f', command= self.Editar_datos)
        self.boton_editar.grid(row=5, column=0, padx=10, pady=10)
        
        self.boton_Eliminar = tk.Button(self, text='Eliminar')
        self.boton_Eliminar.config(width=20, font=('Arial',12,'bold'), fg='#DAD5D6',bg='#BD152E', cursor='hand2', activebackground='#E15370', command=self.Eliminar_datos)
        self.boton_Eliminar.grid(row=5, column=1, padx=10, pady=10)
        
        self.scroll = ttk.Scrollbar(self, orient= 'vertical', command= self.tabla.yview)
        self.scroll.grid(row=4, column=4, sticky='nse') 
        self.tabla.configure(yscrollcommand=self.scroll.set) 
               
        # Iterar la lista de peliculas
        for i in self.lista_peliculas:
            self.tabla.insert('', 0, text=i[0], values=(i[1], i[2], i[3]))
        
    def habilitar_campos(self):
        self.entry_nombre.config(state ='normal')
        self.entry_duracion.config(state ='normal')
        self.entry_genero.config(state ='normal')
            
        self.boton_guardar.config(state ='normal')
        self.boton_cancelar.config(state ='normal')
        
    def deshabilitar_campos(self):
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')
        self.id_pelicula = None
        
        self.entry_nombre.config(state ='disabled')
        self.entry_duracion.config(state ='disabled')
        self.entry_genero.config(state ='disabled')
            
        self.boton_guardar.config(state ='disabled')
        self.boton_cancelar.config(state ='disabled')
    
    def Guardar_datos(self):
        pelicula = Pelicula( nombre= self.mi_nombre.get(), duracion = self.mi_duracion.get(), genero= self.mi_genero.get())
        
        if self.id_pelicula == None:
            Guardar(pelicula=pelicula)
            self.deshabilitar_campos()
            self.tabla_peliculas()
        else:
            Editar(pelicula= pelicula, id_pelicula= self.id_pelicula)
        
    def Editar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula = self.tabla.item(self.tabla.selection())['values'][0]
            self.duracion_pelicula = self.tabla.item(self.tabla.selection())['values'][1]
            self.genero_pelicula = self.tabla.item(self.tabla.selection())['values'][2]
            
            self.habilitar_campos()
            
            self.entry_nombre.insert(0, self.nombre_pelicula)
            self.entry_duracion.insert(0, self.duracion_pelicula)
            self.entry_genero.insert(0, self.genero_pelicula)
        except:
            pass
        
    def Eliminar_datos(self):
        try:
            Eliminar(self.tabla.item(self.tabla.selection())['text'])
            self.tabla_peliculas()
        except:
            pass
        