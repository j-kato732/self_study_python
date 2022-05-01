'''
円を表すCircleクラスを定義しよう。
そのクラスに、面積を計算して返すメソッドareaを持たせよう。
面積の計算には、Pythonの組込モジュールmathのpi定数が使えます。
次に、Circleオブジェクトを作って、areaメソッドを呼び出し、結果を出力しよう
'''

import math

class Circle:
    def __init__(self, r):
        self.radius = r
    
    def area(self):
        return self.radius * self.radius * math.pi

circle = Circle(12)
print(circle.area())