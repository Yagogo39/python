#Juego Piedra, Papel o Tijera 
import random
def Titulo(Mensaje):
    print("\033[1; 31n" + Mensaje + "\033[0n")
    
def inputVerde(Mensaje):
    return input ("\033[1; 32n" + Mensaje + "\033[0n")
def RespuestaAmarilla(Bot, Mensaje, OpcionBot, Texto):
    return print("\033[1; 33n" + Bot + Mensaje +  OpcionBot + Texto + "\033[0n")
def CentrarTexto(Texto):
    Texto= (Texto, )
    AnchoConsola = 80
    TextoCentrado = Texto[0].center(AnchoConsola)
    return Titulo(TextoCentrado)

Opciones = ["piedra", "papel", "tijera"]
NombresBot = ['Hulk', 'Capitan America', 'Thor', 'Doctor Strange', 'Iron Man', 'SpiderMan', 'Capitana Marvel', 'Black Panter']
CentrarTexto('martL7 Piedra, Papel, Tijera')

def jugar():
    Bot = random.choice(NombresBot)
    print("Hola, soy ", Bot, " preparate")
    Usuario = inputVerde('Elige Piedra, Papel, Tijera: ').lower()
    Maquina =  random.choice(Opciones)
    
    if Usuario==Maquina:
        RespuestaAmarilla(Bot, " escogio ", Maquina, " por lo tanto empataron")
    elif Usuario== "piedra" and Maquina == "tijera":
            RespuestaAmarilla(Bot, " escogio ", Maquina, " por lo tanto ganaste")
    elif Usuario == "papel" and Maquina == "piedra":
        RespuestaAmarilla(Bot, " escogio ", Maquina, " por lo tanto ganaste")
    elif Usuario == "tijera" and Maquina =="papel":
        RespuestaAmarilla(Bot, " escogio ", Maquina, " por lo tanto ganaste")
    elif Usuario=="piedra" and Maquina=="papel":
        RespuestaAmarilla(Bot, " escogio ", Maquina, " por lo tanto perdiste")     
    elif Usuario == "papel" and Maquina=="tijera":
        RespuestaAmarilla(Bot, " escogio ", Maquina, " por lo tanto perdiste") 
    elif Usuario == "tijera" and Maquina == "piedra":
        RespuestaAmarilla(Bot, " escogio ", Maquina, " por lo tanto perdiste") 
    else:
        Titulo("esa no es una opcion valida")
        
    NuevoJuego = inputVerde("¿desea jugar de nuevo? (si/no): "). lower()
    if NuevoJuego != "si":
        print ("\033[1; 34n" + 'chao, diviertete con un juego mejor, pero antes califica mi juego' + "\033[0n")  
        quit()
        
Reinicio = True
while Reinicio:
    jugar()