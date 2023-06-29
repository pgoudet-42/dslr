import csv
import os
import sys
import pandas as pd
from matplotlib import pyplot as plt
from utils import change_type_of_datas, clean_array, normalize_datas, rev_tab

def select_column(datas, titles, results):
    i = 0
    while i < len(titles):
        if titles[i] == results[0]:
            titles = titles[:i] + titles[i + 1:]
            datas = datas[:i] + datas[i:]
        elif titles[i] == 'Muggle Studies':
            titles = titles[:i] + titles[i + 1:]
            datas = datas[:i] + datas[i:]
        i += 1

def get_scatter_results():
    file = open("resultats_scatter.txt", 'r')
    file.readline()
    results = (file.readline()[1:-1], file.readline()[1:-1])
    file.close()
    os.remove("resultats_scatter.txt")
    return results

def call_scatter():
    index = 1587
    file = open('scatter_plot copy.py', 'r+')
    rdr1 = file.read()
    file.seek(index)
    file.write("# " + rdr1[index:])
    os.system('python3 "scatter_plot copy.py" datasets/dataset_tmp.csv > resultats_scatter.txt')
    file.seek(0)
    file.write(rdr1[:index] + rdr1[index:] + '  ')
    file.close()

def create_data_frame(datas, titles):
    datas = rev_tab(datas, len(titles))
    df = pd.DataFrame({})
    for i,title in enumerate(titles):
        df.insert(i, title, datas[i])
    return df

def display(datas, titles):
    clean_array(datas)
    titles = titles[6:]
    change_type_of_datas(datas)
    datas = normalize_datas(datas, titles)
    df = create_data_frame(datas, titles)
    call_scatter()
    results = get_scatter_results()
    select_column(datas, titles, results)
    pd.plotting.scatter_matrix(df, figsize=(10,10), marker = 'o', hist_kwds = {'bins': 10}, s = 60, alpha = 0.8)
    plt.xscale('log')
    plt.show()

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
    display(datas, titles)
    
if __name__ == "__main__":
    sys.exit(main())