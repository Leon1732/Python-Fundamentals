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
'''
定义类方法的方式与其他一般函数的定义方式类似，但有如下区别：
* 方法的第一个参数必须是self，而且不能省略
* 方法的调用需要实例化，并以”实例名.方法名(参数列表)“的形式进行调用
'''
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
在定义类时可以定义一个特殊的构造方法，即__init__()方法。
构造方法用于在类实例化时初始化相关数据，如果在这个方法中有相关参数，在实例化时就必须提供。
如果在类中定义了_init_()方法，那么类的实例化操作会自动调用_init_()方法。
'''

class Complex:
    def __init__(self, realpart, imagpart): #定义构造方法
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)


#3.3 方法调用
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


#3.4 创建多个实例
class Dog():
    """小狗狗"""
    def __init__(self, name, age):
        """初始化属性name和age."""
        self.name = name
        self.age = age
    def wang(self):
        """模拟狗狗汪汪叫."""
        print(self.name.title() + " 旺旺")
    def shen(self):
        """模拟狗狗伸舌头."""
        print(self.name.title() + "伸舌头")

my_dog = Dog('将军', 6)
your_dog = Dog('武士', 3)

print("我爱犬的名字是" + my_dog.name + ".")
print("我的爱犬已经" + str(my_dog.age) + "岁了！")
my_dog.wang()

print("\n你爱犬的名字是" + your_dog.name + ".")
print("你的爱犬已经" + str(your_dog.age) + "岁了！")
your_dog.wang()


#3.5 使用私有方法
'''
如果一个Python函数、类方法或属性的名字以两条下划线“_”开始，那么这个函数、方法或属性就是私有的。
在类的内部调用私有方法的语法格式：
self.__方法名

私有函数、方法或属性的特点：
私有函数不可以从它们的模块外面调用
私有类方法不能从它们的类外面调用
私有属性不能从它们的类外面调用
'''
class Site:
	def __init__(self, name, url):
		self.name = name       # public
		self.__url = url   # private

	def who(self):
		print('name  : ', self.name)
		print('url : ', self.__url)

	def __foo(self):          # 定义私有方法
		print('这是私有方法')

	def foo(self):            # 定义公共方法
		print('这是公共方法')
		self.__foo()

x = Site('菜鸟教程', 'www.toppr.net')
x.who()        # 正常输出
x.foo()        # 正常输出
#x.__foo()      # 报错，因为在外部调用了私有方法


#3.6 析构方法
'''
析构方法是__del__()
当使用内置方法del()删除对象时，会调用它本身的析构函数。
另外，当一个对象在某个作用域中调用完毕后，在跳出其作用域的同时也会调用析构函数一次，这样可以使用析构方法__del__()释放内存空间。
'''


class NewClass(object):
    num_count = 0  # 所有的实例都共享此变量，即不单独为每个实例分配

    def __init__(self, name):
        self.name = name
        NewClass.num_count += 1
        print(name, NewClass.num_count)

    def __del__(self):
        NewClass.num_count -= 1
        print("Del", self.name, NewClass.num_count)

    def test():
        print("aa")

aa = NewClass("Hello")
bb = NewClass("World")
cc = NewClass("aaaa")
del aa #调用析构
del bb #调用析构
del cc #调用析构
print("Over")


#3.7 静态方法和类方法
'''
在调用类方法和静态方法时，可以直接由类名进行调用，在调用前无须实例化类。
也可以使用类的任一个实例进行调用
'''
class Jing:
    def __init__(self, x=0): #定义构造方法
        self.x = x

    @staticmethod #使用静态方法装饰器
    def static_method(): #定义静态类方法
        print('此处调用了静态方法！')

    @classmethod #使用类方法装饰器
    def class_method(cls): #定义类方法，默认参数是cls
        print('此处调用了类方法！')

Jing.static_method() #没有实例化类，通过类名调用静态方法
Jing.class_method() #没有实例化类，通过类名调用类方法
dm = Jing()
dm.static_method() #通过类实例调用静态方法
dm.class_method() #通过类实例调用类方法



#4 类属性
#4.1 类属性和实例属性
'''
实例属性：是同一个类的不同实例，其值是不相关联的，也不会互相影响，在定义时使用”self.属性名“的格式定义，在调用时也使用这个格式调用。
类属性：是同一个类的所有实例所共有的，直接在类体中独立定义，在引用时使用”类名.类变量名“的格式，只要某个实例对其进行修改，就会影响这个类的其他实例。
'''
class X_Property:
    class_name = "X_Property" #设置类的属性

    def __init__(self,x=0):
        self.x = x #设置实例属性

    def class_info(self):
        print('类变量值：',X_Property.class_name) #输出类变量值
        print('实例变量值：',self.x) #输出实例变量值

    def chng(self,x): #定义方法chng()修改实例属性
        self.x = x

    def chng_cn(self,name): #定义方法chng_cn()修改类属性
        X_Property.class_name = name

aaa = X_Property() #定义类的实例化对象aaa
bbb = X_Property() #定义类的实例化对象bbb
print('初始化两个实例')
aaa.class_info()
bbb.class_info()

print('\n修改实例变量')
print('修改aaa实例变量')
aaa.chng(3)        #修改对象aaa的实例变量
aaa.class_info()
bbb.class_info()
print('修改bbb实例变量')
bbb.chng(10)        #修改对象bbb的实例变量
aaa.class_info()
bbb.class_info()

print('\n修改类变量')
print('修改aaa类变量')
aaa.chng_cn('aaa')  #修改aaa的类变量
aaa.class_info()
bbb.class_info()
print('修改bbb实例变量')
bbb.chng_cn('bbb')  #修改bbb的类变量
aaa.class_info()
bbb.class_info()


#4.2 使用私有属性
class Person:

   def __init__(self):
       self.__name = 'haha' #设置私有属性
       self.age = 22

   def get_name(self):
       return self.__name

   def get_age(self):
       return self.age

person = Person()
print (person.get_age())
print (person.get_name())
