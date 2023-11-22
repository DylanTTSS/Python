# 4-10 切片
my_destinations = ["DaLi", "Tokyo", "NewYork", "London"]

print("The first three items in the list are:")

# for destination in my_destinations[:3]:
#     print(destination)

# for destination in my_destinations[1:3]:
#     print(destination)

# for destination in my_destinations[1:]:
#     print(destination)

# 4-11 不同的旅游地点
friend_destination = my_destinations[:]

my_destinations.append('ShangHai')
friend_destination.append('FuZhou')

print("My destinations are:")
for destination in my_destinations:
    print(destination)

print("\nMy friend's destinations are:")
for destination in friend_destination:
    print(destination)
