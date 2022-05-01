'''
Squareクラスのオブジェクトをprint関数に渡したら、4辺それぞれの長さを出力しよう。
例えば、Square(29)のようにオブジェクトを作ったら、print関数では29 by 29 by 29 by 29と出力しよう。
'''

class Square():
    square_list = []

    def __init__(self, h):
        self.hen = h
        self.square_list.append(self)
    
    def calculate_perimeter(self):
        return self.hen * 4

    def change_size(self, num):
        self.hen += num
    
    def __repr__(self):
        return f'{self.hen} by {self.hen} by {self.hen} by {self.hen}'

s1 = Square(29)

print(s1)