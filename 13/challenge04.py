'''
HorseクラスとRiderクラスを定義しよう。
コンポジションを使って馬（Horse)に騎手（Rider)を持たせよう。
'''

class Horse:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

class Rider:
    def __init__(self, name):
        self.name = name

daniel = Rider("daniel")
mike = Horse("mike", daniel)

print(mike.owner.name)