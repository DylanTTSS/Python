cars = ['audi', 'bmw', 'subaru', 'toyota']

# for car in cars:  # 条件测试是核心
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# requested_topping = 'mushrooms'
#
# if requested_topping != 'anchovies':
#     print("Hold the anchovies")

# requested_topping = ['mushrooms', 'onions', 'pineapple']

# print('mushrooms' in requested_topping)
# print('pepperoni' in requested_topping)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

# if user not in banned_users:
#     print(f"{user.title()}, you can post a response if you wish")

age = 19
# if age >= 18:
#     print("You are old enough to vote!")
#     print("Have you registered to vote yet?")
# else:
#     print("Sorry you are too young to vote")
#     print("Please register to vote as soon as you turn 18!")

# if age < 4:
#     print("Your admission cost is $0.")
# elif age < 18:
#     print("Your admission cost is $25.")
# else:
#     print("Your admission cost is $40.")


# requested_toppings = ['mushrooms', 'onions', 'pineapple', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print(f"Adding {requested_topping}.")
#
# print("\nFinished making your pizza!")

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
