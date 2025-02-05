itr = iter([1, 2, 3, 4, 5])

print(itr)

for i in itr:
    print(i)

itr = iter([1, 2, 3, 4, 5])
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
