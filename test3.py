"""
 * Project name(项目名称)：Python__all__变量
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 13:22
 * Version(版本): 1.0
 * Description(描述)： 
 """

str1 = "hello"
__str2 = "hello"
str3 = "hello"


def f1():
    """
    f1
    :return:
    """
    print("调用f1()")


def f2():
    """
    f2
    :return:
    """
    print("调用f2()")


def f3():
    """
    f3
    :return:
    """
    print("调用f3()")


def f4():
    """
    f4
    :return:
    """
    print("调用f4()")


def __f5():
    """
    f5
    :return:
    """
    print("调用f5()")


__all__ = ["f1", "f2", "f3", "__f5", "str1","__str2"]
