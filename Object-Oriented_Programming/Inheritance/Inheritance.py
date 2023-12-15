#1 定义子类
'''
格式：
class ClassName1(ClassName2)
    语句
ClassName1：表示子类（派生类）名
ClassName2：表示基类（父类）名
'''
class Car():
    """汽车之家！."""
    def __init__(self, manufacturer, model, year):
        """初始化操作，建立描述汽车的属性."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回描述信息"""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """行驶里程."""
        print("这是一辆新车，目前仪表显示行驶里程是" + str(self.odometer_reading) + "公里！")

class Bmw(Car):
    """这是一个子类Bmw，基类是Car."""
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year) #函数super()将父类和子类关联起来

my_tesla = Bmw('宝马', '535Li', '2017款')
print(my_tesla.get_descriptive_name())



#2 在子类中定义方法和属性
class Car():
    """汽车之家！."""

    def __init__(self, manufacturer, model, year):
        """初始化操作，建立描述汽车的属性."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回描述信息"""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """行驶里程."""
        print("这是一辆新车，目前仪表显示行驶里程是" + str(self.odometer_reading) + "公里！")

class Bmw(Car):
    """这是一个子类Bmw，基类是Car."""

    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery_size = "6缸3.0T"

    def motor(self):
        """输出发动机参数"""
        print("发动机是" + str(self.battery_size))

my_tesla = Bmw('宝马', '535Li', '2017款')
print(my_tesla.get_descriptive_name())
my_tesla.motor()



#3 创建子类的子类
class Car():
    """汽车之家！."""

    def __init__(self, manufacturer, model, year):
        """初始化操作，建立描述汽车的属性."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回描述信息"""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """行驶里程."""
        print("这是一辆新车，目前仪表显示行驶里程是" + str(self.odometer_reading) + "公里！")

class Bmw(Car):
    """这是一个子类Bmw，基类是Car."""
    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.Motor = Motor()

class Motor(Bmw):
    """类Motor是类Car的子类"""
    def __init__(self, Motor_size=6):
        """初始化发动机属性"""
        self.Motor_size = Motor_size

    def describe_motor(self):
        """输出发动机参数"""
        print("这款车的发动机参数是" + str(self.Motor_size) + "6缸，3.0T涡轮增压，225KW。")

my_tesla = Bmw('宝马', '535Li', '2017款')
print(my_tesla.get_descriptive_name())
my_tesla.Motor.describe_motor()



#4 私有属性和私有方法
'''
当子类继承了父类后，虽然子类具有了父类的属性与方法，但是不能继承父类中的私有属性和私有方法。
'''
#以下是一个反例，虽然类A和类B是继承关系，但是不能相互访问私有变量：
class A:
    def __init__(self):
        # 定义私有属性
        self.__name = "wangwu"
        # 普通属性定义
        self.age = 19
class B(A):
    def sayName(self):
        print (self.__name)
b = B()
b.sayName()



#5 多重继承
'''
在多重继承中，继承顺序是一个很重要的要素。如果继承的多个父类有相同的方法名，但在类中使用时未指定父名，则Python解释器将从左至右搜索，即调用先继承的类中的同名方法。
'''
class PrntOne:
    namea = 'PrntOne'

    def set_value(self, a):
        self.a = a

    def set_namea(self, namea):
        PrntOne.namea = namea

    def info(self):
        print('PrntOne:%s,%s' % (PrntOne.namea, self.a))


class PrntSecond:
    nameb = 'PrntSecond'

    def set_nameb(self, nameb):
        PrntSecond.nameb = nameb

    def info(self):
        print('PrntSecond:%s' % (PrntSecond.nameb,))


class Sub(PrntOne, PrntSecond): #定义子类Sub，先后继承于类PrntOne和PrntSecond
    pass


class Sub2(PrntSecond, PrntOne): #定义子类Sub2，先后继承于类PrntSecond和PrntOne
    pass


class Sub3(PrntOne, PrntSecond): #定义子类Sub3，先后继承于类PrntOne和PrntSecond

    def info(self):
        PrntOne.info(self)
        PrntSecond.info(self)


print('使用第一个子类：')
sub = Sub()
sub.set_value('11111')
sub.info()

sub.set_nameb('22222')
sub.info()

print('使用第二个子类：')
sub2 = Sub2()
sub2.set_value('33333')
sub2.info()

sub2.set_nameb('44444')
sub2.info()

print('使用第三个子类：')
sub3 = Sub3()
sub3.set_value('55555')
sub3.info()

sub3.set_nameb('66666')
sub3.info()



#6 方法重写
class Wai:
    def __init__(self,x=0,y=0,color='black'):
        self.x = x
        self.y = y
        self.color =color

    def haijun(self,x,y):
        self.x = x
        self.y = y
        print('鱼雷...')
        self.info()
    def info(self):
        print('定位目标：(%d,%d)' % (self.x,self.y))  
    def gongji(self): #父类中的原方法
        print("导弹发射！")
class FlyWai(Wai):
    def gongji(self): #子类中的修改后的方法
        print("飞船拦截！")
    def fly(self,x,y):
        print('火箭军...')
        self.x = x
        self.y = y
        self.info()
flyWai = FlyWai(color='red')
flyWai.haijun(100,200)
flyWai.fly(12,15)
flyWai.gongji()
