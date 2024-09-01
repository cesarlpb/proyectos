import tkinter as tk
from tkinter import messagebox, ttk
import os
import time
import threading
import pygame

# Path base por defecto
BASE_PATH       = None
DEFAULT_MINUTES = "90"
DEFAULT_HOURS   = "0"
DEFAULT_TRACK   = ""
paused          = False
remaining_time  = 0
running         = False  # Nueva variable para controlar el hilo del temporizador
threads         = []  # Lista para guardar los threads activos
ENV = {}

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent # carpeta 01

# with open(BASE_DIR / '.env') as f:
#     lines = f.readlines()
# for line in lines:
#     key, value = line.split("=")
#     ENV[key] = value
    
# BASE_PATH = ENV["BASE_PATH"]

BASE_PATH = BASE_DIR / "audios" # 01/audios/

# Función para listar los archivos MP3 en el ComboBox
def list_mp3_files():
    global default_track  # Declaramos que vamos a usar la variable global
    mp3_tracks = [f for f in os.listdir(BASE_PATH) if f.endswith(".mp3")]
    # Busca el primer archivo que contenga "3s" en el nombre
    DEFAULT_TRACK = next((f for f in mp3_tracks if "3s" in f), None)
    return mp3_tracks

# Función para reproducir la pista de audio
def play_audio(audio_path):
    # pygame.mixer.init()
    # pygame.mixer.music.load(audio_path)
    # pygame.mixer.music.play()
    """
    Reproduce el archivo de audio especificado.
    """
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
    except Exception as e:
        messagebox.showerror("Error de Reproducción", f"No se pudo reproducir el archivo:\n{audio_path}\n\n{e}")

# Función para el temporizador
# def countdown(total_seconds, audio_file):
#     global paused, remaining_time
#     remaining_time = total_seconds
#     running = True  # Indicar que el temporizador está corriendo
    
#     while remaining_time > 0:
#         if not paused:
#             mins, secs = divmod(remaining_time, 60)
#             hours = mins // 60
#             mins = mins % 60
#             time_str = f'{hours:02}:{mins:02}:{secs:02}'
#             timer_label.config(text=time_str)
            
#             root.update()
#             time.sleep(1)
#             remaining_time -= 1
#         else:
#             time.sleep(1)  # Espera mientras está pausado

    # timer_label.config(text="00:00:00")
    # messagebox.showinfo("Tiempo Finalizado", "¡El tiempo se ha acabado!")
    # audio_path = os.path.join(BASE_PATH, audio_file)
    # play_audio(audio_path)
    
    # if remaining_time == 0:
    #     timer_label.config(text="00:00:00")
    #     audio_path = os.path.join(BASE_PATH, audio_file)
    #     play_audio(audio_path)
        
    # Cuando llegue a cero, reproducir la pista sin interacción del usuario
    # timer_label.config(text="00:00:00")
    # audio_path = os.path.join(BASE_PATH, audio_file)
    # play_audio(audio_path)
    
    # running = False  # Indicar que el temporizador ha terminado o se ha detenido
    
def countdown():
    global paused, remaining_time, running
    
    if remaining_time > 0 and running:
        if not paused:
            mins, secs = divmod(remaining_time, 60)
            hours = mins // 60
            mins = mins % 60
            time_str = f'{hours:02}:{mins:02}:{secs:02}'
            timer_label.config(text=time_str)
            
            remaining_time -= 1
        
        # Llamar de nuevo a countdown después de 1 segundo
        root.after(1000, countdown)
    elif remaining_time == 0 and running:
        timer_label.config(text="00:00:00")
        audio_path = os.path.join(BASE_PATH, track_selector.get())
        play_audio(audio_path)

    if remaining_time <= 0:
        running = False  # Indicar que el temporizador ha terminado o se ha detenido


# Función para iniciar el temporizador en un hilo separado
# def start_timer():
#     global paused, running, threads
    
#     if running:  # Evitar iniciar múltiples hilos del temporizador
#         return
    
#     paused = False  # Reiniciar el estado de pausa
#     try:
#         h = int(hour_entry.get())
#         m = int(minute_entry.get())
#         audio_file = track_selector.get()

#         if h < 0 or m < 0:
#             raise ValueError("Horas y minutos deben ser positivos")
#         if not audio_file:
#             raise ValueError("Debes seleccionar una pista de audio")

#         # Iniciar el temporizador en un nuevo hilo
#         # timer_thread = threading.Thread(target=countdown, args=(h, m, audio_file))
#         # timer_thread.start()
        
#         total_seconds = h * 3600 + m * 60
#         timer_thread = threading.Thread(target=countdown, args=(total_seconds, audio_file))
#         threads.append(timer_thread)  # Agregar el hilo a la lista de threads
#         timer_thread.start()

#     except ValueError as ve:
#         messagebox.showerror("Error", str(ve))

def start_timer():
    global paused, running, remaining_time
    if running:  # Evitar iniciar múltiples hilos del temporizador
        return
    paused = False  # Reiniciar el estado de pausa
    try:
        h = int(hour_entry.get())
        m = int(minute_entry.get())

        if h < 0 or m < 0:
            raise ValueError("Horas y minutos deben ser positivos")
        if not track_selector.get():
            raise ValueError("Debes seleccionar una pista de audio")

        total_seconds = h * 3600 + m * 60
        remaining_time = total_seconds
        running = True
        countdown()  # Iniciar el temporizador usando after

    except ValueError as ve:
        messagebox.showerror("Error", str(ve))

def pause_timer():
    global paused
    paused = True
    
def resume_timer():
    global paused
    paused = False
    
# Nueva función para cerrar el programa    
def close_program():
    global running, threads
    running = False  # Detener el temporizador
    
    # Esperar a que todos los threads terminen
    for thread in threads:
        if thread.is_alive():
            thread.join(timeout=0.1)  # Esperar brevemente a que cada hilo termine
    
    root.destroy()  # Cerrar la ventana inmediatamente después de detener los threads
                    # Cerrar la ventana # alternativa: root.quit()

# Anterior funcional:
# Configuración de la ventana principal
# root = tk.Tk()
# root.title("Temporizador")

# Etiquetas y entradas de texto
# tk.Label(root, text="Horas:").grid(row=0, column=0, padx=5, pady=5)
# hour_entry = tk.Entry(root)
# hour_entry.grid(row=0, column=1, padx=5, pady=5)
# hour_entry.insert(0, DEFAULT_HOURS)

# tk.Label(root, text="Minutos:").grid(row=1, column=0, padx=5, pady=5)
# minute_entry = tk.Entry(root)
# minute_entry.grid(row=1, column=1, padx=5, pady=5)
# minute_entry.insert(0, DEFAULT_MINUTES)

# Menú desplegable para seleccionar la pista de audio
# tk.Label(root, text="Seleccionar pista:").grid(row=2, column=0, padx=5, pady=5)
# track_selector = ttk.Combobox(root, values=list_mp3_files())
# track_selector.grid(row=2, column=1, padx=5, pady=5)
# track_selector.insert(0, "sample-3s.mp3")

# Etiqueta para mostrar el temporizador
# timer_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
# timer_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Anterior - cambio layout ----------------------------------------------
# Botón para iniciar el temporizador
# start_button = tk.Button(root, text="Iniciar Temporizador", command=start_timer)
# start_button.grid(row=4, column=0, columnspan=2, pady=10)

# pause_button = tk.Button(root, text="Pausar", command=pause_timer)
# pause_button.grid(row=5, column=0, padx=5, pady=5)

# resume_button = tk.Button(root, text="Reanudar", command=resume_timer)
# resume_button.grid(row=5, column=1, padx=5, pady=5)

# # Botón para cerrar el programa
# close_button = tk.Button(root, text="Cerrar", command=close_program)
# close_button.grid(row=6, column=0, columnspan=2, pady=10)
# Anterior ^ ------------------------------------------------------------

# Modificado
# Botones de control
# start_button = tk.Button(root, text="Iniciar Temporizador", command=start_timer)
# start_button.grid(row=4, column=0, columnspan=3, pady=5)

# pause_button = tk.Button(root, text="Pausar", command=pause_timer)
# pause_button.grid(row=5, column=0, padx=10, pady=5, sticky="e")

# resume_button = tk.Button(root, text="Reanudar", command=resume_timer)
# resume_button.grid(row=5, column=2, padx=10, pady=5, sticky="w")

# Botón para cerrar el programa
# close_button = tk.Button(root, text="Cerrar", command=close_program)
# close_button.grid(row=6, column=1, pady=10)

# Expandir las columnas para centrar los botones
# root.grid_columnconfigure(0, weight=1)
# root.grid_columnconfigure(1, weight=1)
# root.grid_columnconfigure(2, weight=1)

# Vincular la tecla Enter a la función start_timer
# root.bind('<Return>', lambda event: start_timer())

# Configuración de la ventana principal
root = tk.Tk()
root.title("Temporizador")

# Configurar las columnas para que ocupen espacio equitativo
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

# Etiquetas y entradas de texto
tk.Label(root, text="Horas:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
hour_entry = tk.Entry(root)
hour_entry.grid(row=0, column=1, padx=5, pady=5)
hour_entry.insert(0, DEFAULT_HOURS)

tk.Label(root, text="Minutos:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
minute_entry = tk.Entry(root)
minute_entry.grid(row=1, column=1, padx=5, pady=5)
minute_entry.insert(0, DEFAULT_MINUTES)

tk.Label(root, text="Seleccionar pista:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
track_selector = ttk.Combobox(root, values=list_mp3_files())
track_selector.grid(row=2, column=1, columnspan=1, padx=5, pady=2)
track_selector.insert(0, "sample-3s.mp3")

# Etiqueta para mostrar el temporizador
timer_label = tk.Label(root, text="00:00:00", font=("Helvetica", 48))
timer_label.grid(row=3, column=0, columnspan=2, padx=5, pady=20)

# Botones de control
start_button = tk.Button(root, text="Iniciar Temporizador", 
                        command=start_timer,
                        activebackground='red'
                        )
start_button.grid(row=4, column=0, columnspan=2, pady=10)

pause_button = tk.Button(root, text="Pausar", command=pause_timer)
pause_button.grid(row=5, column=0, padx=20, pady=5, sticky="w")

resume_button = tk.Button(root, text="Reanudar", command=resume_timer)
resume_button.grid(row=5, column=1, padx=30, pady=5, sticky="e")

# Botón para cerrar el programa
close_button = tk.Button(root, text="Cerrar", command=close_program)
close_button.grid(row=6, column=0, columnspan=2, pady=10)

# Vincular la tecla Enter a la función start_timer
root.bind('<Return>', lambda event: start_timer())

# Expandir las columnas para centrar los botones
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

if __name__ == '__main__':
    # Iniciar el loop principal de la ventana
    root.mainloop()
