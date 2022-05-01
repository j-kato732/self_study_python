'''
コンピューターにある何かのファイルをPythonで開いて、コンテンツを出力しよう。
'''

with open('sample.txt', mode='r') as f:
    lists = f.readlines()
    print(lists)