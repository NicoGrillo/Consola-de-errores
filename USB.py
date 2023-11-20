#Librerias
from tkinter import Tk   #Libreria grafica
import tkinter
from pymodbus.client import ModbusSerialClient
import serial
import time

# Configure serial communication
ser = serial.Serial(
    port='COM1',  # Change this to your USB port
    baudrate=9600,
    bytesize=8,
    parity='N',
    stopbits=1,
    timeout=1
)

# Configure Modbus communication
client = ModbusSerialClient(
    method='rtu',
    port='COM1',  # Change this to your USB port
    baudrate=9600,
    timeout=1,
    stopbits=1,
    bytesize=8,
    parity='N'
)

#---------------Funcion para leer la data---------------
def read_data():
    # Read data from the Modbus device
    result = client.read_input_registers(address=0, count=8, unit=1)

    if result.isError():
        print("Error reading data:", result)
        return None

    # Extract the data
    data = result.registers
    return data

#--------------Funcion para guardar la data--------------
def store_data(data):
    # For this example, we print the data, but you can save it to a file, database, etc.
    print("Received data:", data)

#----------------Funcion cerrar ventana------------------
def salir():
    try:
        ser.close()
    except:
        ser.open()
    ventana.destroy()
    
#------------Funcion para abrir el puerto----------------
def open_port():
    ser.open()
  
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

# Main loop
try:
    while True:
        # Read data from the Modbus device
        data = read_data()

        if data is not None:
            # Store the data
            store_data(data)

        # Wait for some time before the next read
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Close the serial port
    ser.close()
    # Close the Modbus client
    client.close()