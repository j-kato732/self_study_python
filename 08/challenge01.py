'''
statisticsモジュールの別の関数を読んでみよう
'''

import statistics

numbers = [234, 1, 46]

# 平均
print(statistics.mean(numbers))
# 中央値
print(statistics.median(numbers))
# 母標準偏差
print(statistics.pstdev(numbers))