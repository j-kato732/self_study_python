import deck as d
import player as p

class Game:
    def __init__(self):
        name1 = input('プレーヤー1の名前：')
        name2 = input('プレーヤー2の名前：')
        self.deck = d.Deck()
        self.p1 = p.Player(name1)
        self.p2 = p.Player(name2)

    def wins(self, winner):
        w = 'このラウンドは{}が勝ちました'
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = '{} は {}、 {} は {} を引きました'
        d = d.format(p1n.name, p1c, p2n.name, p2c)
        print(d)
    
    def play_game(self):
        cards = self.deck.cards
        print('戦争を始めます!')
        while len(cards) >= 2:
            m = 'q で終了、それ以外のキーでPlay：'
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1
            p2n = self.p2
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print('ゲームの終了、{} の勝利です！'.format(win))
    
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "引き分け！"