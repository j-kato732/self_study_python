'''
2つのパラメータを受け取る関数をかこう。
この関数は同じオブジェクトを渡されたらTrueを返し、そうじゃなかったらFalseをかえそう。
'''

def is_same_obj(a, b):
    return a is b

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

r1 = Rectangle(10, 20)
s1 = Square(10)

print(is_same_obj(r1, s1))
print(is_same_obj(1, 2))
