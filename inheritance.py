"""Single level Inheritance
class Parent:
    def method1(self):
        print("I am Parent class")


class Child(Parent):
    def method2(self):
        print("I am Child class")


child1 = Child()
child1.method2()
child1.method1()


Multiple Inheritance
class Father:
    def method1(self):
        print("I am Father")


class Mother:
    def method2(self):
        print("I am Mother")


class Child(Father, Mother):
    def method3(self):
        print("I am Child")


child1 = Child()
child1.method3()
child1.method2()
child1.method1()
print(Child.__mro__)


Multilevel Inheritance
class GrandParent:
    def method1(self):
        print(" I am Grand Parent")


class Parent(GrandParent):
    def method2(self):
        print("I am Parent")


class Child(Parent):
    def method3(self):
        print("I am Child")


child1 = Child()
child1.method1()
child1.method2()
child1.method3()

print(Child.__mro__)


# Hierarchical Inheritance


class Parent:
    def method1(self):
        print("I am Parent")


class Child1(Parent):
    def method2(self):
        print("I am Child 1")


class Child2(Parent):
    def method3(self):
        print("I am Child 2")


child1 = Child1()
child2 = Child2()

child1.method2()
child1.method1()

child2.method3()
child2.method1()
"""

# Hybrid Inheritance


class GrandParent:
    def method1(self):
        print("I am Grand Parent")


class Parent1(GrandParent):
    def method2(self):
        print("I am Parent 1")


class Parent2:
    def method3(self):
        print("I am Parent 2")


class Child(Parent1, Parent2):
    def method4(self):
        print("I am Child")

child = Child()
child.method4()
child.method3()
child.method2()
child.method1()

