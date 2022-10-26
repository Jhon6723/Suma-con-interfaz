from tkinter import Tk, Label, Button
class VentanaEjemplo:
    def __init__(self, master):
        self.master = master
        master.title("Suma de dos numeros")
        self.etiqueta = Label(master, text="Esta es la suma")
        self.etiqueta.pack()
        self.botonSaludo = Button(master, text="Sumar", command=self.sumar)
        self.botonSaludo.pack()
        self.botonCerrar = Button(master, text="Cerrar", command=master.quit)
        self.botonCerrar.pack()
    def sumar(self):
        a=int(input("Ingresa tu valor: "))
        b=int(input("ingresa tu segundo valor: "))
        resultado=a+b
        print("Este es el resultado: ", resultado)
root = Tk()
miVentana = VentanaEjemplo(root)
root.mainloop()