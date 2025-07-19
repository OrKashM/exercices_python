# _ArrayMatrix_sorted.py

import random

class ArrayMatrixHandler:
    def __init__(self):
        self.data = None
        self.mode = None  # 'array' ou 'matrix'

    def choisir_mode(self):
        choix = input("Voulez-vous travailler avec un tableau (T) ou une matrice (M) ? ").strip().lower()
        if choix == 't':
            self.mode = 'array'
            self.initialiser_array()
        elif choix == 'm':
            self.mode = 'matrix'
            self.initialiser_matrice()
        else:
            print("Choix invalide. Réessayez.")
            self.choisir_mode()
    
    @staticmethod
    def demander_entier(message, condition=lambda x: True, erreur="Entrée invalide."):
        while True:
            try:
                valeur = int(input(message))
                if condition(valeur):
                    return valeur
                print(erreur)
            except ValueError:
                print("Veuillez entrer un entier.")
    
    def initialiser_array(self):

        n = self.demander_entier("Combien d'éléments pour ton tableau ? : ", lambda x: x > 0, "Le nombre doit être positif.")
        val_min = self.demander_entier("Valeur minimale pour le tableau : ")
        val_max = self.demander_entier(f"Valeur maximale (≥ {val_min}) : ", lambda x: x >= val_min, f"le nombre doit être supérieur à {val_min}")


        self.data = [random.randint(val_min, val_max) for _ in range(n)]
        print("✅ Tableau généré :", self.data)
        self.tab_max_consecutif()

    def initialiser_matrice(self):

        m = self.demander_entier("Combien de lignes pour ta matrice ? : ", lambda x: x > 0, "Le nombre doit être positif.")
        p = self.demander_entier("Combien de colonnes pour ta matrice ? : ", lambda x: x > 0, "Le nombre doit être positif.")
        val_min_m = self.demander_entier("Valeur minimale pour la matrice : ")
        val_max_m = self.demander_entier(f"Valeur maximale (≥ {val_min_m}) : ", lambda x: x >= val_min_m, f"le nombre doit être supérieur à {val_min_m}")


        self.data = [[random.randint(val_min_m, val_max_m) for _ in range(p)] for _ in range(m)]
        print("✅ Matrice générée :", self.data)
        self.aplatir_matrice()
        self.tab_to_matrix(m,p)

    def tab_max_consecutif(self):
        l = len (self.data)
        for i in range (l-1, 0, -1): # de la fin vers le début
            # Trouver l'index du max dans la partie arr[0..i]
            max_index = 0
            for j in range(1, i + 1):
                if self.data[j] > self.data[max_index]:
                    max_index = j
            # Échanger le max avec l'élément à la fin de la partie non triée
            self.data[i], self.data[max_index] = self.data[max_index], self.data[i]
        #return self.data
        if self.mode == 'array' :
            print("✅ Tableau trié par maximums consécutif :", self.data)

    def aplatir_matrice(self):
        self.data = [val for ligne in self.data for val in ligne]
        self.tab_max_consecutif()

    def tab_to_matrix (self, m, p):
        self.data = [self.data[i * p : (i + 1) * p] for i in range(m)]
        print("✅ Matrice triée par maximums consécutifs : ", self.data)


# Lancer l'application
if __name__ == "__main__":
    app = ArrayMatrixHandler()
    app.choisir_mode()
    
