# 1 最基本的模块调用

[实例](Object-Oriented_Programming/Module/11-2)

在这个实例中，测试文件[but.py](Object-Oriented_Programming/Module/11-2/but.py)调用了外部模块文件[module_test.py](Object-Oriented_Programming/Module/11-2/module_test.py)。两个文件保存在同一目录下，可以调用。

若把module_test.py文件保存到[module](Object-Oriented_Programming/Module/11-2/module)目录中，再次运行文件but.py后会引发ImportError错误，因为两个文件不在同一目录下。
