print("----------------------------------------------------")

#single inheritence example in Python
class parentclass:
    def parentmethod(self):
        print("This is a method from the parent class.")

class childclass(parentclass):
    def childmethod(self):
        print("This is a method from the child class.")

# Create an instance of the child class
child_instance = childclass()
# Call methods from both the parent and child classes
child_instance.parentmethod()   
child_instance.childmethod()




print("\n")  # Print a newline for better readability
print("----------------------------------------------------")






#Multiple inheritance example in Python
class Parent1:
    def method1(self):
        print("This is a method from Parent 1.")

class Parent2:
    def method2(self):
        print("This is a method from Parent 2.")

class Child(Parent1, Parent2):
    def child_method(self):
        print("This is a method from the Child class.")

# Create an instance of the Child class
child_instance = Child() 


# Call methods from both parent classes and the child class
child_instance.method1()
child_instance.method2()
child_instance.child_method()





print("\n")  # Print a newline for better readability
print("----------------------------------------------------")






# Multilevel inheritance example in Python
class Grandparent:
    def grandparent_method(self):
        print("This is a method from the Grandparent class.")

class Parent(Grandparent):
    def parent_method(self):
        print("This is a method from the Parent class.")

class Child(Parent):
    def child_method(self):
        print("This is a method from the Child class.") 

# Create an instance of the Child class
child_instance = Child()    
# Call methods from the grandparent, parent, and child classes
child_instance.grandparent_method()
child_instance.parent_method()
child_instance.child_method()




print("\n")  # Print a newline for better readability
print("----------------------------------------------------")   






# Hierarchical inheritance example in Python
class Parent:
    def parent_method(self):
        print("This is a method from the Parent class.")

class Child1(Parent):
    def child1_metod(self):
        print("This is a method from Child 1 class.")

class Child2(Parent):
    def child2_method(self):
        print("This is a method from Child 2 class.")   

# Create instances of Child1 and Child2
child1_instance = Child1()  
child2_instance = Child2()
# Call methods from the parent class and child classes
child1_instance.parent_method()
child1_instance.child1_metod()
child2_instance.parent_method()
child2_instance.child2_method()
print("\n")  # Print a newline for better readability
print("----------------------------------------------------")

# Hybrid inheritance example in Python
class Base:
    def base_method(self):
        print("This is a method from the Base class.")
class Derived1(Base):
    def derived1_method(self):
        print("This is a method from Derived 1 class.")
class Derived2(Base):
    def derived2_method(self):
        print("This is a method from Derived 2 class.")
class Derived3(Derived1, Derived2):
    def derived3_method(self):
        print("This is a method from Derived 3 class.")
# Create an instance of Derived3
derived_instance = Derived3()
# Call methods from the base and derived classes
derived_instance.base_method()
derived_instance.derived1_method()
derived_instance.derived2_method()
derived_instance.derived3_method()
print("\n")  # Print a newline for better readability
print("----------------------------------------------------")

#inheritance using super() function
