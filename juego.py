import tkinter as tk
import random
from PIL import Image, ImageTk
import pygame  


pygame.mixer.init()

#ventana principal
ventana = tk.Tk()
ventana.geometry("400x450")
ventana.title("Piedra, Papel o Tijeras")
ventana.configure(background="#24253C")

# Variables
eleccion_usuario = None
lista_elecciones = ["piedra", "papel", "tijeras"]

# sonidos
sonido_piedra = "audio/piedra.mp3"  
sonido_papel = "audio/papel.mp3"    
sonido_tijeras = "audio/tijeras.mp3" 


def reproducir_sonido(eleccion):
    if eleccion == "piedra":
        pygame.mixer.music.load(sonido_piedra)
    elif eleccion == "papel":
        pygame.mixer.music.load(sonido_papel)
    elif eleccion == "tijeras":
        pygame.mixer.music.load(sonido_tijeras)
    pygame.mixer.music.play()

# Funciones
def seleccionar(eleccion):
    global eleccion_usuario
    eleccion_usuario = eleccion
    seleccion_label.config(text=f"Tú elegiste: {eleccion.capitalize()}", fg="white")
    reproducir_sonido(eleccion)  
    jugar_boton.config(state=tk.NORMAL)  


def jugar():
    if eleccion_usuario is None:
        resultado_label.config(text="Debes seleccionar una opción.", fg="red")
        return

    eleccion_maquina = random.choice(lista_elecciones)
    maquina_label.config(text=f"La máquina eligió: {eleccion_maquina.capitalize()}", fg="white")

    if eleccion_usuario == eleccion_maquina:
        resultado = "Empate"
        color = "yellow"
    elif (eleccion_usuario == "piedra" and eleccion_maquina == "tijeras") or \
         (eleccion_usuario == "papel" and eleccion_maquina == "piedra") or \
         (eleccion_usuario == "tijeras" and eleccion_maquina == "papel"):
        resultado = "¡Ganaste!"
        color = "green"
    else:
        resultado = "Gana la máquina"
        color = "red"
    
    resultado_label.config(text=resultado, fg=color)
    jugar_boton.config(state=tk.DISABLED)  


def reiniciar():
    global eleccion_usuario
    eleccion_usuario = None
    seleccion_label.config(text="Tú elegiste: Ninguno", fg="white")
    maquina_label.config(text="La máquina eligió: Ninguno", fg="white")
    resultado_label.config(text="", fg="white")
    jugar_boton.config(state=tk.DISABLED)  


# Variables de puntajes
puntaje_usuario = 0
puntaje_maquina = 0
empates = 0


def actualizar_puntajes():
    puntaje_label.config(
        text=f"Puntajes - Tú: {puntaje_usuario} | Máquina: {puntaje_maquina} | Empates: {empates}"
    )


def jugar():
    global puntaje_usuario, puntaje_maquina, empates

    if eleccion_usuario is None:
        resultado_label.config(text="Debes seleccionar una opción.", fg="red")
        return

    eleccion_maquina = random.choice(lista_elecciones)
    maquina_label.config(text=f"La máquina eligió: {eleccion_maquina.capitalize()}", fg="white")

    if eleccion_usuario == eleccion_maquina:
        resultado = "Empate"
        color = "yellow"
        empates += 1
    elif (eleccion_usuario == "piedra" and eleccion_maquina == "tijeras") or \
         (eleccion_usuario == "papel" and eleccion_maquina == "piedra") or \
         (eleccion_usuario == "tijeras" and eleccion_maquina == "papel"):
        resultado = "¡Ganaste!"
        color = "green"
        puntaje_usuario += 1
    else:
        resultado = "Gana la máquina"
        color = "red"
        puntaje_maquina += 1

    resultado_label.config(text=resultado, fg=color)
    actualizar_puntajes()  # Actualizar los puntajes en la interfaz
    jugar_boton.config(state=tk.DISABLED)


def reiniciar():
    global eleccion_usuario
    eleccion_usuario = None
    seleccion_label.config(text="Tú elegiste: Ninguno", fg="white")
    maquina_label.config(text="La máquina eligió: Ninguno", fg="white")
    resultado_label.config(text="", fg="white")
    jugar_boton.config(state=tk.DISABLED)

# Etiqueta para puntajes
puntaje_label = tk.Label(ventana, text="Puntajes - Tú: 0 | Máquina: 0 | Empates: 0",
                         font=("Arial", 12), bg="#24253C", fg="white")
puntaje_label.pack(pady=5)


# Cargar imágenes
def cargar_imagen(ruta):
    try:
        img = Image.open(ruta)
        img_resized = img.resize((100, 100))
        return ImageTk.PhotoImage(img_resized)
    except Exception as e:
        print(f"Error al cargar la imagen {ruta}: {e}")
        return None

piedra_icono = cargar_imagen("img/piedra.jpg")
papel_icono = cargar_imagen("img/papel.jpg")
tijeras_icono = cargar_imagen("img/tijeras.jpg")

# Interfaz
frame_botones = tk.Frame(ventana, bg="#24253C")
frame_botones.pack(pady=20)

piedra_boton = tk.Button(frame_botones, image=piedra_icono, background="#24253C", bd=0, command=lambda: seleccionar("piedra"))
piedra_boton.grid(row=0, column=0, padx=10)

papel_boton = tk.Button(frame_botones, image=papel_icono, background="#24253C", bd=0, command=lambda: seleccionar("papel"))
papel_boton.grid(row=0, column=1, padx=10)

tijeras_boton = tk.Button(frame_botones, image=tijeras_icono, background="#24253C", bd=0, command=lambda: seleccionar("tijeras"))
tijeras_boton.grid(row=0, column=2, padx=10)

frame_opciones = tk.Frame(ventana, bg="#24253C")
frame_opciones.pack(pady=10)

jugar_boton = tk.Button(frame_opciones, text="JUGAR", command=jugar, bg="#4CAF50", fg="white", font=("Arial", 12), state=tk.DISABLED)
jugar_boton.grid(row=0, column=0, padx=10)

reiniciar_boton = tk.Button(frame_opciones, text="REINICIAR", command=reiniciar, bg="#f44336", fg="white", font=("Arial", 12))
reiniciar_boton.grid(row=0, column=1, padx=10)

# Etiquetas
seleccion_label = tk.Label(ventana, text="Tú elegiste: Ninguno", font=("Arial", 12), bg="#24253C", fg="white")
seleccion_label.pack(pady=5)

maquina_label = tk.Label(ventana, text="La máquina eligió: Ninguno", font=("Arial", 12), bg="#24253C", fg="white")
maquina_label.pack(pady=5)

resultado_label = tk.Label(ventana, text="", font=("Arial", 16), bg="#24253C", fg="white")
resultado_label.pack(pady=10)


# Ejecutar
ventana.mainloop()
