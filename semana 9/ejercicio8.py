#	PROGRMA PARA DIBUJAR UN CUADRADO CON EL VALOR DEL LADO DEFINIDO POR EL USUARIO
import turtle


lado=int(input("Ingrerse el valor del lado del cuadrado: "))

t=turtle.Pen()

for x in range (1,5):
	t.forward(lado)
	t.left(90)
turtle.getscreen()._root.mainloop()