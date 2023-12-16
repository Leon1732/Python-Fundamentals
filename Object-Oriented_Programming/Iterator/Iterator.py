#1 创建并使用迭代器
class Use:

    def __init__(self,x=2,max=50):
        self.__mul,self.__x = x,x
        self.__max = max

    def __iter__(self): #定义迭代器协议方法
        return self

    def __next__(self): #定义迭代器协议方法
        if self.__x and self.__x != 1:
            self.__mul *= self.__x
            if self.__mul <= self.__max:
                return self.__mul
            else:
                raise StopIteration #当超过参数max的值时会引发StopIteration异常
        else:
            raise StopIteration

if __name__ == '__main__':
    my = Use()
    for i in my:
        print('迭代的数据元素为：',i)



#2 使用内置迭代器方法iter()
'''
格式：
iter(iterable)
iter(callable, sentinel)

第一种：只有一个参数iterable，要求参数为可迭代类型，也可以使用各种序列类型。
第二种：第一个参数callable表示可调用类型，一般为函数；第二个参数sentinel是一个标记，当第一个参数（函数）的返回值等于第二个参数的值时，迭代或遍历会立马停止。
'''
class Counter:
    def __init__(self, x=0):
        self.x = x

counter = Counter()

def used_iter():
    counter.x += 2
    return counter.x


for i in iter(used_iter, 12):
    print('当前遍历的数值：', i)
