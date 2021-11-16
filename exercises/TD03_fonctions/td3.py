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