'''
上の１から5で書いた関数すべてにdocstringを追加しよう
'''

def square(num):
    '''
    return num ** 2.
    :param num: int or float.
    return 数値numを２乗した値
    '''
    return num ** 2

def print_str(message):
    '''
    :param message: str
    '''
    print(message)

def calc(a, b, c, d=1.1, e=1.08):
    '''
    Return shoukei * tax 
    :param a: int or float.
    :param b: int or float.
    :param c: bool 
    :param d: float default 1.1
    :param e: float default 1.08
    return: a + bの合計から消費税を追加した値を計算
    '''

    shoukei = a + b
    if c:
        return shoukei * d
    else:
        return shoukei + e
        
def str2float(string):
    '''
    Return: float(string)
    :param string: string
    return: 数値を小数に変換する
    '''

    try:
        return float(string)
    except ValueError:
        return "小数の文字列を引数としてください"

print(square(3))