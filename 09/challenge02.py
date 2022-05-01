'''
何か質問するプログラムを書こう。
入力された回答をファイルに書き出そう。
'''

question = 'なぜ人は生きるのでしょうか'

ans = input(f'{question}: ')

with open('answer.txt', mode='w') as f:
    f.write(ans)