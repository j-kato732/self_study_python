'''
チャレンジ1のリストの要素をそれぞれ、インデックス値と一緒に出力しよう。
'''

import challenge01 as c1

for i, movie in enumerate(c1.movies):
    print(i, movie)