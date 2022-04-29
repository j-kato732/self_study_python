'''
文字列をfloat型に変換して戻り値とする関数を書いてみよう。
起こり得る例外をキャッチする例外処理を書こう。
'''

def str2float(string):
    try:
        return float(string)
    except ValueError:
        return "小数の文字列を引数としてください"

print(str2float("Hello"))