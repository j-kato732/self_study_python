'''
六角形を表すHezagonクラスを定義しよう。
そのクラスには、外周の長さを計算して返すメソッドcalculate_primeterを定義しよう。
そして、Hexagonオプジェクトを作ってcalclate_perimeterメソッドを呼びだし、結果を出力しよう
'''

class Hexagon:
    def __init__(self, l):
        self.length = l
    
    def area(self):
        return self.length * 6

hexa = Hexagon(3)
print(hexa.area())