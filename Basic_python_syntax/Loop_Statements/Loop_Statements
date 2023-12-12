#1 for循环
#1.1 基本for循环
'''
格式：
for iterating_var in sequence:
    statements

iterating_var: 表示循环变量
sequence: 表示遍历对象，通常是元组、列表和字典等
statements: 表示执行语句
'''
for letter in 'Python':     # 第一个实例
   print ('当前字母 :', letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print ('当前单词 :', fruit)


#1.2 通过序列索引迭代（使用range）
'''
格式：
range([start,] stop[, step])

start: 可选参数，起始数，默认值为0
stop: 终止数，如果range只有一个参数x，那么range产生一个从0至x-1的整数列表
step: 可选参数，表示步长
'''
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('当前水果 :', fruits[index])


#1.3 for...else循环
'''
格式：
for iterating_var in sequence:
    statements1
else:
    statements2

iterating_var: 表示循环变量
sequence: 表示遍历对象，通常是元组、列表和字典等
statements1: 表示for语句的循环体
statements2: 只有在循环正常退出（即遍历完所有遍历对象中的值）时才执行
'''
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print ('%d 等于 %d * %d' % (num,i,j))
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print (num, '是一个质数')


#2 while循环
#2.1 基本while循环
count = 0
while (count < 9):
   print ('The count is:', count)
   count = count + 1


#2.2 while...else循环（和for...else类似）
count = 0
while count < 5:
   print (count, "小于5")
   count = count + 1
else:
   print (count, "不小于5")
