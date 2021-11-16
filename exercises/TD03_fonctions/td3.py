import sys

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    seconde = temps[0] * 24 * 60 * 60 + temps[1] * 60 * 60 + temps[2] * 60 + temps[3]
    return seconde

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""

    if seconde >= 0 :
        if seconde >= 86400:
            jour = int(seconde / 86400)
            seconde = int(seconde % 86400)
        if seconde >= 3600:
            heure = int(seconde / 3600)
            seconde = int(seconde % 3600)
        if seconde >= 60:
            minute = int(seconde / 60)
            seconde = int(seconde % 60)

    temps1 = [jour, heure, minute, seconde]
    return temps1

temps2 = secondeEnTemps(100000)
print(temps2[0], "jours", temps2[1], "heures", temps2[2], "minutes", temps2[3], "secondes")

def afficheTemps(temps3):

    if temps3[0] == 1 :
        print("1 jour", end=" ")
    elif temps3[0] >= 2 :
        print(temps3[0], "jours", end=" ")

    if temps3[1] == 1 :
        print("1 heure", end=" ")
    elif temps3[1] >= 2 :
        print(temps3[1], "heures", end=" ")

    if temps3[2] == 1 :
        print("1 minute", end=" ")
    elif temps3[2] >= 2 :
        print(temps3[2], "minutes", end=" ")

    if temps3[3] == 1 :
        print("1 seconde", end=" ")
    elif temps3[3] >= 2 :
        print(temps3[3], "secondes", end=" ")

temps4 = [1, 0, 14, 23]
afficheTemps(temps4)

def demandeTemps():

    temps5 = [0, 0, 0, 0]
    temps5[0] = int(input("\nVeuillez saisir le nombre de jours : "))
    if temps5[0] < 0 :
        print("Erreur.")
        sys.exit()
    temps5[1] = int(input("Veuillez saisir le nombre d'heures : "))
    if temps5[1] < 0 or temps5[1] >= 24 :
        print("Erreur.")
        sys.exit()
    temps5[2] = int(input("Veuillez saisir le nombre de minutes : "))
    if temps5[2] < 0 or temps5[2] >= 60 :
        print("Erreur.")
        sys.exit()
    temps5[3] = int(input("Veuillez saisir le nombre de secondes : "))
    if temps5[3] < 0 or temps5[3] >= 60:
        print("Erreur.")
        sys.exit()

    return temps5

afficheTemps(demandeTemps())


def demandeTempsBoucle():

    temps6 = [0, 0, 0, 0]
    temps6[0] = int(input("\nVeuillez saisir le nombre de jours : "))

    if temps6[0] < 0 :
        while temps6[0] < 0 :
            print("Erreur.")
            temps6[0] = int(input("Veuillez saisir le nombre de jours : "))

    temps6[1] = int(input("Veuillez saisir le nombre d'heures : "))
    if temps6[1] < 0 or temps6[1] >= 24 :
        while temps6[1] < 0 or temps6[1] >= 24 :
            print("Erreur.")
            temps6[1] = int(input("Veuillez saisir le nombre d'heures : "))

    temps6[2] = int(input("Veuillez saisir le nombre de minutes : "))
    if temps6[2] < 0 or temps6[2] >= 60 :
        while temps6[2] < 0 or temps6[2] >= 60 :
            print("Erreur.")
            temps6[2] = int(input("Veuillez saisir le nombre de minutes : "))

    temps6[3] = int(input("Veuillez saisir le nombre de secondes : "))
    if temps6[3] < 0 or temps6[3] >= 60 :
        while temps6[3] < 0 or temps6[3] >= 60 :
            print("Erreur.")
            temps6[3] = int(input("Veuillez saisir le nombre de secondes : "))

    return temps6

afficheTemps(demandeTempsBoucle())