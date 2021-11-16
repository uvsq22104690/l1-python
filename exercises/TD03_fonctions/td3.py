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

    temps = [jour, heure, minute, seconde]
    return temps

temps = secondeEnTemps(100000)
print(temps[0], "jours", temps[1], "heures", temps[2], "minutes", temps[3], "secondes")

def afficheTemps(temps):

    if temps[0] == 1 :
        print("1 jour", end=" ")
    elif temps[0] >= 2 :
        print(temps[0], "jours", end=" ")

    if temps[1] == 1 :
        print("1 heure", end=" ")
    elif temps[1] >= 2 :
        print(temps[1], "heures", end=" ")

    if temps[2] == 1 :
        print("1 minute", end=" ")
    elif temps[2] >= 2 :
        print(temps[2], "minutes", end=" ")

    if temps[3] == 1 :
        print("1 seconde", end=" ")
    elif temps[3] >= 2 :
        print(temps[3], "secondes", end=" ")

afficheTemps((1, 0, 14, 23))

def demandeTemps():
    temps = []
    temps[0] = int(input("Veuillez saisir le nombre de jours."))
    if temps[0] < 0 :
        print("Erreur.")
    temps[1] = int(input("Veuillez saisir le nombre d'heures."))
    if temps[1] < 0 or temps[1] >= 24 :
        print("Erreur.")
    temps[2] = int(input("Veuillez saisir le nombre de minutes."))
    if temps[2] < 0 or temps[2] >= 60 :
        print("Erreur.")
    temps[3] = int(input("Veuillez saisir le nombre de secondes."))
    if temps[3] < 0 or temps[3] >= 60:
        print("Erreur.")

afficheTemps(demandeTemps())