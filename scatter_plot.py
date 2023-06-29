import csv
import os
import sys
from matplotlib import pyplot as plt
import math_dslr
from utils import clean_empty_el, display_tab
from utils import change_type_of_datas, clean_array, normalize_datas, rev_tab


def display_plot(datas, titles):
    clean_empty_el(datas)
    for data in datas:
        if '' in data:
            print("fuck")
    plt.rcParams["figure.figsize"] = (30,10)
    plt.xlabel("individus")
    plt.ylabel("notes")
    plt.title(f"features {titles[0]} - {titles[1]}")
    for i,data in enumerate(datas):
        plt.scatter(range(len(data)), data)
    plt.show()


def compare(tab, features):
    lst = rev_tab(tab, 6)
    change_type_of_datas(lst)
    means = []
    for el in lst:
        means.append(math_dslr.mean(el))
    min = (math_dslr.max(means) - math_dslr.min(means))
    index1 = -1
    index2 = -1
    for i in range(len(means) - 1):
        for j in range (i + 1, len(means)):
            if abs(means[i] - means[j]) < min:
                min = abs(means[i] - means[j])
                index1 = i
                index2 = j
    print(f"les deux meilleurs matieres les plus proches sont: \n-{features[index1]}\n-{features[index2]}")
    return (features[index1], features[index2])


def get_datas_from_feature(datas, titles, features):
    column = []
    for i,title in enumerate(titles):
        if title == features[0] or title == features[1]:
            column.append(i)
    displayed_data = []
    datas = rev_tab(datas, len(titles))
    for i,data in enumerate(datas):
        if i == 8 or i == 10:
            displayed_data.append(data)
    display_plot(displayed_data, features)


def get_resultats(datas, titles):
    try:file = open("resultats.txt")
    except: print("Error while opening resultats.txt")
    rdr = csv.reader(file)
    results = []
    features = []
    for i,el in enumerate(rdr):
        if i == 0:
            features.append(el[0])
        if i > 2 and i < 9:
            results.append(el[0][10:-1])
    tab = []
    features = features[0].split('|')
    for i,feat in enumerate(features):
        features[i] = feat.strip()
    for res in results:
        tab.append(res.split('|'))
    features = compare(tab, features)
    get_datas_from_feature(datas, titles, features)

        



def describe_normalize_datas(datas, titles):
    reduce_data = []
    for data in datas:
        reduce_data.append(data[6:])
    change_type_of_datas(reduce_data)
    reduce_data = normalize_datas(reduce_data, titles)
    for i,_ in enumerate(datas):
        datas[i] = datas[i][:6] + reduce_data[i]
    try:
        file = open("tmp.csv", "w")
    except:
        print("Error while opening file")
        exit(1)
    wrtr = csv.writer(file)
    wrtr.writerow(titles)
    for data in datas:
        wrtr.writerow(data)
    file.close()
    os.system("python3 describe.py tmp.csv > resultats.txt")
    get_resultats(datas, titles)
    try:
        os.remove("tmp.csv")
        os.remove("resultats.txt")
    except: print("Error while delting files")
    return(datas)
    

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
    titles = titles[6:]
    normdatas = describe_normalize_datas(datas, titles)
    clean_array(normdatas)
    # display_plot(normdatas, titles)


if __name__ == "__main__":
    sys.exit(main())