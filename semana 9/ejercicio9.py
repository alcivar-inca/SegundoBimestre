#	PROGRAMA PARA GRAFICAR UN poligono CON LOS DATOS INGRESADOS POR EL USUARIO
import turtle

def poligono(nl , l, ang):
	t=turtle.Pen()
	for x in range (0,nl):
		t.forward(l)
		t.left(ang)
	turtle.getscreen()._root.mainloop()

numLados=int(input("Ingrese el numero de lados (1 -50): "))
lado=int(input("Ingrerse el valor del lado: "))
angulo=360/numLados

poligono(numLados, lado, angulo)

