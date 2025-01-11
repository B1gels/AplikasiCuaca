import requests
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk #*gunanya buat bisa memasukkan gambar ke Tkinter 

def Jendela_utama():

    window = tk.Tk()
    image = Image.open("image/icon_cuaca.png")
    gambar = ImageTk.PhotoImage(image.resize((100,100)))



    window.geometry("300x300")
    # window.configure(bg="white")
    window.resizable(False,False)
    window.title("== APLIKASI CUACA ==")
    first_widget = ttk.Frame(window)
    first_widget.pack(padx=10,pady=10,fill="x",expand=True)

    # !ini itu tabel widget pertama,berisi
    logo = ttk.Label(first_widget,image=gambar)
    logo.pack()

    desc = ttk.Label(first_widget,text="Masukkan Nama Kota")
    desc.pack()

    input = ttk.Entry(first_widget)
    input.pack()

    submit = ttk.Button(first_widget,text="submit!!")
    submit.pack(pady=5)
    # komponen

    window.mainloop()