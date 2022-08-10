# class MyClass:
#     def myFunc(self):
#         pass
#
#     def display(abc,name):
#         print("Name is : ",name)
#
#
# # mc  = MyClass()
# # mc.myFunc()
# # mc.display("Syed M Usama")
#
# # Instance method and static method
#
# class MyClass1:
#     def myFunc(self):
#         print("Instance Method")
#
#     @staticmethod
#     def display(name):
#         print("(Static method) Name is : ",name)
#
#
# mc1 = MyClass1()
# # called instance method
# mc1.myFunc()
# # called static method
# mc1.display("Syed M Usama")
#
#
# # Declaring local variables, class variables, Global variables
# i , j = 10 , 25
# class MyClass2:
#     a,b = 100,200
#
#     def add(self, x , y): # local variables
#         print('Sum of two numbers are  = ', x + y)
#
#     def add1(self): # class variables
#         print('Sum of two numbers are  = ', self.a+self.b)
#
#     def multiply(self): # accessing global variables
#         print('Product of two numbers are  = ', i * j)
#
# mc2 = MyClass2()
# mc2.add(100,200)
# mc2.add1()
# mc2.multiply()

# Access all variable with same variable name
a , b = 10 , 25
class MyClass3:
    a,b = 100,200

    def add(self, a , b):
        print('Accessing local Variables = ', a + b) # local variables
        print('Accessing class Variables = ', self.a + self.b) # class variables
        print('Accessing global Variables = ', globals()['a']  + globals()['b']) # global variables

mc3 = MyClass3()
mc3.add(100,500)

