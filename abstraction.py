from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def method1(self):
        pass

    @staticmethod
    def method2():
        print("This is Concrete method")

    @abstractmethod
    def method3(self):
        pass

    @abstractmethod
    def method4(self):
        pass


class Subclass(AbstractClass):
    def method1(self):
        print("method1 is implemented in sub class")

    def method3(self):
        print("method3 is implemented in sub class")


obj1 = Subclass()
obj1.method1()
obj1.method2()
obj1.method3()




