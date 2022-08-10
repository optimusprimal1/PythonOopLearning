# Private variables can be access only within  the class
# class myClass:
#     __a  = 10
#     def disp(self):
#         print(self.__a)
#         self.__disp1()
#
#     def __disp1(self):
#         print("This is a private method.")


# mc = myClass()
# mc.disp()

# We can access private variables outside of class indirectly using methods
class myClass:
    __a  = 10
    def getempid(self,empid):
        self.__a= empid

    def dispempid(self):
        print('Displaying emp id', self.__a)




myclas = myClass()
myclas.getempid(200)
myclas.dispempid()

#calling private variables and methods are accessible outside class by using _classname

class Test:
    __a = 10

    def __m1(self):
        Test.__a = 20
        print(self.__a)


t = Test()
t._Test__m1()
print(t._Test__a)
print(Test._Test__a)
print(Test.__dict__)
