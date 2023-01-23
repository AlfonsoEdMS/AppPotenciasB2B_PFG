#importing library
from tkinter import *
from tkinter import font, messagebox, filedialog
from PIL import ImageTk, Image
import time
#Import the required Libraries
import customtkinter
from app_functions import erase_data, calculate_data, charge_data
import sqlite3

connection = sqlite3.connect('db/first_light(1).db')
db = connection.cursor()

w=Tk()

#Using piece of code from old splash screen
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
#w.configure(bg='#ED1B76')
w.overrideredirect(1) #for hiding titlebar

#new window to open
def new_win():
    # Setting up theme of your app
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    #Create app
    root = customtkinter.CTk()
    root.geometry("580x450")
    root.title("Asesoría de potencias B2B monoCUPS")
    root.eval("tk::PlaceWindow . center")

    def login():
        #Save the DATA
        add_user = str(entry1.get())
        add_password = str(entry2.get())
        #QUERY
        sqlite_insert_with_param = """
            SELECT * 
            FROM Users 
            WHERE Usuario = ? AND Contraseña = ?;
            """
        #EXECUTE
        data_tuple = (add_user, add_password)
        exist = db.execute(sqlite_insert_with_param, data_tuple).fetchone()
        if exist is None:
            print(messagebox.askretrycancel(message="Usuario No Registrado", title="Acceso Denegado"))
            pass
        else:
            #root.destroy()
            #new_win()
            print('Corret!')

    frame = customtkinter.CTkFrame(master = root)
    frame.pack(pady = 20, padx=60, fill='both', expand=True)

    #image = Image.open("pngs/logo_etsime.png")
    #image = image.resize((400, 100), Image.ANTIALIAS)
    upm_img = ImageTk.PhotoImage(file = "pngs/logo_blanco_etsime.png")
    upm_widget = customtkinter.CTkLabel(frame, image = upm_img)
    upm_widget.pack(pady=12, padx=10, fill='both')

    label = customtkinter.CTkLabel(master=frame, text="FirstLight", text_font=("Courier", 20))
    label.pack(pady=12, padx=10, fill='both') #image_label

    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
    entry1.pack(pady=12, padx=10)

    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
    entry2.pack(pady=12, padx=10)

    button = customtkinter.CTkButton(master=frame, text="Login", command=login)
    button.pack(pady=12, padx=10)

    checkbox = customtkinter.CTkCheckBox(master=frame, text="Remeber Me")
    checkbox.pack(pady=12, padx=10)

    #run app
    root.mainloop()


Frame(w, width=427, height=250, bg='#272727').place(x=0,y=0)
label1=Label(w, text='PROGRAMMED', fg='white', bg='#272727') #decorate it 
label1.configure(font=("Game Of Squids", 24, "bold"))   #You need to install this font in your PC or try another one
label1.place(x=80,y=90)

label2=Label(w, text='Loading...', fg='white', bg='#272727') #decorate it 
label2.configure(font=("Calibri", 11))
label2.place(x=10,y=215)

#making animation

image_a=ImageTk.PhotoImage(Image.open('pngs/c2.png'))
image_b=ImageTk.PhotoImage(Image.open('pngs/c1.png'))




for i in range(3): #5loops
    l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)



w.destroy()
new_win()
connection.close()
w.mainloop()
