def sum(tab):
    sum = 0
    for el in tab:
        sum += el
    return sum

def mean(tab):
    return sum(tab) / len(tab)

def max(tab):
    max = tab[0]
    for el in tab:
        try: 
            if el > max: max = el
        except: continue
    return max

def min(tab):
    max = tab[0]
    for el in tab:
        try:
            if el < max: max = el
        except: continue
    return max

def sqrt(nbr):
    precision = 10
    largeur  = 2
    longueur = nbr/largeur
    for i in range(precision):
        largeur = (longueur+largeur)/2
        longueur = nbr/largeur
    return (largeur)

def std(tab):
    moyenne = mean(tab)
    sum_ecart = 0
    for el in tab:
        sum_ecart += (moyenne - el) * (moyenne - el)
    tmp = sum_ecart / len(tab)
    return sqrt(tmp)

def prem_quart(tab):
    size = len(tab)
    res: float = float(size / 4)
    if res > int(res):
        res += 1
    return (tab[int(res)])

def trois_quart(tab):
    if len(tab) < 4:
        return 0.0
    size = len(tab)
    res: float = float(size / 4)
    res = res * 3
    if res > int(res):
        res += 1
    return (tab[int(res)])

def deux_quart(tab):
    size = len(tab)
    res: float = float(size / 4)
    res = res * 2
    if res > int(res):
        res += 1
    return (tab[int(res)])