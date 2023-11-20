#Resumen: Este programa debe recibir datos por comunicación serial utilizando un puerto USB, mediante uso de cierto protocolo de comunicación.
#Recibido los datos, mediante un factor de conversión se obtiene un rango entre 0v y 10v, con su respectivo signo. Luego se pasan a grafico individual para cada señal.
#Requisitos: 
#*protocolo de comunicación sencillo 
#*hasta 8 variables que almacenen los datos de cada una de las 8 señales
#*factor de conversión
#*selector de tipo de señal (+-10v, 4-20mA, 0-10mA)
#*boton de On/Off
#*comunicacion USB
#*libreria para graficar

#Librerias
from tkinter import Tk   #Libreria grafica
import tkinter

#----------------Funcion cerrar ventana------------------
def salir():
    print("Salir")
    ventana.destroy()
    
#------------Funcion para abrir el puerto----------------
def open_port():
    #ser.open()
    print("Puerto abierto")
  
#--------------------Ventana-----------------------------
ventana = Tk()          #Esta variable es la ventana en sí
ventana.title("Consola de pruebas")         #Defino un titulo para la ventana
ventana.geometry("500x500")                 #Defino un tamaño por defecto de la ventana

#------------------Boton 1:Mensaje-----------------------
boton_1 = tkinter.Button(ventana,text="Abrir Puerto", command=open_port, fg="red") #command= Elige que funcionar ejecutar al presionar. fg= Color del texto del boton
boton_1.pack()
boton_1.place(x=10,y=465)       #Ubica el boton en VENTANA

#------------------Boton 2:Cerrar------------------------
boton_2 = tkinter.Button(ventana,text="Salir", command=salir, fg="blue") #command= Elige que funcionar ejecutar al presionar. fg= Color del texto del boton
boton_2.pack()
boton_2.place(x=455,y=465)       #Ubica el boton en VENTANA  

ventana.mainloop()               #Pone en pantalla la VENTANA y todo lo referido a él