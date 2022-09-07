# #approach 1

# import operation

# operation.add(10,20)
# operation.subtract(20,10)


# # Approach 2

# from operation import add,multiplication,subtract

# add(40,50)
# multiplication(10,20)

# from operation import *
# add(3090,3080)
# subtract(3080,89)
# multiplication(46,49)


# accessing 2 same method name using module

#approach 1

# import bird
# import animal

# bird.fly()
# bird.color()

# animal.fly()
# animal.color()

#approach 2
# from bird import fly, color
# from animal import fly, color

# fly()

# color()


# #approach 3

# from bird import fly, color

# fly()

# color()

# from animal import fly, color
# fly()

# color()


# module having classes and methods and call its method in another module
# Approach 1
import imp
import a
import b
animalobj = a.Animal()
animalobj.display()

birdobj = b.Bird()
birdobj.display()

# Approach 2 
from a import Animal
from b import Bird

anobj = Animal()
anobj.display()

birobj = Bird()
birobj.display()









