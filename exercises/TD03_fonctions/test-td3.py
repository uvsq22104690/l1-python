import time

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

afficheTemps(gmtime())