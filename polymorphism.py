def total(*args):
    if args:
        sum = type(args[0])()
        for i in args:
            sum += i
        return sum


print(total(1))
print(total(1, 2))
print(total(1, 2, 3))
print(total('a', 'b', 'c'))
print(total('a', 'b'))
print(total(1.0, 2.0))
print(total([1, 2], [3, 4]))
print(total(1, 2, 3, 4.0, 5.67))