'''
Shapeクラスを定義しよう。呼ばれたら"I am a shape"を返すメソッドwhat_am_iを定義しよう。
前のチャレンジで定義したRectabgleとSquareクラスを変更して、このShapeクラスを継承させよう。
そして、RectangleとSquareのオブジェクトを生成日て、このチャレンジで追加したメソッドwhat_am_iを読んでみよう
'''

class Shape:
    def what_am_i(self):
        return 'I am a shape'

class Rectangle(Shape):
    def __init__(self, h, w):
        self.height = h
        self.width = w
    
    def calculate_perimeter(self):
        return 2 * self.height + 2 * self.width

class Square(Shape):
    def __init__(self, h):
        self.hen = h
    
    def calculate_perimeter(self):
        return self.hen * 4

    def change_size(self, num):
        self.hen += num

rect = Rectangle(20, 10)
squ = Square(10)

print(rect.what_am_i(), squ.what_am_i())