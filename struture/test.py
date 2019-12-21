class Foo:

    @staticmethod
    def aaa():
        print(111)

    @classmethod
    def bbb(cls):
        print(222)



# a = Foo()
# a.aaa()
# Foo.aaa()
# a.bbb()
# Foo.bbb()


# class obj:
#     number = 0
#     def __init__(self):
#         self.number += 1
#
#
# a = obj()
# b = obj()
# print(a.number)
# print(b.number)


class Test(object):
    num_of_instance = 0
    _foo = 2
    def __init__(self, name):
        self.name = name
        Test.num_of_instance += 1

    def a(self):
        print()


class Test2(Test):
    def b(self):
        print(self.name)


if __name__ == '__main__':

    # t1 = Test('jack')
    #
    # t2 = Test('lucy')
    # print(
    # t1.name, t1.num_of_instance)  # jack 2
    # print(
    # t2.name, t2.num_of_instance  # lucy 2
    # )
    # Test2('lxl').b()
    # print(Test._foo)

    def a_new_decorator(f):
        def wrapTheFunction():
            print("I am doing some boring work before executing a_func()")



            print("I am doing some boring work after executing a_func()")

        return wrapTheFunction

    @a_new_decorator
    def a_function_requiring_decoration():
        print("I am the function which needs some decoration to remove my foul smell")


    # a_function_requiring_decoration()
    # outputs: "I am the function which needs some decoration to remove my foul smell"

    # a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
    # # now a_function_requiring_decoration is wrapped by wrapTheFunction()
    #
    # a_function_requiring_decoration()
    a_function_requiring_decoration()


    class A:
        def __init__(self):
            print('A')
        def foo1(self):
            print("A")



    class B(A):

        def foo2(self):
            pass


    class C(A):

        def foo1(self):
            print('C')



    class D(B, C):
        pass


    d = D()
    d.foo1()



    class d:
        def __init__(self):

            if not hasattr(self, '__instance'):
                __instance = d()

            return __instance

