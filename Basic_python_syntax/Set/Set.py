student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)   # 输出集合，重复的元素被自动去掉

# 测试成员'Rose'是否在集合中
if('Rose' in student) :
    print('Rose 在集合中')
else :
	print('Rose 不在集合中')


# set可以进行集合运算
a = set('abcde') #创建集合“a”
b = set('abc') #创建集合“b”
print(a)
print(a - b)     # a和b的差集
print(a | b)     # a和b的并集
print(a & b)     # a和b的交集
print(a ^ b)     # a和b中不同时存在的元素
