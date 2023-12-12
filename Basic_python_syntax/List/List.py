#1 列表基础
#1.1 创建列表
list1 = [1, 1.1, 'abc'] #在列表中放入一个整型1，一个浮点型1.1，一个字符串abc
print(list1)

numbers = list(range(1, 4))	#使用方法方法range()创建列表
print(numbers)


#1.2 访问列表中的值
list1 = ['Google', 'baidu', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];

print ("list1[0]: ", list1[0]) #输出list1中的第1个元素
print ("list2[1:5]: ", list2[1:5]) #输出list2中的第2-5个元素


#1.3 使用列表中的值
car = ['奥迪', '宝马', '奔驰', '雷克萨斯']
message = "我人生中的第一辆汽车是:" + car[0].title() + "."
print(message)



#2 列表基本操作
#2.1 更新列表元素
car = ['奥迪', '宝马', '奔驰', '雷克萨斯']
print(car)
car[0] = '沃尔沃' #将car中第一个元素替换
print(car)


#2.2 插入新的元素
car = ['奥迪', '宝马', '奔驰', '雷克萨斯']
print(car)
car.insert(0, '凯迪拉克') #将新的元素存储到car列表索引为0的位置
print(car)

car = ['奥迪', '宝马', '奔驰', '雷克萨斯']
print(car)
car.append('凯迪拉克') #在列表末尾添加新元素
print(car)


#2.3 在列表中删除元素
#2.3.1 使用del语句（删除的元素不再使用）
car = ['奥迪', '宝马', '奔驰', '雷克萨斯']
print(car)
del car[0] #删除列表中索引值为0的元素
print(car)

#2.3.2 使用pop()方法（删除的元素后面会继续使用）
car = ['奥迪', '宝马', '奔驰', '雷克萨斯']
print(car)
car.pop(1) #删除列表中索引值为1的元素
print(car)

#2.3.3 显示删除的元素
car = ['奔驰', '宝马', '奥迪']
first_owned = car.pop(0)
print('我人生中的第一辆汽车是：' + first_owned.title() + '！')
print(car)

#2.3.4 删除列表中指定值的元素
car = ['奔驰', '宝马', '奥迪']
print(car)
car.remove('宝马') #删除列表中值为“宝马”的元素，使用remove()后仍可以使用被删除的值
print(car)



#3 列表排列处理
#3.1 sort()方法对列表永久性排序
car = ['benchi', 'baoma', 'aodi', 'leikesasi']
car.sort() #按元素中字母数量由小到大排列
print(car)

car = ['benchi', 'baoma', 'aodi', 'leikesasi']
car.sort(reverse=True) #按元素中字母数量由大到小排列
print(car)


#3.2 sorted()方法对列表临时排序
cars = ['benchi', 'baoma', 'aodi', 'leikesasi']
print("列表中原来的排列顺序是：")
print(cars)

print("\n经过排列处理后的顺序：")
print(sorted(cars))

print("\n再次显示列表中原来的排列顺序是：")
print(cars)


#3.3 倒序输出列表信息
cars = ['benchi', 'baoma', 'aodi', 'leikesasi']
print("列表中原来的排列顺序是：")
print(cars)

print("\n经过排列处理后的顺序：")
cars.reverse()
print(cars)
print("\n再次显示当前列表的排列顺序是：")
print(cars)



#4 列表高级操作
#4.1 列表中的运算符（见图1）


#4.2 列表截取与拼接
L=['Google', ' Apple ', 'Taobao']
print(L[2]) #显示列表L中的第3个元素
print(L[-2]) #显示列表L中的倒数第2个元素
print(L[1:]) #显示从第2个元素开始后的所有元素
squares = [1, 4, 9, 16, 25]
print(squares + [36, 49, 64, 81, 100])


#4.3 列表嵌套
m = ['a', 'b', 'c']
n = [1, 2, 3]
x = [m, n]
print(x) #同时输出列表m和列表n的值
print(x[0]) #输出x中位置为0的元素，即列表m的值
print(x[0][1]) #输出x中位置为0的列表中位置为1的元素值


#4.4 获取列表元素中的最大值和最小值
list1, list2 = ['Google', 'Apple', 'Taobao'], [456, 700, 200]

print ("list1 最大元素值 : ", max(list1))
print ("list2 最大元素值 : ", max(list2))
print ("list1 最小元素值 : ", min(list1))
print ("list2 最小元素值 : ", min(list2))


#4.5 追加其它列表中的值
list1 = ['Google', 'Apple', 'Taobao']
list2=list(range(5)) # 创建 0-4 的列表
list1.extend(list2)  # 扩展列表
print ("扩展后的列表：", list1)


#4.6 统计列表中某元素出现次数
aList = [123, 'Google', 'Apple', 'Taobao', 123];

print ("统计元素“123 ”的个数 : ", aList.count(123))
print ("统计元素“Apple”的个数 : ", aList.count('Apple'))


#4.7 清空列表中元素
list1 = [123,'Google', 'Runoob', 'Taobao', 'Baidu',456]
list1.clear()
print ("列表已经被清空，现在还有元素：", list1)


#4.8 复制列表元素
list1 = ['Google', 'Apple', 'Taobao', 'Baidu']
list2 = list1.copy()
print ("list2列表中的元素是从列表list1中复制而来的：", list2)


#4.9 获取列表中某个元素索引值
list1 = ['Google', 'Apple', 'Taobao', 'Baidu']
print ('Apple的索引值为', list1.index('Apple'))
print ('Taobao的索引值为', list1.index('Taobao'))
print ('Baidu的索引值为', list1.index('Baidu'))
print ('Google的索引值为', list1.index('Google'))
