import tkinter as tk
from tkinter import TclError, ttk, SOLID
#must be flat, groove, raised, ridge, solid, or sunken
from PIL import ImageTk, Image


#def
def erase_data():
    print("Success_1!")
def charge_data():
    print("Success_2!")
def calculate_data():
    print("Success_3!")

def frame_Logo(container):
    frame_logo = tk.Frame(container, width = 400, height= 100, bg = '#3d6466')
    frame_logo.grid(row = 0, column=0)
    frame_logo.pack()
    #logo_frame widget
    image = Image.open("pngs/logo_etsime.png")
    image = image.resize((400, 100), Image.ANTIALIAS)
    logo_img = ImageTk.PhotoImage(image)
    logo_widget = tk.Label(frame_logo, image = logo_img, bg = '#3d6466')
    logo_widget.image = logo_img
    logo_widget.pack()

def frame_1(container):
    frame_1 = tk.Frame(container, width = 400, height= 100, bg = '#3d6466')
    frame_1.pack()
    #Label widget Frame_1
    frame_1.columnconfigure(0, weight=3)
    frame_1.columnconfigure(1, weight=6)
    #1
    label_a = tk.Label(frame_1,  text="Cliente: ", width = 17, font = ('Arial', 10), bg = '#3d6466', relief = SOLID
    ).grid(column=0, row=0, sticky=tk.W, pady=1)
    cliente = ttk.Entry(master = frame_1, width=37)
    cliente.focus()
    cliente.grid(column=1, row=0, sticky=tk.E)
    #2
    label_b = tk.Label(frame_1, text="Fecha Estudio: ", width = 17, font = ('Arial', 10), bg = '#3d6466', relief = SOLID
    ).grid(column=0, row=1, sticky=tk.W, pady=1)
    fecha_estudio = ttk.Entry(master = frame_1, width=37)
    fecha_estudio.focus()
    fecha_estudio.grid(column=1, row=1, sticky=tk.W)
    #3
    label_c = tk.Label(master=frame_1, text="CUPS: ", width = 17, font = ('Arial', 10), bg = '#3d6466', relief = SOLID
    ).grid(column=0, row=2, sticky=tk.W, pady=1)
    cups = ttk.Entry(master = frame_1, width=37)
    cups.focus()
    cups.grid(column=1, row=2, sticky=tk.W)
    #4
    label_d = tk.Label(master=frame_1, text="Tarifa: ", width = 17, font = ('Arial', 10), bg = '#3d6466', relief = SOLID
    ).grid(column=0, row=3, sticky=tk.W, pady=1)
    tarifa = ttk.Entry(master = frame_1, width=37)
    tarifa.focus()
    tarifa.grid(column=1, row=3, sticky=tk.W)
    #5
    label_e = tk.Label(master=frame_1, text="CIF: ", width = 17, font = ('Arial', 10), bg = '#3d6466', relief = SOLID
    ).grid(column=0, row=4, sticky=tk.W, pady=1)
    cif = ttk.Entry(master = frame_1, width=37)
    cif.focus()
    cif.grid(column=1, row=4, sticky=tk.W)

def frame_2(container):
    frame_2 = tk.Frame(container, width = 400, height= 100, bg = '#3d6466')
    frame_2.pack()
    #Adding a Button
    frame_2.columnconfigure(0 , weight = 1)
    frame_2.columnconfigure(1 , weight = 1)
    frame_2.columnconfigure(2 , weight = 1)

    btn1 = tk.Button(frame_2 , text = "Borrar Datos", bg = '#28393a', fg="white", cursor="hand2", activebackground = '#badee2',
    activeforeground='black', font = ('Arial', 10), height= 4, width = 14, command= lambda: erase_data())
    btn1.grid(row = 0 , column = 0 , sticky=tk.W + tk.E, padx=2, pady=5)

    btn2 = tk.Button(frame_2 , text = "Obtener Datos Suministro", bg = '#28393a', fg="white", cursor="hand2",
    activebackground = '#badee2', activeforeground='black', wraplength = 80, font = ('Arial', 10), height= 4, width = 14,
    command= lambda: charge_data())
    btn2.grid(row = 0 , column = 1 , sticky=tk.W + tk.E, padx=2, pady=5)

    btn3 = tk.Button(frame_2 , text = "Calcular Potencias Optimas", bg = '#28393a', fg="white", cursor="hand2",
    activebackground = '#badee2',activeforeground='black', wraplength = 80, font = ('Arial', 10), height= 4, 
    width = 14, command= lambda: calculate_data())
    btn3.grid(row = 0 , column = 2 , sticky=tk.W + tk.E, padx=2, pady=5)
