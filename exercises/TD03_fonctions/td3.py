import sys

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    seconde = temps[0] * 24 * 60 * 60 + temps[1] * 60 * 60 + temps[2] * 60 + temps[3]
    return seconde

"""temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))"""

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""

    temps1 = [0, 0, 0, 0]
    if seconde >= 0 :
        if seconde >= 86400:
            jour = int(seconde / 86400)
            temps1[0] = jour
            seconde = int(seconde % 86400)
        if seconde >= 3600:
            heure = int(seconde / 3600)
            temps1[1] = heure
            seconde = int(seconde % 3600)
        if seconde >= 60:
            minute = int(seconde / 60)
            temps1[2] = minute
            seconde = int(seconde % 60)

    temps1[3] = seconde
    return temps1

"""temps2 = secondeEnTemps(100000)
print(temps2[0], "jours", temps2[1], "heures", temps2[2], "minutes", temps2[3], "secondes")"""

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

"""temps4 = [1, 0, 14, 23]
afficheTemps(temps4)"""

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

def sommeTemps(temps7,temps8):
    temps9 = [0, 0, 0, 0]

    temps9[3] = temps7[3] + temps8[3]
    while temps9[3] >= 60:
        temps9[2] += 1
        temps9[3] = temps9[3] - 60

    temps9[2] = temps9[2] + temps7[2] + temps8[2]
    while temps9[2] >= 60:
        temps9[1] += 1
        temps9[2] = temps9[2] - 60

    temps9[1] = temps9[1] + temps7[1] + temps8[1]
    while temps9[1] >= 24:
        temps9[0] += 1
        temps9[1] = temps9[1] - 24

    temps9[0] = temps9[0] + temps7[0] + temps8[0]

    print(temps9)

sommeTemps((2,3,4,25),(5,22,57,1))

def proportionTemps(temps,proportion):
    nouveau_temps = secondeEnTemps(tempsEnSeconde(temps)*proportion)
    return nouveau_temps

afficheTemps(proportionTemps((2,0,36,0),0.2))

def tempsEnDate(temps):
    date = [0, 0, 0, 0, 0]
    if temps[0] > 365 :
        date[0] = int(temps[0]/365)
        temps[0] = temps[0] - int(temps[0]/365) * 365

    date[1] = temps[0]
    date[2] = temps[1]
    date[3] = temps[2]
    date[4] = temps[3]
    return date


def afficheDate(date = -1):

    print("")

    if date[0] == 1:
        print("1 année", end=" ")
    elif date[0] >= 2:
        print(date[0], "années", end=" ")

    if date[1] == 1:
        print("1 jour", end=" ")
    elif date[1] >= 2:
        print(date[1], "jours", end=" ")

    if date[2] == 1:
        print("1 heure", end=" ")
    elif date[2] >= 2:
        print(date[2], "heures", end=" ")

    if date[3] == 1:
        print("1 minute", end=" ")
    elif date[3] >= 2:
        print(date[3], "minutes", end=" ")

    if date[4] == 1:
        print("1 seconde", end=" ")
    elif date[4] >= 2:
        print(date[4], "secondes", end=" ")

temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))