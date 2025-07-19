# _ArrayMatrix_sorted_gui.py


import tkinter as tk
from tkinter import messagebox
import random

class ArrayMatrixApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tri de Tableaux et Matrices")
        self.data = None
        self.mode = None

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Choisissez un mode :")
        self.label.pack()

        self.btn_array = tk.Button(self.master, text="Tableau", command=self.init_array)
        self.btn_array.pack(pady=5)

        self.btn_matrix = tk.Button(self.master, text="Matrice", command=self.init_matrix)
        self.btn_matrix.pack(pady=5)

        self.result_label = tk.Label(self.master, text="", wraplength=400, justify="left")
        self.result_label.pack(pady=10)

    def demander_entier_popup(self, message, condition=lambda x: True):
        while True:
            value = tk.simpledialog.askstring("Entrée", message)
            if value is None:
                return None
            try:
                val = int(value)
                if condition(val):
                    return val
                else:
                    messagebox.showerror("Erreur", "Condition non remplie.")
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez entrer un entier valide.")

    def init_array(self):
        self.mode = 'array'
        n = self.demander_entier_popup("Nombre d'éléments pour le tableau :", lambda x: x > 0)
        if n is None: return
        val_min = self.demander_entier_popup("Valeur minimale :")
        if val_min is None: return
        val_max = self.demander_entier_popup(f"Valeur maximale (≥ {val_min}) :", lambda x: x >= val_min)
        if val_max is None: return

        self.data = [random.randint(val_min, val_max) for _ in range(n)]
        resultat = f"✅ Tableau généré : {self.data}\n"
        self.tab_max_consecutif()
        resultat += f"✅ Tableau trié : {self.data}"
        self.result_label.config(text=resultat)

    def init_matrix(self):
        self.mode = 'matrix'
        m = self.demander_entier_popup("Nombre de lignes :", lambda x: x > 0)
        if m is None: return
        p = self.demander_entier_popup("Nombre de colonnes :", lambda x: x > 0)
        if p is None: return
        val_min = self.demander_entier_popup("Valeur minimale :")
        if val_min is None: return
        val_max = self.demander_entier_popup(f"Valeur maximale (≥ {val_min}) :", lambda x: x >= val_min)
        if val_max is None: return

        self.data = [[random.randint(val_min, val_max) for _ in range(p)] for _ in range(m)]
        resultat = f"✅ Matrice générée : {self.data}\n"
        self.aplatir_matrice()
        self.tab_to_matrix(m, p)
        resultat += f"✅ Matrice triée : {self.data}"
        self.result_label.config(text=resultat)

    def tab_max_consecutif(self):
        l = len(self.data)
        for i in range(l - 1, 0, -1):
            max_index = 0
            for j in range(1, i + 1):
                if self.data[j] > self.data[max_index]:
                    max_index = j
            self.data[i], self.data[max_index] = self.data[max_index], self.data[i]

    def aplatir_matrice(self):
        self.data = [val for row in self.data for val in row]
        self.tab_max_consecutif()

    def tab_to_matrix(self, m, p):
        self.data = [self.data[i * p:(i + 1) * p] for i in range(m)]

# Lancer l'application
if __name__ == "__main__":
    import tkinter.simpledialog
    root = tk.Tk()
    app = ArrayMatrixApp(root)
    root.mainloop()
