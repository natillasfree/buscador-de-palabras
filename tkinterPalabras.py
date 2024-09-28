from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Trabajando con cadenas - Natalia")
ventana.geometry("460x490")
ventana.resizable(False, False)

fondo = PhotoImage(file="estampado.png")
fondo_label = Label(ventana, image=fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

def encuentra_palabra():
    palabra_opcion1 = entrada_palabra.get().lower()
    texto = texto_grande.get("1.0", END).lower().strip()
    if palabra_opcion1 in texto.split():
        messagebox.showinfo("Resultado", f"La palabra '{palabra_opcion1}' ha sido encontrada en el texto.")
        return palabra_opcion1
    else:
        messagebox.showinfo("Resultado", f"La palabra '{palabra_opcion1}' no ha sido encontrada en el texto.")
        return None

def cuenta_caracteres_palabras():
    texto = texto_grande.get("1.0", END).strip()
    num_caracteres = len(texto)
    num_palabras = len(texto.split())
    messagebox.showinfo("Resultado", f"Número de palabras: {num_palabras}\nNúmero de caracteres: {num_caracteres}")

def es_palindromo():
    palabra_opcion1 = entrada_palabra.get().lower()
    if palabra_opcion1:
        palabra = palabra_opcion1.lower()
        if palabra == palabra[::-1]:
            messagebox.showinfo("Resultado", f"La palabra '{palabra}' es un palíndromo.")
        else:
            messagebox.showinfo("Resultado", f"La palabra '{palabra}' no es un palíndromo.")
    else:
        messagebox.showinfo("Error", "Primero debes encontrar una palabra.")

texto_grande = Text(ventana, height=18, width=50)
texto_grande.pack(pady=10)

label_palabra = Label(ventana, text="Palabra a buscar:",height=2, bg="#A6782F", fg="white")
label_palabra.pack(pady=2)

entrada_palabra = Entry(ventana, width=20)
entrada_palabra.pack()

boton_encuentra_palabra = Button(ventana, text="Encuentra palabra", command=lambda: encuentra_palabra(), bg="#BF7339", fg="white")
boton_encuentra_palabra.pack(pady=5)

boton_cuenta_caracteres_palabras = Button(ventana, text="Cuenta caracteres y palabras", command=cuenta_caracteres_palabras, bg="#BF7339", fg="white")
boton_cuenta_caracteres_palabras.pack(pady=5)

boton_palindromo = Button(ventana, text="Palíndromo??", command=es_palindromo, bg="#BF7339", fg="white")
boton_palindromo.pack(pady=5)

ventana.mainloop()
