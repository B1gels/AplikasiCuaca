import tkinter as tk
from tkinter import ttk ,messagebox
from PIL import Image,ImageTk #*gunanya buat bisa memasukkan gambar ke Tkinter 

def Jendela_utama():
    # *membuat jendela utama
    window = tk.Tk()

    # *mengambil gambar dan mengubahnya agar bisa dimasukkan ke tkInter
    image = Image.open("image/icon_cuaca.png")
    gambar = ImageTk.PhotoImage(image.resize((100,100)))

    # *konfigurasi jendela utama
    window.geometry("300x300")
    window.resizable(False,False)
    window.title("== APLIKASI CUACA ==")

    # *widget baru dalam jendela utama
    first_widget = ttk.Frame(window)
    first_widget.pack(padx=10,pady=10,fill="x",expand=True)

    # !ini itu tabel widget pertama
    # !Logo
    logo = ttk.Label(first_widget,image=gambar)
    logo.pack()

    # !desc
    desc = ttk.Label(first_widget,text="Masukkan Nama Kota")
    desc.pack()

    # !input nama kota
    input = ttk.Entry(first_widget)
    input.pack()

    # !tombol submit
    submit = ttk.Button(first_widget,text="submit!!",command=lambda: periksa_input(input))
    submit.pack(pady=5)


    window.mainloop()

def periksa_input(input):
    kota = input.get().strip()  # *Ambil input dari user dan hapus spasi di awal/akhir
    if not kota:  # Jika input kosong
        messagebox.showerror("Error", "Nama kota tidak boleh kosong!")
    else:
        tampilkan_cuaca(kota) 

def tampilkan_cuaca(kota):
    # *Membuat jendela baru
    window2 = tk.Tk()

    # *Konfigurasi jendela kedua
    window2.geometry("300x300")
    window2.title(f"cuaca di {kota}")
    window2.resizable(False,False)

    # *widget
    widget = ttk.Frame(window2)
    widget.pack(padx=10,pady=10,fill="x",expand=True)

    # # !mengubah style frame widget
    # widget.configure(style="custom.TFrame")
    # style = ttk.Style()
    # style.configure("custom.TFrame",background="lightblue",)
    
    tabel1 = ttk.Label(widget,text="Cuaca di kota kendari",background="lightblue")
    tabel1.pack()
    window2.mainloop()