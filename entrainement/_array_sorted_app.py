# _array_sorted_app.py

# De quelle librairie ai-je besoin ?

import random, time


# 1. Générer un array aléatoirment 

n = int(input("Combien d'éléments pour ton array ? : "  ))
while n < 0 :
    n = int(input("Entrer un nombre d'éléments possitif : "))
#print(n)

val_min = int(input("La valeur minimale possible : "))
while val_min < 0 :
    val_min = int(input("Entrer une valeur minimale possitive : "))

#print (val_min)

val_max = int(input("La valeur maximale possible : "))
while val_max < val_min :
    val_max = int(input(f"Entrer une valeur supérieure à {val_min} : "))

#print(val_max)


unsorted_array = [random.randint(val_min, val_max) for _ in range(n)]
print("Tableau original :", unsorted_array)


# 2. La recherche des maximums consécutifs

def max_consecutif (tableau):
    l = len (tableau)
    for i in range (l-1, 0, -1): # de la fin vers le début
        # Trouver l'index du max dans la partie arr[0..i]
        max_index = 0
        for j in range(1, i + 1):
            if tableau[j] > tableau[max_index]:
                max_index = j
        # Échanger le max avec l'élément à la fin de la partie non triée
        tableau[i], tableau[max_index] = tableau[max_index], tableau[i]
    return tableau
    #print("Tableau trié au max :", tableau)


max_consecutif(unsorted_array)


# 3. La recherche des minimums consécutifs

def min_consecutif (tableau):
    l = len(tableau)
    for i in range(l):
        # Trouver l'index du minimum dans arr[i..n-1]
        min_index = i
        for j in range(i + 1, l):
            if tableau[j] < tableau[min_index]:
                min_index = j
        # Échanger l'élément courant avec le plus petit trouvé
        tableau[i], tableau[min_index] = tableau[min_index], tableau[i]
    #return tableau
    print("Tableau trié au min :", tableau)

min_consecutif(unsorted_array)


# 4. La génération aléatoire d'une matrice de taille m*p

m = int(input("Combien de lignes pour ta matrice ? : "  ))
while m < 0 :
    m = int(input("Entrer un nombre de lignes possitif : "))
#print(m)

p = int(input("Combien de colonnes pour ta matrice ? : "  ))
while p < 0 :
    p = int(input("Entrer un nombre de colonnes possitif : "))
#print(p)

val_min_matrice = int(input("La valeur minimale possible pour ta matrice : "))
while val_min_matrice < 0 :
    val_min_matrice = int(input("Entrer une valeur minimale possitive : "))

#print (val_min_matrice)

val_max_matrice = int(input("La valeur maximale possible : "))
while val_max_matrice < val_min_matrice :
    val_max_matrice = int(input(f"Entrer une valeur supérieure à {val_min_matrice} : "))

#print(val_max_matrice)

unsorted_matrix =[[random.randint(val_min_matrice, val_max_matrice) for _ in range(p)] for _ in range(m)]
print("Matrice originale :", unsorted_matrix)


# La transformation d'une matrice en un tableau

def aplatir_matrice(matrice):
    return [val for ligne in matrice for val in ligne]
    #Matrix_aplatie = [val for ligne in matrice for val in ligne]
    #print("Matrice applatie : ", Matrix_aplatie)


aplatie_unsorted_matrix= aplatir_matrice(unsorted_matrix)

max_consecutif(aplatie_unsorted_matrix)

def reconstituer_matrice(tableau, m, p) :
    if len(tableau) != m * p:
        raise ValueError("La taille du tableau ne correspond pas à m * p.")
    
    #return [tableau[i * p : (i + 1) * p] for i in range(m)]
    Matrix_sorted = [tableau[i * p : (i + 1) * p] for i in range(m)]
    print("Matrice triée : ", Matrix_sorted)


reconstituer_matrice(max_consecutif(aplatie_unsorted_matrix), m, p)