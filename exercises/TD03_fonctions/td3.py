import sys
import time

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

    print("")

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

    while temps6[0] < 0 :
        print("Erreur.")
        temps6[0] = int(input("Veuillez saisir le nombre de jours : "))


    temps6[1] = int(input("Veuillez saisir le nombre d'heures : "))
    while temps6[1] < 0 or temps6[1] >= 24:
        print("Erreur.")
        temps6[1] = int(input("Veuillez saisir le nombre d'heures : "))

    temps6[2] = int(input("Veuillez saisir le nombre de minutes : "))
    while temps6[2] < 0 or temps6[2] >= 60:
        print("Erreur.")
        temps6[2] = int(input("Veuillez saisir le nombre de minutes : "))

    temps6[3] = int(input("Veuillez saisir le nombre de secondes : "))
    while temps6[3] < 0 or temps6[3] >= 60:
        print("Erreur.")
        temps6[3] = int(input("Veuillez saisir le nombre de secondes : "))

    return temps6

afficheTemps(demandeTempsBoucle())

def sommeTemps(temps7,temps8):

    temps7EnSec = tempsEnSeconde(temps7)
    temps8EnSec = tempsEnSeconde(temps8)
    sommeEnSec = temps7EnSec + temps8EnSec
    return secondeEnTemps(sommeEnSec)

afficheTemps(sommeTemps((2,3,4,25),(5,22,57,1)))

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

def afficheDateMois(date = -1):
    date_mois = [0, 0, 0, 0, 0, 0]
    if date[1] >= 1 and date[1] <= 31 :
        date_mois[1] = "Janvier"
    if date[1] >= 32 and date[1] <= 59 :
        date_mois[1] = "Février"
        date[1] = date[1] - 31
    if date[1] >= 60 and date[1] <= 90 :
        date_mois[1] = "Mars"
        date[1] = date[1] - 59
    if date[1] >= 91 and date[1] <= 120 :
        date_mois[1] = "Avril"
        date[1] = date[1] - 90
    if date[1] >= 121 and date[1] <= 151 :
        date_mois[1] = "Mai"
        date[1] = date[1] - 120
    if date[1] >= 152 and date[1] <= 181 :
        date_mois[1] = "Juin"
        date[1] = date[1] - 151
    if date[1] >= 182 and date[1] <= 212 :
        date_mois[1] = "Juillet"
        date[1] = date[1] - 151
    if date[1] >= 213 and date[1] <= 243 :
        date_mois[1] = "Août"
        date[1] = date[1] - 212
    if date[1] >= 244 and date[1] <= 273 :
        date_mois[1] = "Septembre"
        date[1] = date[1] - 243
    if date[1] >= 274 and date[1] <= 304 :
        date_mois[1] = "Octobre"
        date[1] = date[1] - 273
    if date[1] >= 305 and date[1] <= 334 :
        date_mois[1] = "Novembre"
        date[1] = date[1] - 304
    if date[1] >= 335 and date[1] <= 365 :
        date_mois[1] = "Décembre"
        date[1] = date[1] - 334

    date_mois[0] = date[0]
    date_mois[2] = date[1]
    date_mois[3] = date[2]
    date_mois[4] = date[3]
    date_mois[5] = date[4]

    print("")
    print(date_mois[2], date_mois[1], date_mois[0] + 1970, "à " + str(date_mois[3]) + ":" + str(date_mois[4]) + ":" + str(date_mois[5]))

afficheDateMois(tempsEnDate(temps))

time