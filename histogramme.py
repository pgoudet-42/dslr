import os
from math_dslr import mean, std
import sys, csv
from matplotlib import pyplot as plt
import utils



def write_files(houses, titles):
    files = []
    try:
        for i in range(4):
            files.append(open(f"tmp{i}.csv", 'w'))
    except:
        print("Error while opening files")
        exit(1)
    for i,file in enumerate(files):
        wrtr = csv.writer(file)
        wrtr.writerow(titles)
        for line in houses[i]:
            wrtr.writerow(line)

    for i, file in enumerate(files):
        file.close()
        os.system(f"python3 describe.py tmp{i}.csv")
        print()
    try:
        for i in range(4):
            os.remove(f"tmp{i}.csv")
    except:
        print("Error while deleting tmp files")
        exit(1)

def display_histo(houses, titles):
    features = utils.rev_tab(houses, len(titles))
    ecart_type = []
    for feature in features:
        ecart_type.append(std(feature))
    plt.rcParams["figure.figsize"] = (30,10)
    for i in range(0,len(ecart_type)):
        plt.bar(i, ecart_type[i], 1)
    plt.yscale('log')
    plt.ylabel("Standard deviation", fontsize=30)
    plt.xlabel("features", fontsize=30)
    plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12], titles)
    plt.show()


def get_mean(houses, titles):
    for i, house in enumerate(houses):
        tab = []
        for j in range(len(titles)):
            tab.append(mean(utils.get_vertical_list(house, j)))
        houses[i] = tab
    return houses


def get_4_means(titles, datas):
    groups = utils.get_houses(datas)
    houses = [[],[],[],[]]
    for i, house in enumerate(groups):
        for el in datas:
            if el[1] == house and i == 0:
                houses[i].append(el)
            elif el[1] == house and i == 1:
                houses[i].append(el)
            elif el[1] == house and i == 2:
                houses[i].append(el)
            elif el[1] == house and i == 3:
                houses[i].append(el)
    # write_files(houses, titles)
    list(map(utils.clean_array, houses))
    list(map(utils.change_type_of_datas, houses))
    titles = titles[6:]
    houses = get_mean(houses, titles)
    display_histo(houses, titles)


def main():
    try:
        file = open(sys.argv[1], 'r')
    except:
        print("Error while opening file")
        return (1)
    rdr = csv.reader(file)
    datas = []
    titles = rdr.__next__()
    list(map(datas.append, rdr))
    file.close()
    get_4_means(titles, datas)
    

if __name__ == '__main__':
    sys.exit(main())