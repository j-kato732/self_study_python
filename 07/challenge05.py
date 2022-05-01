'''
2つのリストに含まれる全ての数字の組み合わせで掛け算しよう。
1つ目のリストは[8, 19, 148, 4],
2つ目のリストは[9, 1, 33, 83]で、
それぞれ掛け算した結果は新しいリストに格納しよう。
'''

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
results = []


for num in list1:
    for num2 in list2:
        results.append(num * num2)

print(results)