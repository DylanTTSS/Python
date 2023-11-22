# 5-8 以特殊的方式跟管理员打招呼  5-9 处理没有用户的情况

# users_names = ['admin', 'dylan', 'taylor', 'ed', 'job']
# if users_names:
#     for users_name in users_names:
#         if users_name == 'admin':
#             print(f"\nHello {users_name}, would you like to see a status report\n")
#         else:
#             print(f"Hello {users_name.title()}, thank you for logging in again")
# else:
#     print("We need to find some users!")

# 5-10 检查用户名
# current_users = ['admin', 'dylan', 'taylor', 'ed', 'job']
# new_users = ['dylan', 'taylor', 'mc', 'tin','ad']
# current_users_lower = current_users[:]
#
# for new_user in new_users:
#     if new_user in current_users:
#         print(f"Sorry, {new_user} is not available")
#     else:
#         print(f"{new_user} a useful name")

# 5-11 序数
numbers = range(1, 10)

# for number in numbers:
#     print(number)

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")
