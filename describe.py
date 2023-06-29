import csv
import sys
from math_dslr import prem_quart, mean, std, deux_quart, trois_quart, min, max
from utils import get_vertical_list, change_type_of_datas, clean_array



def display_results(count, moy, std, mini, quart1, quart2, quart3, maxi, titles):
    print(" "*7, end = '')
    for title in titles:
        print(f'{title:^13s}', end = '|')
    print("\n\ncount: ", end="")
    for i, el in enumerate(count):
        print(f'{el:^{max([len(titles[i]), 13])}.5f}',end="|")
    print("\nmean:  ", end="")
    for i, el in enumerate(moy):
        print(f'{el:^{max([len(titles[i]), 13])}.5f}',end="|")
    print("\nstd:   ", end="")
    for i, el in enumerate(std):
        print(f'{el:^{max([len(titles[i]), 13])}.5f}',end="|")
    print("\nmin:   ", end="")
    for i, el in enumerate(mini):
        print(f'{el:^{max([len(titles[i]), 13])}.5f}',end="|")
    print("\n25%:   ", end="")
    for i, el in enumerate(quart1):
        print(f'{el:^{max([len(titles[i]), 13])}.5f}',end="|")
    print("\n50%:   ", end="")
    for i, el in enumerate(quart2):
        print(f'{el:^{max([len(titles[i]), 13])}.5f}',end="|")
    print("\n75%:   ", end="")
    for i, el in enumerate(quart3):
        print(f'{el:^{max([len(titles[i]), 13])}.5f}',end="|")
    print("\nmax:   ", end="")
    for i, el in enumerate(maxi):
        print(f'{el:^{max([len(titles[i]), 13])}.5f}',end="|")
    print()


def get_statistics_values(datas, titles):
    count = []
    moy = []
    ecart_type = []
    minimum = []
    quart1 = []
    quart2 = []
    quart3 = []
    maximum = []
    change_type_of_datas(datas)
    for i, _ in enumerate(titles):
            count.append(len(get_vertical_list(datas, i)))
            moy.append(mean(get_vertical_list(datas, i)))
            ecart_type.append(std(get_vertical_list(datas, i)))
            minimum.append(min(get_vertical_list(datas, i)))
            quart1.append(prem_quart(get_vertical_list(datas, i)))
            quart2.append(deux_quart(get_vertical_list(datas, i)))
            quart3.append(trois_quart(get_vertical_list(datas, i)))
            maximum.append(max(get_vertical_list(datas, i)))
    display_results(count, moy, ecart_type, minimum, quart1, quart2, quart3, maximum, titles)


def main():
    datas = []
    titles = []
    try:
        file = open(sys.argv[1], 'r')
    except:
        print("Error while opening file")
        return (1)
    rdr = csv.reader(file)
    titles = rdr.__next__()
    for el in rdr:
        datas.append(el)
    titles = titles[6:]
    clean_array(datas)
    get_statistics_values(datas, titles)


if __name__ == '__main__':
    sys.exit(main())