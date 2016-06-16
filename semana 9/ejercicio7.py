#	Programa que grafica un plogono de N lados ingreado por el usuario
import turtle
lados= int(input("Ingrese numero de lados: "))
angulo= (180-(180/lados))
t=turtle.Pen()
for x in range(1,lados+1):
	t.forward(200)
	t.left(angulo)
turtle.getscreen()._root.mainloop()