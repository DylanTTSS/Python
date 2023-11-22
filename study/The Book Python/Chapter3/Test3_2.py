# 3-4 嘉宾名单
guests = ["XiaoMing", "XiaoHong", "XiaoLi"]
#
# name = guests[0].title()
# print(f"{name}, please come to dinner")
#
# name = guests[1].title()
# print(f"{name}, please come to dinner")
#
# name = guests[2].title()
# print(f"{name}, please come to dinner")

# 3-5 修改嘉宾名单
print("XiaoMing can't come to the dinner")
guests.remove("XiaoMing")
guests.append("XiaoWang")

# name = guests[0].title()
# print(f"{name}, please come to dinner")
#
# name = guests[1].title()
# print(f"{name}, please come to dinner")
#
# name = guests[2].title()
# print(f"{name}, please come to dinner")

# 3-6 添加嘉宾
# print("I find a bigger table")
#
guests.insert(0, "XiaoXu")
guests.insert(3, "XiaoHu")
guests.append("XiaoXiao")
#
# for i in range(len(guests)):
#     print(guests[i], "please come to dinner")

# 3-7 缩减名单
print("Only two guests can be invited")
# 注意每次删除后对原列表排序的影响
guests.pop(1)
guests.pop(1)
guests.pop(1)
guests.pop(1)

# name = guests[0].title()
# print(f"{name}, please come to dinner")
#
# name = guests[1].title()
# print(f"{name}, please come to dinner")

# 注意每次删除后对原列表排序的影响
del guests[0]
del guests[0]

print(guests)