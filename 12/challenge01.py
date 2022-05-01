'''
りんごと言われて思い浮かぶ、4つの属性を考えよう。
その4つの属性をインスタンス変数にもつ、Appleのクラスを定義しよう。
'''

class Apple:
    def __init__(self, w, c, l, v):
        self.weight = w
        self.color = c
        self.leaf = l
        self.value = v
        print('Created')

apple = Apple(200, "red", True, 100)
print(apple.weight)
print(apple.color)
print(apple.leaf)
print(apple.value)