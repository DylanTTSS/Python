# message = input("Tell me something, and I will repeat it back to you:")
# print(message)

# name = input("Please enter your name:")
# print(f"\nHello, {name.title()}!")
#
# prompt = "If you tell us who you are, we can personalize the message u see"
# prompt += "\nWhat is your first name:"
# name = input(prompt)
#
# # print(type(name))
#
# print(f"\nHello, {name.title()}!")

# while循环
# current_number = 1
# while current_number < 5:
#     print(current_number)
#     current_number += 1

# 让用户选择何时退出
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end thr program."
# message = ""
# active = True
#
# while active:
#     message = input(prompt)
#
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# 使用break语句推出循环
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished."
#
# while True:
#     city = input(prompt)
#
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go {city.title()}!")

# 在循环中使用continue
current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#
#     print(current_number)

# 使用while循环处理列表和字典
# 在列表之间移动元素
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
#
# while unconfirmed_users:
#     current_users = unconfirmed_users.pop()
#
#     print(f"Verifying user: {current_users.title()}")
#     confirmed_users.append(current_users)
#
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# 删除为特定值的所有列表元素
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
#
# while 'dog' in pets:
#     pets.remove('dog')
#
# print(pets)

# 使用用户输入来填充字典
responses = {}

polling_active = True
while polling_active:
    name = input("\nWhat's your name?")
    response = input("Which mountain would you like to climb someday?")

    responses[name] = response

    repeat = input("Would you like to let another person respond?(yes / no)")
    if repeat == 'no':
        polling_active = False

print("\n---Pll Results---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")

