from mo import moo_fun

name = 'Current module'
def bar():
    print('当前模块中函数bar:')
    print('变量name：',name)

def call_moo_fun(fun):
    fun()

if __name__ == '__main__':
    bar()
    print()
    moo_fun()
    print()
    call_moo_fun(moo_fun)

