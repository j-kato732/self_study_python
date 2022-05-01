'''
三角形を表すTriangleクラスを定義して、面積を返すareaメソッドを持たせよう。
そしてTriangleオブジェクトを作って、areaメソッドを呼び出して、結果を出力しよう
'''

class Triangle:
    def __init__(self, h, b):
        self.height = h
        self.bottom = b

    def area(self):
        return self.height * self.bottom * 0.5

tri = Triangle(20, 10)
print(tri.area())