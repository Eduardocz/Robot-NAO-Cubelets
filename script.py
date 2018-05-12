# -*- coding: utf-8 -*-
from Tkinter import*
import serial
import socket
import os
from array import *
from naoqi import ALProxy
from naoqi import ALModule
from naoqi import ALBroker
import Tkinter

"""
SCRIPT PARA CONECTAR EL ROBOT NAO CON EL ARDUINO, RECIBIR DATOS DEL ARDUINO E INTERPRETARLOS CON EL ROBOT

"""

class Nao:
 
    def __init__(self, master):   
        """
        Recursos para la interfaz de usuario.
        """
        frame = Frame(master)
        root.geometry("400x350+0+0")#Define el tamaño de la ventana
        root.title("Configuración") # Titulo de la ventana

        #Formulario para recibir datos de la interfaz, y poder conectar el nao con el arduino
        #Ip del robot
        self.frase1=Label(root,text="IP DEL ROBOT").place(x=135, y=80)
        self.campo_de_texto_ip = Tkinter.Entry(root)
        self.campo_de_texto_ip.place(x=100,y=100)
        #Puerto del robot
        self.frase2=Label(root,text="INGRESA EL PUERTO DEL ROBOT").place(x=80, y=120)
        self.campo_de_texto_port =Tkinter.Entry(root)
        self.campo_de_texto_port.place(x=100,y=140)
        #Puerto COM del arduino, verificar en que puerto COM esta conectado su Arduino,
        #En Windows se usas ej:COM1, COM2 en Linux eje: tty01, tty01 
        self.frase2=Label(root,text="INGRESA EL PUERTO COM DEL ARDUINO").place(x=60, y=160)
        self.campo_de_texto_com =Tkinter.Entry(root)
        self.campo_de_texto_com.place(x=100,y=180)
        #Boton para llamar a la funcion
        self.boton = Button(root,compound=TOP, text="Activar",height=2, width=5,
                           command=self.iniciarSv, activeforeground="#1d2d20").place(x=150,y=260)
    

        frame.pack() #Carga todos los elementos, de la vista

    def iniciarSv(self):

        #Instanciamos objetos que nos sirvirar para manipular al robot.
        try:
            self.mover = ALProxy("ALMotion", str(self.campo_de_texto_ip.get()), int(self.campo_de_texto_port.get()))
            self.memory = ALProxy("ALMemory",str(self.campo_de_texto_ip.get()), int(self.campo_de_texto_port.get()))
            self.tts = ALProxy("ALTextToSpeech",str(self.campo_de_texto_ip.get()), int(self.campo_de_texto_port.get()))
            self.postura = ALProxy("ALRobotPosture",str(self.campo_de_texto_ip.get()),int(self.campo_de_texto_port.get()))
            self.memoryProxy = ALProxy("ALMemory",str(self.campo_de_texto_ip.get()), int(self.campo_de_texto_port.get()))
            self.animatedSpeechProxy = ALProxy("ALAnimatedSpeech",str(self.campo_de_texto_ip.get()), int(self.campo_de_texto_port.get()))
        except Exception, e:
            #En caso de qu eocurra un error, mostramos el msj
            print "Error al crear el proxy------------"
            print "Error was: ", e
        else:
          #si nuestra creacion de objeto fu exitosa, imprimiremos el siguien te msj.
          print "¡Conexión Exitosa!"
          pass

        print"inicie a leer"
        self.postura.goToPosture("Stand", 0.6)
      # #Hacemos una conexion con el arduino, asignando el puerto COM, velocidad
      #   try:
      #       self.PuertoSerie = serial.Serial(self.campo_de_texto_com.get(), 9600)
        
      #   except Exception as e:
      #       print "No se establecio conexión "
         
        
      #animatedSpeechProxy.say("Hola soy Nao ^start(animations/Stand/Gestures/IDontKnow_2) Hola que tal")  #estable dialogo con animación 
      # #bandera para el control de while
      #   b=1
      #   while (b==1):
      #         # Leemos los datos hasta que encontarmos el final de linea
      #       sArduino = PuertoSerie.readline() #Alamacenamos los datos obtenidos del arduino en una variable
      #       cad=sArduino.rstrip('\n')
      #       #Comparamos obtenidos para procesarlos.
      #       if (cad.find("mano")>=0):
      #           self.postura.goToPosture("Stand", 0.6)
      #           pass
      #       if (cad.find("cabeza")>=0):
      #           self.postura.goToPosture("Sit", 0.6)
      #           pass
      #       if (cad.find("brazo")>=0):
      #           pass
      #       if(cad.find("pierna")>=0):
      #           pass
      #       if(cad.find("pie")>=0):
      #           pass
      #       if(cad.find("casco")>=0):
      #           pass
      #   pass
        
        
root = Tk()
root.resizable(0,0)#para que la ventana no se pueda maximizar

app = Nao(root) #Instanciamos la clase Nao

root.mainloop() 
