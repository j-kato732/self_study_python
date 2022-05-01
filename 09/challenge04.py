'''
チャレンジ３を日本語で同じようにやってみよう。
例えば、"Top Gun"を”トップガン"のように　日本語に置き換えて、CSVファイルに書き出そう。
'''

import csv

lists = [["トップガン", "リスキービジネス", "マイノリティレポート"], ["タイタニック", "ザレブナント", "インセプション"], ["トレーニングデイ", "マンオンファイア", "フライト"]]

with open('challenge04.csv', mode='w', encoding='utf-8') as f:
    for row in lists:
        w = csv.writer(f, delimiter=',')
        w.writerow(row)
