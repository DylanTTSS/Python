# 4-3 数到20
# for number in range(1, 21):
#     print(number)

# 4-4 一百万
numbers = []
for number in range(1, 1000000):
    numbers.append(number)

# for number in numbers:
#     print(number)

# 4-5 一百万求和

# print(min(numbers))
# print(max(numbers))
# print(sum(numbers))

# 4-6 奇数
odds = list(range(1, 20, 2))
for odd in odds:
    print(odd)

# 4-7 3的倍数
# divides = []
# for divide in range(3, 31):
#     if divide % 3 == 0:
#         divides.append(divide)

divides = [divide for divide in range(3, 31) if divide % 3 == 0]

for divide in divides:
    print(divide)

# 4-8 立方
cubes = list(value ** 3 for value in range(1, 11))

for cube in cubes:
    print(cube)

