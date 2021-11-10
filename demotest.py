# a='Hello'
# b=' '
# c='World'
# d='!'
# print(a+b+c+d)
# print (type('a,b,c,d'))
# num1 = 10
# num2 = 3
# result = num1 / num2
# print(result)
# --任务
# 一个长方形的长为3.14cm，宽为1.57cm，请计算这个长方形的面积，保留小数点后两位。
# print(round(3.14 * 1.57,2))

# s = 'ABED'
# for ch in s:
# print(ch)
# num = 1
# num1 = 1
# while num <= 10:
#     num1 = num1 * num
#     num = num + 1
# print(num1)
#
# s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
# num = 1
# sum = 0
# while True:
#     if num > 100:
#         break
#     sum = sum + num
#     num = num + 1
# print(sum)
#
# num = 0
# sum = 0
# while True:
#     if num > 1000:
#         break
#     if num % 2 == 0:
#         sum = sum + num
#     num = num + 1
# print(sum)

# num = 2
# sum = 0
# while True:
#     if num > 1000:
#         break
#     sum = sum + num
#     num = num + 2
# print(sum)
#
# sum = 0
# num = 0
# while num < 1000:
#     num = num + 1
#     if num % 2 == 1:
#         continue
#     sum = sum + num
# print(sum)

# names = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
# name = names.pop(2)
# print(name)
# print(names)
#
# names = ['Alice', 'Bob', 'Candy', 'David', 'Ellena']
# names.insert(5,'Gen')
# names.insert(6,'Phoebe')
# names.append('Zero')
# print(names)
"""
list列表操作函数
pop()方法默认删除列表的最后一个元素，并返回。也可以指定需要删除元素的位置
insert()方法可以在列表通过从索引增加元素
append()方法默认删除
tuple元祖操作函数
count()哟呵你过来统计tuple中某个元素出现的次数，但是对于不存在的元素，count()方法不会报错而是返回0
index()方法可以返回指定元素的下标，当一个元素多次重复出现时，则返回第一次出现的下标位置。与count()方法不一样的是当指定元素不存在时会报错

"""


# score = (100, 69, 29, 100, 72, 99, 98, 100, 75, 100, 100, 42, 88, 100)
# print(score.count(100))

# alice_scores = [100, 89, 92]
# bob_scores = [70, 65, 81]
# candy_scores = [88, 72, 77]
# all_scores = [alice_scores, bob_scores, candy_scores]
# print(all_scores)
# score = all_scores[1]
# print(score)
#
# T = (0,1,2,3,4,5,6,7,8,9)
# L = list(T)
# print(L)
#
# T = (1, 'CH', [3, 4])
# print(T)
# L = []
# x = 1
# while x <= 100:
#     L.append(x * x)
#     x = x + 1
# print(sum(L))


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


def list_sum(L):
    result = 0
    for num in L:
        result = result + num
    return result


L = [1, 3, 5, 7, 9, 11]
result = list_sum(L)
print(result)


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(10))


def greet(s='world'):
    return 'Hello,{}.'.format(s)


print(greet())
print(greet('Python'))


def greet(n='world'):
    if n == 'world':
        print('Hello,world.')
    else:
        print('Hello,{}'.format(n))


greet()
