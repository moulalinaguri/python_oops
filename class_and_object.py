class SampleClass:
    attribute1 = 10
    attribute2 = 20


# print(SampleClass.attribute1)
# print(SampleClass.attribute2)

# obj1 = SampleClass()
# print(obj1.attribute1)
# print(obj1.attribute2)

obj1 = SampleClass()
obj2 = SampleClass()
obj3 = SampleClass()

print(obj1.attribute1)
print(obj1.attribute2)
print(obj2.attribute1)
print(obj2.attribute2)
print(obj3.attribute1)
print(obj3.attribute2)

SampleClass.attribute1 = 100

print(obj1.attribute1)
print(obj1.attribute2)
print(obj2.attribute1)
print(obj2.attribute2)
print(obj3.attribute1)
print(obj3.attribute2)

obj1.attribute1 = 500

print(obj1.attribute1)
print(obj1.attribute2)
print(obj2.attribute1)
print(obj2.attribute2)
print(obj3.attribute1)
print(obj3.attribute2)

