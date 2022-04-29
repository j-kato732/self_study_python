'''
3つの必須引数と2つのオプション引数がある関数を書いてみよう。
'''

def calc(a, b, c, d=1.1, e=1.08):
    shoukei = a + b
    if c:
        return shoukei * d
    else:
        return shoukei + e
    

print(calc(100, 345, True))