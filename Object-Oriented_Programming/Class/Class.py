#1 定义并使用类
class MyClass: #定义类MyClass
    "这是一个类."

myclass = MyClass() #实例化类MyClass。 myclass即为一个对象
print('输出类的说明：')
print(myclass.__doc__) #显示属性值。 Python中每个对象都会有个“_doc_”属性，该属性用于描述该对象的作用
print('显示类帮助信息：')
help(myclass)



#2 类对象
class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self): #定义类方法f()
        return 'hello world'

x = MyClass() # 实例化类
# 访问类的属性和方法
print("类MyClass中的属性i为：", x.i)
print("类MyClass中的方法f输出为：", x.f())



#3 类方法
#3.1 定义并使用类方法
class SmplClass:
    def info(self): #定义类方法info()
        print('我定义的类！')

    def mycacl(self, x, y): #定义类方法mycacl()
        return x + y

sc = SmplClass() #实例化类SmplClass
print('调用info方法的结果：')
sc.info()
print('调用mycacl方法的结果：')
print(sc.mycacl(3, 4))


#3.2 构造方法
'''
在定义类时可以定义一个特殊的构造方法，即_init_()方法。
构造方法用于在类实例化时初始化相关数据，如果在这个方法中有相关参数，在实例化时就必须提供。
如果在类中定义了_init_()方法，那么类的实例化操作会自动调用_init_()方法。
'''

class Complex:
    def __init__(self, realpart, imagpart): #定义构造方法
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)


#3.2 方法调用
'''
在Python中，类中的方法既可以调用本类中的方法，也可以调用全局函数来实现相关功能。
调用本类中方法时的格式：
self.方法名(参数列表)
'''

def diao(x,y):
    return (abs(x),abs(y))

class Ant:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.d_point()

    def yi(self,x,y):
        x,y = diao(x,y)
        self.e_point(x,y)
        self.d_point()

    def e_point(self,x,y):
        self.x += x
        self.y += y

    def d_point(self):
        print("亲，当前的位置是：(%d,%d)" % (self.x,self.y))  

ant_a = Ant()
ant_a.yi(2,7)
ant_a.yi(-5,6)


#3.3 创建多个实例
