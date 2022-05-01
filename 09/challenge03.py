'''
リストのリストに含まれている要素をCSVファイルに書き出そう。
データは次の通り：[["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
データの各要素はCSVの1行となり、その1行に含まれる各要素がカンマで区切られるように書き出そう。
'''

import csv

lists = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

with open('challenge03.csv', mode='w') as f:
    for row in lists:
        w = csv.writer(f, delimiter=",")
        w.writerow(row)
