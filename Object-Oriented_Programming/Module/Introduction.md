# 1 最基本的模块调用

[实例](11-2)

在这个实例中，测试文件[but.py](11-2/but.py)调用了外部模块文件[module_test.py](11-2/module_test.py)。两个文件保存在同一目录下，可以调用。

若把module_test.py文件保存到[module](11-2/module)目录中，再次运行文件but.py后会引发ImportError错误，因为两个文件不在同一目录下。

# 2 编译指定文件

[实例](11-3)

该实例中文件bianyi.py将同目录下文件mokuai.py编译成文件mokuai.pyc。运行mokuai.pyc和单独运行mokuai.py效果是一样的。mokuai.pyc是以Python字节码的形式存在，起到防止源码泄露的作用。.pyc文件可以用cmd运行，可输入以下指令运行：

`python xxx.pyc`
