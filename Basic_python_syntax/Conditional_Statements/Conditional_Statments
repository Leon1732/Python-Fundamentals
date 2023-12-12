#if...else 语句
x = input('请输入一个整数：')
x = int(x)
if x < 0:
    print('大哥，你输的是一个负数。')
else:
    print('大哥，你输的是零或正数。')


#if...elif...else 语句
x = input('小朋友，请输入你的二级C语言成绩：')
x = float(x)
if x >= 90:
    print('你的成绩为：优。')
elif x >= 80:
    print('你的成绩为：良。')
elif x >= 70:
    print('你的成绩为：中。')
elif x >= 60:
    print('你的成绩为：合格。')
else:
    print('你的成绩为：不合格。')


#switch 语句
#由于python没有switch语句，需要用其它方式实现。以下介绍三种方法：
#1. elif实现
num = 9
if num >= 0 and num <= 10:    # 判断值是否在0~10之间
    print ('hello')             # 输出结果

num = 10
if num < 0 or num > 10:       # 判断值是否在小于0或大于10
    print ('hello')
else:
	print ('undefine')      # 输出结果

num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print ('hello')
else:
    print ('undefine')          # 输出结果


#2. 自定义类实现
class switch(object):
    def __init__(self, value):      # 初始化需要匹配的值value
        self.value = value
        self.fall = False  # 如果匹配到的case语句中没有break，则fall为true。

    def __iter__(self):
        yield self.match  # 调用match方法 返回一个生成器
        raise StopIteration  # StopIteration 异常来判断for循环是否结束

    def match(self, *args):  # 模拟case子句的方法
        if self.fall or not args:  # 如果fall为true，则继续执行下面的case子句
            # 或case子句没有匹配项，则流转到默认分支。
            return True
        elif self.value in args:  # 匹配成功
            self.fall = True
            return True
        else:  # 匹配失败
            return False

operator = "+"
x = 1
y = 2
for case in switch(operator):  # switch只能用于for in循环中
    if case('+'):
        print(x + y)
        break
    if case('-'):
        print(x - y)
        break
    if case('*'):
        print(x * y)
        break
    if case('/'):
        print(x / y)
        break
    if case():  # 默认分支
        print("")


#3. 使用字典实现
from __future__ import division
x = 1
y = 2
operator = "/"
result = {
    "+" : x + y,
    "-" : x - y,
    "*" : x * y,
    "/" : x / y
}
print (result.get(operator))
