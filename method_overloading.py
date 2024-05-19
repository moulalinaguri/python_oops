"""class MethodOverLoading:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


obj1 = MethodOverLoading()

obj1.add(1, 2, 3)
obj1.add(1, 2)

/Users/moulali/Documents/Data_Engineering_2024/PySpark_Projects/python_oops/venv/bin/python /Users/moulali/Documents/Data_Engineering_2024/PySpark_Projects/python_oops/method_overloading.py
Traceback (most recent call last):
  File "/Users/moulali/Documents/Data_Engineering_2024/PySpark_Projects/python_oops/method_overloading.py", line 12, in <module>
    obj1.add(1, 2)
TypeError: MethodOverLoading.add() missing 1 required positional argument: 'c'

Process finished with exit code 1
"""

import multipledispatch


class MethodOverLoading:
    @multipledispatch.dispatch(int, int)
    def add(self, a, b):
        return a + b

    @multipledispatch.dispatch(int, int, int)
    def add(self, a, b, c):
        return a + b + c

    @multipledispatch.dispatch(str, str)
    def add(self, a, b):
        return a+b


obj1 = MethodOverLoading()
print(obj1.add(1, 2, 3))
print(obj1.add(1, 2))
print(obj1.add("Moulali ", "Naguri"))
