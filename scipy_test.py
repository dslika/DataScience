# import numpy as np

# # 入力ブロック
# count = int(input().rstrip())
# inputs = []
# for i in range(count):
#     inputs.append(input())
#
# # テストデータを設定
# count = 5
# inputs = ["3", "4", "1", "5", "10"]
#
# # 処理
# sum1 = 0
# for data in inputs:
#     sum1 += int(data)
# # 出力
# print(sum1)

# def star_main():
# input_lines = int(input())
#
# data = [1, 2, 3, 4, 5]  # 配列の生成
#
# for i in range(input_lines):
#     s = input().rstrip().split(' ')
#
#     ave = sum(data) / len(data)  # 合計/配列の長さ(データの個数)で平均値を計算
#     print ave
#     # if i == input_lines - 1:
#     #     print("*")
#     # else:
#     #     print("*", end='')

# input_lines = int(input())
# for i in range(input_lines):
#     s = input().rstrip().split(',')
#     print("hello = " + s[0] + " , world = " + s[1])

# D069:割り切れない平均点
# s = [int(i) for i in input().rstrip().split(' ')]
# ave = sum(s) / len(s)  # 合計/配列の長さ(データの個数)で平均値を計算
# print(round(ave, 1))

# C006:ハイスコアランキング
# 入力部分
# input_s1 = input().rstrip().split(' ')
# input_s2 = input().rstrip().split(' ')
# input_s3 = input().rstrip().split(' ')

# スコア計算部分

#
# convert_dict = {
#     'A': 4,
#     'E': 3,
#     'G': 6,
#     'I': 1,
#     'O': 0,
#     'S': 5,
#     'Z': 2
# }
# li = []
# for v in t:
#     li.append(str(convert_dict.get(v, v)))
# print("".join(li))

# input_s1 = input()
#
# s = 0
# for i in range(int(input_s1)):
#     s += (i + 1)
#
# print(s)


# input_lines = int(input())
#
# le = []
# ge = []
# for i in range(input_lines):
#     input_s1 = input().rstrip().split(' ')
#     if input_s1[0] == 'le':  # <
#         le.append(input_s1[1])
#     if input_s1[0] == 'ge':  # <
#         ge.append(input_s1[1])
#
# print(max(ge) + ' ' + min(le))

# C039: 古代の数式
# from collections import Counter
#
# input_s1 = input().rstrip().split('+')
#
# num = 0
# for v in input_s1:
#     counter = dict(Counter(v))
#     num += counter.get('<', 0) * 10 + counter.get('/', 0)
#
# print(num)


# # mod7占い
#
# import itertools
#
# # count = 10
# # inputs = list(range(1, 11))
#
# count = int(input().rstrip())
# inputs = []
# for i in range(count):
#     inputs.append(input())
#
# # 処理
# sum1 = 0
# main_list = list(itertools.combinations(inputs, 3))
# for v in main_list:
#     sum2 = 0
#     for v1 in v:
#         sum2 += int(v1)
#     if sum2 % 7 == 0:
#         sum1 = sum1 + 1
#
# print(sum1)


# B040: たのしい暗号解読
param = input().rstrip().split(',')
pass_text = input().rstrip().split(' ')

# テストデータを設定
# param = ['2', 'qwertyuiopasdfghjklzxcvbnm']
# pass_text = "hqomq gfsoft iqeaqzigf"

st = [chr(i) for i in range(ord('a'), ord('z') + 1)]
pass_dict = dict(zip(param[1], st))


def check_pass(input_s1):
    main_list = []
    # main_text = ''
    for code in input_s1.split(' '):
        text = ''
        for s in code:
            text += pass_dict.get(s)

        main_list.append(text)
    return ' '.join(main_list)


for i in range(int(param[0])):
    pass_text = check_pass(pass_text)

print(pass_text)
