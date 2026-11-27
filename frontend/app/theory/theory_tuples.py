some_list = [1, 2, 3, 4, 5]

# first = some_list[0]
# second = some_list[1]
# third = some_list[2]
#
# print(first)

first, second, third, *rest = some_list

print(rest)
print(*rest)
print(4, 5)
