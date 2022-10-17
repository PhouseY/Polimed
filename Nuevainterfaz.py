
from ast import Try
from distutils.cmd import Command
from email import message
from email.mime import image
from msilib.schema import Icon
from tkinter import *
from tkinter import messagebox
from turtle import title
from PIL import ImageTk, Image
import pymysql

class Login_Polimed:
    ####################### DIMENSIONES DE LA PANTALLA Y COLOR DEL FONDO ############
    def __init__(self, ventana):
        self.ventana = ventana
        self.NombreUsuario= StringVar()
        self.ContraseñaUsuario= StringVar()
        self.ventana.title("PoliMed")
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+450+250"%(w/2,h/2))
        self.ventana.config(bg="light slate blue") 
        self.ventana.resizable(1,1)
        self.ventana.attributes("-fullscreen")

        #################### IMAGEN DE LOGO TIPO ########################
    
        self.image = Image.open("a-heart-2001744_1920.png")
        self.image = self.image.resize((150,150),Image.Resampling.LANCZOS)
        Lg_Polimed = ImageTk.PhotoImage(self.image)
        label_Logo = Label(ventana, image = Lg_Polimed, bg="light slate blue")
        label_Logo.image = Lg_Polimed
        label_Logo.pack()

        ##################### TITULOS, ENTRADAS, BOTONES ######################
        self.Primer_titulo = Label (ventana, text= "Poli-Med", font=("Comic Sans MS",30,), bg="light slate blue").pack()
        self.Titulo_De_Usuario = Label(ventana, text = "Usuario", font = ("Comic Sans MS",14,), bg = "light slate blue").pack()
        self.Primera_Entrada = Entry(ventana, font = ("Comic Sans MS",12,), textvariable= self.NombreUsuario).pack()
        self.Espacio_Emergencia= Label(ventana, text = " ", font=("Comic Sans MS",14), bg = "light slate blue").pack()
        self.Titulo_De_Password = Label (ventana, text = "Contraseña", font=("Comic Sans MS",14), bg = "light slate blue").pack()
        self.Segunda_Entrada = Entry(ventana, font= ("Comic Sans MS",12,), show="*", textvariable= self.ContraseñaUsuario)
       
        self.Segunda_Entrada.pack()  
        self.Espacio_Emergencia2= Label(ventana, text = " ", font=("Comic Sans MS",14), bg = "light slate blue").pack()
        self.Boton_Ingreso = Button (ventana, text= "Ingresar", font = ("Comic Sans MS", 16), bg = "light slate blue", command= self.Datos_Para_Validar).pack()
        self.Espacio_Emergencia3 = Label(ventana, text="", bg = "light slate blue").pack()
        self.Boton_Registro = Button (ventana, text= "Registrarse", font = ("Comic Sans MS", 16), bg = "light slate blue", command= self.Conexion).pack()
        ####################### CONEXION CON BASE DE DATOS ############################################
    def Conexion(self):
        self.bd = pymysql.connect(
            user = "root",
            host = "localhost",
            passwd= "",
            db = "usuariospoli"
        )
        self.fcursor = self.bd.cursor()
        
        self.sql = "INSERT INTO tablausuarios (Usuarios, Contra) VALUE ('{0}','{1}')".format(self.NombreUsuario.get(), self.ContraseñaUsuario.get())
        
        try:
            self.fcursor.execute(self.sql)
            self.bd.commit()
            messagebox.showinfo(message="Registro Realizado", title="Aviso")
            
        except:
            self.bd.rollback()
            messagebox.showinfo(message= "Registro NO Realizado", title= "Aviso")
        
        self.bd.close()
    ############################# VALIDACION DE DATOS DE USUARIO ####################################################    
    def Datos_Para_Validar(self):
        self.bd = pymysql.connect(
            user = "root",
            host = "localhost",
            passwd= "",
            db = "usuariospoli"
        )
        
        self.fcursor = self.bd.cursor()
        
        self.fcursor.execute("SELECT Contra FROM tablausuarios WHERE Usuarios='"+self.NombreUsuario.get()+"'and Contra='"+self.ContraseñaUsuario.get()+"'")
        
        if self.fcursor.fetchall() and self.ventana:
            self.ventana2 = Toplevel()
            w, h = self.ventana2.winfo_screenwidth(), self.ventana2.winfo_screenheight()
            self.ventana2.geometry("%dx%d+450+250"%(w/2,h/2))
            self.ventana2.config(bg="light slate blue") 
            self.ventana2.title("Menú de Selección")
            self.ventana2.resizable(1,1)
            self.ventana2.attributes("-fullscreen")
            self.ventana.withdraw()
            self.ventana2.mainloop()
            
            
        else:
            messagebox.showinfo(message="Contraseña o Usuarios Incorrectos", title= "Aviso de loggin")
            
        self.bd.close()
    
    def Cerrar_ventana(self):
        self.ventana.destroy()
    
        ####################### Definir Funciones de nuevas Ventana ####################################
    #def segunda_Ventana(self):
        
        
        
############## HERENCIA DE VENTANA Y MAINLOOP#############################
def inicio():
    ventana = Tk()
    Login_Polimed(ventana)

    ventana.mainloop()

if __name__ == "__main__":
    inicio()



