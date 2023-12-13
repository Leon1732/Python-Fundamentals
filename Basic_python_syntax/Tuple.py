#1 创建并访问元组
#1.1 创建并访问元组
tup1 = ('Google', 'toppr', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

print ("tup1[0]: ", tup1[0]) #显示元组中索引为0的元素值
print ("tup2[1:5]: ", tup2[1:5]) #显示元组中索引从1到4的元素值


#1.2 for循环遍历元组值
dimensions = (200, 50)
print("元组dimensions的数据元素有：")
for dimension in dimensions:
    print(dimension)



#2 修改元组
#2.1 连接两个元组值
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2; #创建一个新的元组tup3
print (tup3)


#2.2 修改元组变量值
# 虽然语法规定元组内的元素值不能被修改，但可以给存储元组的变量重新赋值，从而达到修改元组的目的
int1 = (200, 50)
print("原来的值是：")
for dimension in int1:
    print(dimension)

int1 = (400, 100)
print("\n修改后的值是：")
for dimension in int1:
    print(dimension)


#3 删除元组
tup = ('Google', 'Toppr', 1997, 2000)
print (tup)
del tup #使用del语句删除整个元组，删除后该元组将不存在



#4 元组索引和截取
L = ('Google', 'Taobao', 'Toppr')
print(L[2]) #读取元组L中的第3个元素
print(L[-2]) #读取元组L中的倒数第2个元素
print(L[1:]) #截取元组L中从第2个元素开始的所有元素


#5 使用内置方法操作元组（统计个数，最大值，最小值，列表转换元组）
car = ['奥迪', '宝马', '奔驰', '雷克萨斯']
print(len(car)) #输出列表car的长度
tuple2 = ('5', '4', '8')
print(max(tuple2)) #显示元组tuple2中元素最大值
tuple3 = ('5', '4', '8')
print(min(tuple3)) #显示元组tuple3中元素最小值
list1= ['Google', 'Taobao', 'Toppr', 'Baidu']
tuple1=tuple(list1)
print(tuple1)
