#Hacer un programa que convierta una unidad dada en dias, horas, minutos y segundos a segundos
dias = int(input("Ingrese la cantidad de dias: "))
horas = int(input("Ingrese la cantidad de horas: "))
minutos = int(input("Ingrese la cantidad de minutos: "))
segundos = int(input("Ingrese la cantidad de segundos: "))

def Calcular_Total_Segundos(num_dias, num_hrs, num_min, num_seg):
    segundos_totales = 0
    segundos_totales += num_seg
    segundos_totales += num_min * 60
    segundos_totales += num_hrs * 60 * 60
    segundos_totales += num_dias * 24 * 60 * 60
    
    return segundos_totales

segundos_totales = Calcular_Total_Segundos(dias, horas, minutos, segundos)

print ("La cantidad de segundos es:", segundos_totales) 
