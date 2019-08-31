class Test:
    def __init__(self, age):
        self.age = age
    name = "asdas"

    @classmethod
    def add(cls):
        print(cls.name)


class Foo(Test):
    def __init__(self):
        super(Test, self).__init__()




