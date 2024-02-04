class A:

    # def __init__(self, ilya):
    #     self.b = ilya
    def func(self):
        print("Hello")


class B(A):
    a = 5
    def func(self):
        print("Privet")

B().func()
#     @staticmethod
#     def func2():
#         print("hello2")
#
# a = A("Helloworld")
# c = A("No")
# a.func()
# c.func()
