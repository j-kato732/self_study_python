'''
Squareクラスにsquare_listクラス変数を追加しよう。
そして、新しくSquareクラスのオブジェクトが作られるたびに、そのオブジェクトをこのリストに追加しよう
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


s1 = Square(10)
s2 = Square(5)
s3 = Square(30)

print(Square.square_list)