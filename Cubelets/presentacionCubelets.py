# -*- coding: utf-8 -*-
#Autor:Juan Eduardo Chávez, CDMX., Febrero 2018.
#Vesión:1.0
import random
from naoqi import ALProxy
from naoqi import ALModule
from naoqi import ALBroker
import threading
import time
import subprocess
"""
 PRESENTACIÓN EXPOSICIÓN DE LOS CUBELETS POR EL ROBOT NAO

"""
class Presentacion():

    def __init__(self):
        #Modifiqué esta ip por la de su robot
        robot_ip="127.0.0.1"      #ip robot NAO
        robot_port=53191               #Modifiqué puerto por el de su robot

        try:
            self.memoria = ALProxy("ALMemory", robot_ip, robot_port)
            self.mover = ALProxy("ALMotion",robot_ip,robot_port ) 
            self.tts = ALProxy("ALTextToSpeech",robot_ip,robot_port ) 
            self.postura = ALProxy("ALRobotPosture",robot_ip,robot_port) 
            self.animatedSpeechProxy = ALProxy("ALAnimatedSpeech",robot_ip, robot_port)
            self.audio = ALProxy("ALAudioPlayer", robot_ip, robot_port)
        except Exception, e:
            print "Error al crear el proxy------------"
            print "Error: ", e
        else:
            print "¡Conexión Exitosa!"
            #Creamos un ciclo FOR quien se encargara de abrir todas las imágenes y los speech.
            for x in xrange(0,25): #Rango de número de imágenes a mostrar
                hilo1 = threading.Thread(target=self.abreimagen(x))#Preparamos el hilo que abrira la imagen.
                hilo1.start() #Iniciamos el hilo de la imagen 
                hilo2 = threading.Thread(target=self.speech(x)) #Preparamos el hilo del speech
                hilo2.start()   #Iniciamos el hilo del speech
                pass

            hilo1 = threading.Thread(target=self.abreimagen("final"))
            hilo1.start()
            hilo2 = threading.Thread(target=self.animatedSpeechProxy.say("Gracias por tu atención, espero que hayas apendido algo nuevo"))
            hilo2.start()
            self.p.kill()
        pass

    #Esta función nos ayudara a reproducir un sonido.
    #@nombre=nombre del sonido
    def reproducirSonido(self, nombre):

        sonidoId = self.audio.loadFile("sonidos/"+nombre+".wav")
        self.audio.play(sonidoId)

        pass

    #abreimagen recibe parametro
    #@num número de imagen guardada en la carpeta img
    def abreimagen(self, num):
        self.postura.goToPosture("Stand", 0.5) #Iniciamos el robot en Stand, para iniciar las preguntas.
        try:
            #Abrimos la imagen en un subproceso para que pueda ejecutarse a la par con la voz-movimiento de NAO
            var="img/0"+str(num)+".gif"
            self.p = subprocess.Popen(["python", "abreImagen.py",var])
            pass

        except:
            print("No ha sido posible cargar la imagen")

        pass
    
    def speech(self, num):
        #@text: vector que contiene los diálogos que serán ejecutados en voz por el robot NAO
        text=["Hola, hoy estoy aquí para platicarle un poco sobre los Cubelet, unos pequeños cubos con los cuales puedes crear tus propios robot, de una de manera muy fácil y divertida",
                "¡y de seguro te preguntarás!, ¿Qué son los cubelets?",
                "Los Cubelets son cubos con electrónica incluída, que hacen una tarea en particular en la forma que se conecten con otros cubos. Por ejemplo, se tiene un sensor estándar, la lógica correspondiente y un actuador en un cubo de plástico que se conecta con otros vía imanes. Se pueden armar robots que hagan tareas específicas muy fácilmente.",
                "Para entender un poco más a los Cubelets, es necesario conocerlos a todos, existen en total 18 diferentes cubelets, y se dividen en tres tipos: los cubelets de sentido que son de color negro, cubelets de acción que son de color claro y cubelets de procesamiento que son de varios colores",
                "La mayoría de los Cubelets tienen cinco lados de conexión y un lado especial, que identifica la función de ese Cubelet. Otros tienen seis lados de conexión y su función está indicada por su color. Todos los Cubelets tiene una pequeña luz LED en una esquina. Cuando el Cubelet es parte de un robot y el cubo de batería del robot está encendido, la luz LED se enciende",
                "A continuación te presento los Cubelets uno por uno para entenderlos mejor. El cubo de batería tiene un pequeño interruptor. Cuando se desplaza hasta el O, el cubo de batería está apagado. Desliza el interruptor hacia la línea y se encenderá su función es alimentar de energía al robot",
                "Conociendo a los cubelets de sentido. Cubelets distancia: detecta a qué distancia está de un objeto; este utiliza una luz infrarroja y es precisa entre 10 y 80 cm.",
                "Cubelet temperatura: contiene un pequeño termómetro (en realidad, es un termostato) que detecta la temperatura.",
                "Cubelet brillo: este detecta la cantidad de luz que llega a su sensor; tiene una fotocélula analógica que responde a diferentes condiciones de luz",
                "Cubelet potenciómetro: ubicado a un lado de sus regula los datos",
                "Conociendo los Cubelets de procesamiento. Cubelet mínimo: puede aceptar cualquier cantidad de datos, pero sólo valida el valor más pequeño que recibe.",
                "Cubelet máximo: acepta muchas entradas diferentes, pero sólo válida al que tiene el mayor valor.",
                "Cubelet inversor: calcula un valor que es el opuesto de los valores que recibe; los valores bajos se convierten en altos y viceversa.",
                "Cubelet bloqueador: es una barrera datos; se usa para conectar módulos independientes sin que interfiera la funcionalidad de uno con el otro.",
                "Cubelet Pasivo: este cubelet solo sirve como un cable, se usa para hacer más grande nuestro robot.",
                "Conociendo los cubelets de acción. Cubelets gráfico de barras: es algo así como las de un ecualizador; es una forma de representar valores en luz",
                "Cubelet rotor: posee un dispositivo que gira en una de sus caras, y gira de acuerdo al cubo de programación y al de detección.",
                "Cubelet movimiento: es un bloque con ruedas para conducir alrededor en superficies planas; contiene un motor y ruedas de rodillos para el movimiento sobre una superficie horizontal; el Cubelet movimiento sólo se mueve en una dirección.",
                "Cubelet altavoz: este emite sonidos con diferentes intensidades según los valores de entrada que se le den, ideal para realizar robots ruidosos; contiene un altavoz y un pequeño amplificador.",
                "Cubelet linterna: emite un haz de luz concentrado desde un LED blanco de gran alcance.",
                "Cubelet Bluetooth, El cubo Bluetooth es un cubo con habilidades especiales. Tiene una radio Bluetooth dentro que permite que dispositivos como un ordenador, tableta o teléfono inteligente se comuniquen con Cubelets. Se utiliza para programar los cubelets de forma más especializada",
                "Vamos a definir ¿Qué es un Robot? para entender mejor lo que estamos platicando. Un robot es una máquina que percibe su entorno y actúa acorde al mismo. Cada robot necesita un cubo de sentido y un cubo de acción. Recuerda: los cubos de sentido son negros y los cubos de acción son claros.",
                "Empieza lo divertido, vamos a construir nuestro primer robot, Todos los robots necesitan energía. El cubo azul-gris es el cubo de la batería. Para construir un robot, necesitarás un cubo gris, un cubo negro y un cubo claro. ¡Solo tienes que juntarlos para construir un robot!  Nota: Arma tu robot como se muestra en la imagen",
                "Probando la funcionalidad de mi robot: Cubre el cubo sensor de luminosidad con tu mano y la intensidad de la linterna es menor. Aleja tu mano del cubo y la luz de la linterna se vuelve más intensa. Es muy fácil crear un robot con Cubelet, puedes intercambiar los cubos por otros como el de distancia, calor etc. para observar sus comportamientos",
                "Seguro te preguntaras, como rayos funcionan, ¿Cómo se transmiten los valores? enseguida te muestro un ejemplo. Cada cubo de sentido negro detecta alguna propiedad de su entorno y la convierte en un valor. Cada cubo de sentido le transmite su valor a todos sus vecinos. Puedes verlos hablar por el parpadeo de las luces verdes en cada cubo. Nota:la flecha muestra cómo un valor se transmite desde el cubo sensor de luminosidad al cubo de acción de luz.",
                "Cubos pensantes o de procesamiento. Los cubos pensantes o de procesamiento son de varios colores. Dado que los Robots son máquinas que detectan primero, luego piensan y luego actúan, necesitamos estar seguros de que los cubos de procesamiento se colocan entre el cubo de sentido y el cubo de acción con los que quieren interactuar.",
                "Para conocer más este tipo de cubos, vamos armar un robot con un cubo inversor Cuando ponemos el cubo de procesamiento inversor en el robot, los valores pasan a través del cubo de sentido al cubo de acción. Cuando el cubo sensor de luminosidad detecta mucha luz, transmite un valor alto, el cual se transforma en un valor bajo y pasa al cubo de acción de la luz, que reduce su intensidad.",
                ""]


        #Ejecutamos el metodo de animación y voz con el siguiente metodo.
        self.animatedSpeechProxy.say(text[num]+"^mode(contextual)") 
        #Despues de terminar la voz y animación del robot, cerramos la imagen para que pueda lanzarse otra.
        time.sleep(1)
        self.p.kill()
        pass

    """
        Obtener datos de los sensores como el touch y bumper
        para eso hacemos uso de la función getData
    """
    def obtenerTouch(self):
        while(True):
            frente=self.memoria.getData("FrontTactilTouched")
            pieIzquierdo=self.memoria.getData("LeftBumperPressed")
            pieDerecho=self.memoria.getData("RightBumperPressed")
            if (frente==1):
                print "frente"
                return "frente"
                pass
            if (pieDerecho==1):
                print "pie derecho"
                return "pieDerecho"
                pass
            if (pieIzquierdo==1):
                print "pie Izquierdo"
                return "pieIzquierdo"
                pass
        pass

    """
        Evaluamos las respuestas obtenidad por los touch y bumper y evaluamos que sea correcta o 
        incorrecta.
        @matriz respuestas:contiene la respuesta correcta y el número de imagen correspondiente
        las primeras posiciones de la matriz se mantienen en null

        @res: respuesta obtenida
        @return: correcto e incorrecto segun sea el caso y la matriz 
        en posición de la imagen correcta.
    """
    def tocaste(self, res):

        respuestas =[["null","null","null"],
                     ["null","pieDerecho","10"],
                     ["null","pieIzquierdo","6"],
                     ["null","frente","12"],
                     ["null","pieIzquierdo","18"]]

        resCorrecta = respuestas[res][1]
        print "Respuesta Correcta: "+ resCorrecta
        resUsuario= self.obtenerTouch()
        print "Preciono: " + resUsuario
        if (resUsuario==resCorrecta):
            print "correcto"
            return "correcto",respuestas[res][2]
            pass
        else: 
            print "incorrecto"
            return "incorrecto",respuestas[res][2]
            pass

        pass

    """
        Voz y movimiento según sea la pregunta a lanzar.
        @txt: contiene los dialogos a decir
        @hilo1: abre la imagen correspondiente al diálogo
        @hilo2 lanza la animación y voz con el robot
    """
    def speechPreguntas(self):
        text=["Bueno, espero que allás aprendido algo sobre la robótica, es hora de probar tus conocimientos adquiridos. Instrucciones: yo pondre en la pantalla preguntas del tema visto, y tu podras contestar tocando alguna de mis partes, como pie, cabeza o mano.",
              "Pregunta, ¿Cuántos tipos de cubos existen ?, responde tocando alguna de mis partes.",
              "Pregunta. ¿Qué cubo detecta a qué distancia está de un objeto?, responde tocando alguna de mis partes.",
              "Pregunta. ¿Como funcionan los robot?,responde tocando alguna de mis partes. ",
              "Pregunta. ¿Cual es un tipo de robot?"]
        
        hilo1 = threading.Thread(target=self.abreimagen("p00"))
        hilo1.start()
        hilo2 = threading.Thread(target=self.animatedSpeechProxy.say(text[0]))
        hilo2.start()
        self.p.kill()

        #Cramos un  ciclo con el numero de preguntas que se van a lanzar en pantalla, en este caso 5 preguntas.!
        for x in xrange(1,3):
            hilo3 = threading.Thread(target=self.abreimagen("p0"+str(x)))
            hilo3.start()
            hilo4 = threading.Thread(target=self.animatedSpeechProxy.say(text[1]))
            hilo4.start()

            #obtener respuesta, al tocar alguna de sus partes de NAO
            var = self.tocaste(x)
            print "respuesta correcta: "+ var[0]
            print "de la imagen: "+ var[1]
            #Comparación si la parte es la correcta
            if var[0] == "correcto":
                #Ejecutar acción en caso de que sea correcto
                print "¡Felicidades!"
                self.p.kill()
                hilo1 = threading.Thread(target=self.abreimagen("correcto"))
                hilo1.start()
                #self.reproducirSonido("Correcto")
                hilo2 = threading.Thread(target=self.animatedSpeechProxy.say("!Genial, muy bien felicidades! ^mode(contextual)"))
                hilo2.start()
                time.sleep(3)
                #Una vez terminado el speech cerramos la imagen, en caso de que se valla a mostrar otra
                self.p.kill()
                pass
            else:
                #ejecutar acción en caso de que la respuesta sea incorrecta
                print "¡oh! ¡creo que se te has equivocado!"
                self.p.kill()
                #preparamos el hilo con imagen de respuesta incorrectaa
                hilo1 = threading.Thread(target=self.abreimagen("incorrecto"))
                #inicia el hilo de la imagen
                hilo1.start()
                self.reproducirSonido("Incorrecto")
                print "¡Imagen incorrecto!"
                #Preparamos el hilo del speech 
                hilo2 = threading.Thread(target=self.animatedSpeechProxy.say("¡oh no!, te has equivocado la respuesta es incorrecta.! ^mode(contextual)"))
                #Iniciamos el hilo del speech
                hilo2.start()
                #Cerramos el hilo del speech.
                self.p.kill()
                hilo1 = threading.Thread(target=self.abreimagen(str(var[1])))
                #inicia el hilo de la imagen
                hilo1.start()
                hilo2 = threading.Thread(target=self.animatedSpeechProxy.say("La respuesta correcta se muestra en la siguiente imagen"))
                #Iniciamos el hilo del speech
                hilo2.start()
                time.sleep(5)
                self.p.kill()

            pass
        pass

    def posturas(self, postura):
        self.postura.goToPosture(str(postura), 0.5)
        pass


def main():
    #Cremos un objeto de la clase presentación para poder llamar a los demas metodos.
    mi_app = Presentacion()
    return(0)

#pass:sLQ4XaN5
if __name__ == '__main__':
    main()


