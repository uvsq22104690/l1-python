def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste = [n]
    while n != 1 :
        if n % 2 == 0 :
            n = n / 2
        elif n % 2 == 1 :
            n = n * 3 + 1
        liste.append(int(n))
    return liste

print(syracuse(3))


def testeConjecture(n_max) :
    for i in range(2, n_max) :
        if syracuse(i)[-1] == 1 :
            return True

print(testeConjecture(10000))


def tempsVol(n):
    """ Retourne le temps de vol de n """
    return len(syracuse(n))-1

print("Le temps de vol de", 3, "est", tempsVol(3))

def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    listeTempsVol = [n_max]
    for i in range(1, n_max) :
        listeTempsVol.append(tempsVol(i))
    del listeTempsVol[0]
    return listeTempsVol

print(tempsVolListe(100))

index = tempsVolListe(10000).index(max(tempsVolListe(10000)))+1

print("Le nombre qui a le plus grand temps de vol entre 1 et 10000 est", index, "avec", max(tempsVolListe(10000)), "de temps de vol.")

def altitudeMaximale(n):
    liste = []
    for i in range(2, n):
        liste.append(syracuse(i))
        return liste

print(altitudeMaximale(10))