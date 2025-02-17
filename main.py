import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

global total_trials, successful_trials
total_trials = 0
successful_trials = 0

def generate_random_triangle():
    """Generiert zufällig drei Punkte auf dem Kreisumfang."""
    angles = np.sort(np.random.uniform(0, 2 * np.pi, 3))  # Zufällige Winkel
    points = np.array([[np.cos(a), np.sin(a)] for a in angles])  # Umrechnung in Koordinaten
    return points

def contains_origin(triangle):
    """Prüft, ob das Dreieck den Ursprung (Mittelpunkt) enthält."""
    A, B, C = triangle
    
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
    
    b1 = sign([0, 0], A, B) < 0
    b2 = sign([0, 0], B, C) < 0
    b3 = sign([0, 0], C, A) < 0
    
    return (b1 == b2) and (b2 == b3)

def draw_triangle():
    """Zeichnet das zufällige Dreieck auf dem Kreis."""
    global ax, canvas, total_trials, successful_trials, label_probability
    ax.clear()
    
    # Kreis zeichnen
    circle = plt.Circle((0, 0), 1, color='blue', fill=False, linestyle='dashed')
    ax.add_patch(circle)
    
    # Zufälliges Dreieck generieren
    triangle = generate_random_triangle()
    
    # Überprüfen, ob der Mittelpunkt enthalten ist
    total_trials += 1
    if contains_origin(triangle):
        successful_trials += 1
        color = 'green'
        title = "Das Dreieck enthält den Mittelpunkt!"
    else:
        color = 'red'
        title = "Das Dreieck enthält den Mittelpunkt NICHT!"
    
    # Wahrscheinlichkeit berechnen
    probability = successful_trials / total_trials
    label_probability.config(text=f"Geschätzte Wahrscheinlichkeit: {probability:.3f}")
    
    # Dreieck zeichnen
    x, y = zip(*triangle)
    ax.fill(x + (x[0],), y + (y[0],), color=color, alpha=0.5)
    ax.scatter(x, y, color='black')
    ax.scatter(0, 0, color='purple', label='Mittelpunkt', s=100)
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.set_title(title)
    ax.legend()
    
    canvas.draw()

# GUI mit Tkinter
root = tk.Tk()
root.title("Zufälliges Dreieck auf einem Kreis")

fig, ax = plt.subplots(figsize=(5, 5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

btn = tk.Button(root, text="Neues Dreieck", command=draw_triangle)
btn.pack()

label_probability = tk.Label(root, text="Geschätzte Wahrscheinlichkeit: 0.000")
label_probability.pack()

draw_triangle()  # Erstes Dreieck zeichnen

root.mainloop()
