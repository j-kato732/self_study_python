'''
無限ループする数字あてプログラムを書こう。
ユーザに文字を入力してもらい、qが入力されたら終了、数字が入力されたら正解かどうかを判定しよう。
正解の数値はプログラム内にいくつかリストで持たせておいて、ユーザーが入力した数字がそのどれかと一致したら「正解」、一致しなかったら「不正解」と表示しよう。
もし数字かq以外の文字が入力されたら、「数字を入力するか、qで終了します」と表示しよう。
'''

numbers = [1,4,9]

while True:
    a = input("数あてゲーム(qで終了します)：")

    if a == "q":
        break

    try:
        b = int(a) 
    except ValueError:
        print('数字を入力するか、qで終了します')
        continue

    if b in numbers:
        print('「正解」')
        break
    else:
        print('「不正解」')
        continue
    
    