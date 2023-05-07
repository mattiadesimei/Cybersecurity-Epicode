#Mattia De Simei

#Calcolo del perimetro di una data figura

# Funzione perimetro cerchio
def calcola_perimetro_cerchio(raggio):
    return 2 * 3.14 * raggio

# Funzione perimetro quadrato
def calcola_perimetro_quadrato(lato):
    return 4 * lato

# Funzione perimetro rettangolo
def calcola_perimetro_rettangolo(base, altezza):
    return 2 * (base + altezza)

# Funzione per la scelta della figura e dell'incognita (raggio, lato, etc..)
def calcola_perimetro():
    figura = input("Calcola il perimetro di (cerchio, quadrato, rettangolo): ")

    if figura == "cerchio":
        raggio = float(input("Inserisci il raggio del cerchio: "))
        perimetro = calcola_perimetro_cerchio(raggio)
        print("Il perimetro del cerchio è:", perimetro)
    elif figura == "quadrato":
        lato = float(input("Inserisci il lato del quadrato: "))
        perimetro = calcola_perimetro_quadrato(lato)
        print("Il perimetro del quadrato è:", perimetro)
    elif figura == "rettangolo":
        base = float(input("Inserisci la base del rettangolo: "))
        altezza = float(input("Inserisci l'altezza del rettangolo: "))
        perimetro = calcola_perimetro_rettangolo(base, altezza)
        print("Il perimetro del rettangolo è:", perimetro)
    else:
        print("Figura non contemplata")

# Funzione principale di richiamo
calcola_perimetro()