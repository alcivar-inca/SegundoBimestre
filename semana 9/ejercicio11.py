#	PROGRAMA PARA CARGAR IMAGENES CON TKINTER

from Tkinter import*
tk= Tk()

canvas=Canvas(tk, width=400, height=400)
canvas.pack()


my_image=PhotoImage(file="photo.gif")
canvas.create_image(0,0, anchor= NW, image=my_image)
tk.mainloop()