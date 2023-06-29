from itertools import permutations
import math_dslr


def display_tab(tab):
    for t in tab:
        print(t)

def get_vertical_list(datas, i):
    tab = []
    for j in range(len(datas)):
            if type(datas[j][i]) is float:
                tab.append(datas[j][i])
    return (tab)

def change_type_of_datas(datas):
    errors = []
    for i in range(len(datas)):
        for j in range(len(datas[i])):
            try:
                datas[i][j] = float(datas[i][j])
            except:
                errors.append((i,j))


def clean_array(datas):
    for i,el in enumerate(datas):
        datas[i] = el[6:]

def get_houses(datas):
    houses = []
    for el in datas:
        if (el[1] in houses) == False:
            houses.append(el[1])
    return houses

def rev_tab(tab, xlen):
    tabTmp = [[0 for i in range(len(tab))] for j in range(xlen)]
    for i in range(len(tab)):
        for j in range(xlen):
            tabTmp[j][i] = tab[i][j]
    return tabTmp


def normalize_datas(datas, titles):
    size = len(datas)
    datas = rev_tab(datas, len(titles))
    for i,data in enumerate(datas):
        maxi = math_dslr.max(data)
        mini = math_dslr.min(data)
        for j in range(len(datas[i])):
            try: datas[i][j] = (data[j] - mini)/(maxi - mini) * 10
            except: continue
    datas = rev_tab(datas, size)
    return (datas)

def clean_empty_el(tab):
    i = 0
    while i < len(tab):
        j = 0
        while j < len(tab[i]):
            if tab[i][j] == '':
                tab[i].remove(tab[i][j])
                j = j - 1
            j = j + 1
        i = i +1
