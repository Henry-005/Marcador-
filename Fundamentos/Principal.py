import serial
from tkinter import *
import pygame
import random

pygame.mixer.init()
golsound = pygame.mixer.Sound("audios/gol.mp3")
pitaso = pygame.mixer.Sound("audios/pitido.mp3")
porterosound = pygame.mixer.Sound("audios/keylor.mp3")

ser = serial.Serial('COM4', 9600)  # Ajusta 'COM3' al puerto adecuado para tu configuración

def enviar_datos(equipo, marcador, var_mode):
    data = bytes([equipo, marcador, var_mode, 0])
    ser.write(data)

def marcador(contador1, contador2, equipo1, equipo2):
    win = Tk()
    win.title("Marcador")
    win.minsize(450, 225)
    win.resizable(0, 0)
    img = PhotoImage(file=("imagenes\\Num1.png"))

    frame1 = Frame(win)
    frame1.pack(side=LEFT)
    frame2 = Frame(win)
    frame2.pack(side=LEFT)

    can = Canvas(frame1, width=225, height=250, bg="blue")
    can.pack()
    can2 = Canvas(frame2, width=225, height=250, bg="red")
    can2.pack()

    nombre = "imagenes\\Num" + str(contador1) + ".png"  #
    img = PhotoImage(file=nombre)  # carga la imagen con su respectivo nombre
    lbl = Label(frame1, image=img)
    lbl.place(x=25, y=50)

    nombre2 = "imagenes\\Num" + str(contador2) + ".png"  #
    img2 = PhotoImage(file=nombre2)  # carga la imagen con su respectivo nombre
    lbl2 = Label(frame2, image=img2)
    lbl2.place(x=25, y=50)

    label1 = Label(frame1, text=equipo1, bg="white")
    label1.place(x=110, y=10)

    label2 = Label(frame2, text=equipo2, bg="white")
    label2.place(x=110, y=10)

    cont1 = contador1
    cont2 = contador2

    def mar1():
        porte = [["P1", "P2", "P3"], ["P4", "P5", "P6", ], ["P1", "P2"], ["P3", "P4"], ["P5", "P6"],
                 ["P1", "P3", "P5"], ["P2", "P4", "P6"]]
        portero = random.choice(porte)
        tir = ["P1", "P2", "P3", "P4", "P5", "P6"]
        tiro = random.choice(tir)
        print(f"El jugador tiro en {tiro} y el portero estaba en {portero}")
        if tiro not in portero:
            win.deiconify
            win.destroy()
            v = ["VAR", "NOVAR"]
            if random.choice(v) == "VAR":
                print("HAY VAR")
                pitaso.play()
                if contador1 == 2:
                    enviar_datos(1, 7, 1)
                    return ventana_marcador(7, contador2)
                elif contador1 == 1:
                    enviar_datos(1, 6, 1)
                    return ventana_marcador(6, contador2)
                elif contador1 == 0:
                    enviar_datos(1, 5, 1)
                    return ventana_marcador(5, contador2)
                else:
                    enviar_datos(1, contador1 - 3, 1)
                    return ventana_marcador(contador1 - 3, contador2)
            else:
                print("NO HAY VAR")
                golsound.play()
                enviar_datos(1, contador1 + 1, 0)
                ventana_marcador(contador1 + 1, contador2)
        else:
            print("El portero atajo")
            porterosound.play()

    def mar2():
        porte = [["P1", "P2", "P3"], ["P4", "P5", "P6", ], ["P1", "P2"], ["P3", "P4"], ["P5", "P6"],
                 ["P1", "P3", "P5"], ["P2", "P4", "P6"]]
        portero = random.choice(porte)
        tir = ["P1", "P2", "P3", "P4", "P5", "P6"]
        tiro = random.choice(tir)
        print(f"El jugador tiro en {tiro} y el portero estaba en {portero}")
        if tiro not in portero:
            win.deiconify
            win.destroy()
            v = ["VAR", "NOVAR"]
            if random.choice(v) == "VAR":
                print("HAY VAR")
                pitaso.play()
                if contador2 == 2:
                    enviar_datos(2, 7, 1)
                    return ventana_marcador(cont1, 7)
                elif contador2 == 1:
                    enviar_datos(2, 6, 1)
                    return ventana_marcador(cont1, 6)
                elif contador2 == 0:
                    enviar_datos(2, 5, 1)
                    return ventana_marcador(cont1, 5)
                else:
                    enviar_datos(2, contador2 - 3, 1)
                    return ventana_marcador(cont1, contador2 - 3)
            else:
                print("NO HAY VAR")
                golsound.play()
                enviar_datos(2, contador2 + 1, 0)
                ventana_marcador(cont1, contador2 + 1)
        else:
            print("El portero atajo")
            porterosound.play()

    btn1 = Button(frame1, text="Gol1", command=mar1)
    btn1.place(x=25, y=200)

    btn2 = Button(frame2, text="Gol2", command=mar2)
    btn2.place(x=25, y=200)

    win.mainloop()


def ventana_marcador(cont1, cont2):
    marcador(cont1, cont2, "NUEVO EQUIPO1", "NUEVO EQUIPO2")


ventana_marcador(0, 0)
