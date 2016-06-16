#	Ejercicio 1 (IMPORTANDO LIBRERYA TIME)
import time

t = time.localtime()
year=t[0]
mont=t[1]
day= t[2]
hora=t[3]
minuto =t[4]

print("Fecha: "+ str(year) + " / " + str(mont) + " /" + str(day))
print("Hora: " + str(hora) + " h " + str(minuto))