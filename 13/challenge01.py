'''
RectangleとSquareクラスを作ろう。
両方のクラスに、その図形の外周の長さを計算して返すcalculate_perimeterメソッドを定義しよう。
そして、RectangleとSquareのオブジェクトを作って、それぞれのcalculate_perimeterメソッドを呼ぼう。
'''

class Rectangle:
    def __init__(self, h, w):
        self.height = h
        self.width = w
    
    def calculate_perimeter(self):
        return 2 * self.height + 2 * self.width

class Square:
    def __init__(self, h):
        self.hen = h
    
    def calculate_perimeter(self):
        return self.hen * 4

rect = Rectangle(20, 10)
squ = Square(10)

print(rect.calculate_perimeter(), squ.calculate_perimeter())