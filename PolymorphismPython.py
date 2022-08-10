#overriding variables

class Parent:
    name="Scott"

class Child(Parent):
    # name = "David"
    pass


# c= Child()
# print('c.name = ',c.name)

# Overrding method

class Bank:
    def rateofInterent(self):
        return 0

class ICICI(Bank):
    def rateofInterent(self):
        return 10.5



# ic = ICICI()
# print('ic.rateofInterent() = ',ic.rateofInterent())
#
# bank  = Bank()
# print('bank.rateofInterent() = ',bank.rateofInterent())


# Method overloading

class Human:
    def sayhello(self, name=None):
        if name is not None:
            print("My name is ", name)
        else:
            print("Hello")

obj = Human()
obj.sayhello("Syed M Usama")
obj.sayhello()
