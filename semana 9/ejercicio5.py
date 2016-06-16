#	Programa que grafica un poligono de N lados ingresados por el usuario
import turtle


lados=int(input("Ingrerse el numero de lados: "))
angulo=360/lados

t=turtle.Pen()

for x in range (1,lados+1):
	t.forward(200)
	t.left(angulo)
turtle.getscreen()._root.mainloop()