'''
Squarekうらすにchange_sizeメソッドを定義して、そこに渡した数値の分だけSquareオブジェクトの横幅を増やしたり、減らしたり（マイナスの場合）してみよう。
'''

class Square:
    def __init__(self, h):
        self.hen = h
    
    def calculate_perimeter(self):
        return self.hen * 4
    
    def change_size(self, num):
        self.hen += num

squ = Square(10)

print(squ.calculate_perimeter())
print(squ.change_size(5))
print(squ.calculate_perimeter())