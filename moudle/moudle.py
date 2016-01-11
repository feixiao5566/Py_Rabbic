#!/usr/bin/env python
# encoding: utf-8
#标准注释,第一行表示文件可以直接在Unix/Linux/Mac上运行,第2行注释
#表示.py文件本身使用标准UTF-8编码;
#'a test moudle' 任何模块代码的第一个字符串都被视为模块的文档注释
__author__='FeiXiao' #快来瞻仰我的大名
import sys  #导入该模块,我们就有了变量sys指向该模块,利用它,就可以访问该模块所有功能

def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello world")
    elif len(args) == 2:
        print("Hello,%s!" % args[1])
    else:
        print("Too many arguments!")

if __name__=='__main__':
    test()

#当我们在命令行运行这个模块文件时,Python解释器把一个特殊变量__name__置位
#__main__,而如果在其他地方导入该hello模块时,if判断将失败,因此,这种if测试
#可以让一个模块通过命令运行是执行一些额外的代码,最常见的就是运行测试


