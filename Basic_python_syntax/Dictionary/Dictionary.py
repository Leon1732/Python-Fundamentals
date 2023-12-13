#1 使用字典
#1.1 创建并访问键值对
'''
格式：
d = {key1 : value1, key : value2}

每个键值对中的键（key）必须是唯一的、不可变的，但值（value）则不必。
'''
dict = {'数学': '99', '语文': '99', '英语': '99' }

print ("语文成绩是：",dict['语文'])
print ("数学成绩是：",dict['数学'])
print ("英语成绩是：",dict['英语'])


#1.2 向字典中添加数据
dict = {'数学': '99', '语文': '99', '英语': '99' }

dict['物理'] =100 #添加字典值1
dict['化学'] =98 #添加字典值2

print (dict)
print ("物理成绩是：", dict['物理'])
print ("化学成绩是：", dict['化学'])


#1.3 修改字典
dict = {'Name': 'Toppr', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8               # 更新 Age
dict['School'] = 'Python教程'  # 添加信息

print ("dict['Age']：", dict['Age'])
print ("dict['School']：", dict['School'])
print (dict)


#1.4 删除字典中元素
dict = {'Name': 'Toppr', 'Age': 7, 'Class': 'First'}
del dict['Name'] # 删除键 'Name'
print (dict)


#1.5 创建空字典
dict = {} #创建空字典
dict['name']='Toppr'
dict['Age']=7
dict['Class']='First'
print (dict)


#1.6 和字典有关的内置函数
dict = {'Name': 'Toppr', 'Age': 7, 'Class': 'First'}
print(len(dict)) #显示总数
print(str(dict)) #显示字典详细信息
print(type(dict)) #返回字典的类型



#2 遍历字典
#2.1 遍历所有键值对
user = {'网名': '浪潮之巅',
          '外号': '浪潮第一帅',
          '职业': '程序员',
          }
for key, value in user.items(): #使用for...in循环语句一次性遍历所有键值对
    print("\nKey: " + key)
    print("Value: " + value)


#2.2 遍历字典中的所有键
favorite_languages = {
    '张三': 'Python',
    '李四': 'C',
    '王五': 'Ruby',
    '赵六': 'Java',
    }
for name in favorite_languages.keys(): #使用方法keys()以列表形式返回一个字典中的所有键
    print(name.title())


#2.3 遍历字典中的所有值
dict = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
print ("字典中所有的值为 : ",  list(dict.values())) #使用方法values()返回一个字典中的所有值



#3 其它内置方法
#3.1 使用方法clear()清空字典
dict = {'Name': 'Zara', 'Age': 7}
print ("字典长度 : %d" %  len(dict))
dict.clear() #不同于del语句，clear语句只是删除了键值，字典还存在
print ("字典删除后长度 : %d" %  len(dict))
print(dict)


#3.2 使用方法copy()复制字典
dict1 = {'Name': 'Toppr', 'Age': 7, 'Class': 'First'}
dict2 = dict1.copy()
print ("新复制的字典为 : ",dict2)


#3.3 使用方法fromkeys()创建新字典
'''
格式：
dict.fromkeys(seq[, value])

seq: 表示字典键值列表
value: 一个可选参数，用于设置键序列（seq）的值
'''
seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
print ("新的字典为 : %s" %  str(dict))
dict = dict.fromkeys(seq, 10)
print ("新的字典为 : %s" %  str(dict))


#3.4 使用方法get()获取指定键值
'''
格式：
dict.get(key, defult=None)

key: 表示在字典中需要查找的键
defult: 表示如果指定键的值不存在，则返回默认值
'''
dict = {'Name': 'Toppr', 'Age': 27}
print ("Age 值为 : %s" %  dict.get('Age'))
print ("Sex 值为 : %s" %  dict.get('Sex', "NA"))


#3.5 使用方法setfault()获取指定的键值
'''
setfault()与get()类似。区别是如果键不在字典中，则会添加键并将值设为默认值
'''
dict = {'Name': 'Toppr', 'Age': 7}
print ("Age 键的值为 : %s" %  dict.setdefault('Age', None))
print ("Sex 键的值为 : %s" %  dict.setdefault('Sex', None))
print ("新字典为：", dict)


#3.6 使用方法update()修改字典
dict = {'Name': 'Toppr', 'Age': 7}
dict2 = {'Sex': 'female' }
dict.update(dict2) #将字典dict2添加到字典dict中
print ("更新字典 dict : ", dict)
