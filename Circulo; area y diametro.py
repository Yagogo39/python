#Hacer un programa que reciba como dato el radio de un circulo. Hallar el area y el diametro de dicha figura.
radio = float(input ("Ingrese el radio del circulo en centimetros: "))

def Hallar_area (radio):
    return 3.1416 * (radio * radio)

def Hallar_Diametro(radio):
    return 2 * radio

print ("El area del circulo es: ", Hallar_area(radio), "cm")
print("El diametro del circulo es: ", Hallar_Diametro(radio), "cm")