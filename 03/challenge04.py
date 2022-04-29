'''
任意なキーを入力させるプログラムをかこう。
入力されたキーを使って1つ前のチャレンジで用意した辞書から、バリューを取得して表示しよう。
'''

import challenge03 as c3


key = input("キーを入力してください")

if key in c3.kato["Profile"]:
    print(c3.kato["Profile"][key])
else:
    print("入力された項目は存在しません。")