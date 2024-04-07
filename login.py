import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox,simpledialog
from PIL import Image, ImageTk
from container import Container

class Login(tk.Frame):
    image = None
    db_name = "database.db"

    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.pack()
        self.place(x=0, y=0, width=1100, height=650)
        self.controlador = controlador
        self.widgets()

    def validacion(self, user, pas):
        return len(user) > 0 and len(pas) > 0

    def login(self):
        user = self.username.get()
        pas = self.password.get()

        if self.validacion(user, pas):
            consulta = "SELECT * FROM usuarios WHERE username=? AND password=?"
            parametros = (user, pas)

            try:
                with sqlite3.connect(self.db_name) as conn:
                    cursor = conn.cursor()
                    cursor.execute(consulta, parametros)
                    result = cursor.fetchall()

                    if result:
                        self.control1()
                    else:
                        self.username.delete(0, 'end')
                        self.password.delete(0, 'end')
                        messagebox.showerror(title="Error", message="Usuario y/o contraseña incorrecta")
            except sqlite3.Error as e:
                messagebox.showerror(title="Error", message="No se conectó a la base de datos: {}".format(e))
        else:
            messagebox.showerror(title="Error", message="Llene todas las casillas")

    def control1(self):
        self.controlador.show_frame(Container)

    def control2(self):
        self.controlador.show_frame(Registro)

    def widgets(self):
        
#===============Frame izquierdo=================================================================================#
        fondo = tk.Frame(self, bg="#C6D9E3")
        fondo.pack()
        fondo.place(x=0, y=0, width=1100, height=650)

        self.logo_image = Image.open("imagenes/logo1.png")
        self.logo_image = self.logo_image.resize((200, 200))
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = ttk.Label(fondo, image=self.logo_image, background="#C6D9E3")
        self.logo_label.place(x=450, y=20)

        self.logo_image1 = Image.open("imagenes/innova1.png")
        self.logo_image1 = self.logo_image1.resize((300, 100))
        self.logo_image1 = ImageTk.PhotoImage(self.logo_image1)
        self.logo_label1 = ttk.Label(fondo, image=self.logo_image1, background="#C6D9E3")
        self.logo_label1.place(x=10, y=20)

        user = ttk.Label(fondo, text="Nombre de usuario", font="sans 16 bold", background="#C6D9E3")
        user.place(x=450, y=250)
        self.username = ttk.Entry(fondo, font="sans 16 bold")
        self.username.place(x=450, y=290, width=240, height=40)

        pas = ttk.Label(fondo, text="Contraseña", font="sans 16 bold", background="#C6D9E3")
        pas.place(x=450, y=340)
        self.password = ttk.Entry(fondo, show="*", font="sans 16 bold")
        self.password.place(x=450, y=380, width=240, height=40)

        imagen_pil = Image.open("icono/iniciar.png")
        imagen_resize = imagen_pil.resize((30, 30))
        imagen_tk = ImageTk.PhotoImage(imagen_resize)

        btn1 = tk.Button(fondo, text="Iniciar", bg="gray", image=imagen_tk, compound=tk.LEFT, command=self.login,font=("sans", 16, "bold"))
        btn1.image = imagen_tk
        btn1.place(x=450, y=440, width=240, height=40)

        imagen_pil1 = Image.open("icono/registrar.png")
        imagen_resize1 = imagen_pil1.resize((30, 30))
        imagen_tk1 = ImageTk.PhotoImage(imagen_resize1)

        btn2 = tk.Button(fondo, text="Registrar", bg="gray", image=imagen_tk1, compound=tk.LEFT, command=self.control2,font=("sans", 16, "bold"))
        btn2.image = imagen_tk1
        btn2.place(x=450, y=500, width=240, height=40)

#==================================================================================================================# 
        
class Registro(tk.Frame):
    image = None
    db_name = "database.db"

    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.pack()
        self.place(x=0, y=0, width=1100, height=650)
        self.controlador = controlador
        self.widgets()

    def validacion(self, user, pas):
        return len(user) > 0 and len(pas) > 0

    def create_table(self):
        consulta = '''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            name TEXT,
            password TEXT
        )
        '''
        self.eje_consulta(consulta)

    def eje_consulta(self, consulta, parametros=()):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(consulta, parametros)
                conn.commit()
        except sqlite3.Error as e:
            messagebox.showerror(title="Error", message="Error al ejecutar la consulta: {}".format(e))

    def registro(self):
        user = self.username.get()
        pas = self.password.get()
        key = self.key.get()
        if self.validacion(user, pas):
            if len(pas) < 6:
                messagebox.showinfo(title="Error", message="Contraseña demasiado corta")
                self.username.delete(0, 'end')
                self.password.delete(0, 'end')
            else:
                if key=="1234":
                    self.create_table()  # Asegurarse de que la tabla existe
                    consulta = "INSERT INTO usuarios VALUES (?,?,?)"
                    parametros = (None, user, pas)
                    self.eje_consulta(consulta, parametros)
                    self.control1()
                else:
                    messagebox.showerror(title="Registro",message="Error al ingresar el código de registro")
        else:
            messagebox.showerror(title="Error", message="Llene sus datos")

    def control1(self):
        self.controlador.show_frame(Container)

    def control2(self):
        self.controlador.show_frame(Login)

    def widgets(self):
        
#==============Frame izquierdo========================================================================================# 
        fondo = Frame(self, bg="#C6D9E3")
        fondo.pack()
        fondo.place(x=0, y=0, width=1100, height=650)
        
        self.logo_image = Image.open("imagenes/logo1.png")
        self.logo_image = self.logo_image.resize((200, 200))
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = tk.Label(fondo,image=self.logo_image, bg="#C6D9E3")
        self.logo_label.place(x=450, y=20)
        
        self.logo_image1 = Image.open("imagenes/innova1.png")
        self.logo_image1 = self.logo_image1.resize((300, 100))
        self.logo_image1 = ImageTk.PhotoImage(self.logo_image1)
        self.logo_label1 = ttk.Label(fondo, image=self.logo_image1, background="#C6D9E3")
        self.logo_label1.place(x=10, y=20)
        
        user = Label(fondo, text="Nombre de usuario", font="sans 16 bold", bg="#C6D9E3")
        user.place(x=450, y=230)
        self.username = ttk.Entry(fondo, font="sans 16 bold")
        self.username.place(x=450, y=270, width=240, height=40)
        
        pas = Label(fondo, text="Contraseña", font="sans 16 bold", bg="#C6D9E3")
        pas.place(x=450, y=320)
        self.password = ttk.Entry(fondo, show="*", font="16")
        self.password.place(x=450, y=360, width=240, height=40)
        
        key = Label(fondo, text="Código de registro", font="sans 16 bold", bg="#C6D9E3")
        key.place(x=450, y=400)
        self.key = ttk.Entry(fondo, show="*", font="16")
        self.key.place(x=450, y=440, width=240, height=40)

        imagen_pil = Image.open("icono/registrar.png")
        imagen_resize3 = imagen_pil.resize((30, 30))
        imagen_tk = ImageTk.PhotoImage(imagen_resize3)
        
        btn3 = Button(fondo, bg="gray", fg="black", text="Registrarse", font="sans 16 bold", command=self.registro)
        btn3.config(image=imagen_tk, compound=LEFT, padx=10)
        btn3.image = imagen_tk
        btn3.place(x=450, y=500, width=240, height=40)

        imagen_pil = Image.open("icono/regresar.png")
        imagen_resize4 = imagen_pil.resize((30, 30))
        imagen_tk = ImageTk.PhotoImage(imagen_resize4)

        btn4 = Button(fondo, bg="gray", fg="black", text="Regresar", font="sans 16 bold", command=self.control2)
        btn4.config(image=imagen_tk, compound=LEFT, padx=10)
        btn4.image = imagen_tk
        btn4.place(x=450, y=560, width=240, height=40)

#======================================================================================================================#