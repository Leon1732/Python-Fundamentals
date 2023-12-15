# 1 最基本的模块调用

[实例]()

在这个实例中，测试文件but.py调用了外部模块文件module_test.py。两个文件保存在同一目录下，可以调用。

若把module_test.py文件保存到module目录中，再次运行文件but.py后会引发ImportError错误，因为两个文件不在同一目录下。
