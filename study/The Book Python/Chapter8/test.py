# 8.1 Functions
# def greet_user():
#     """显示简单的问候语"""
#     print("Hello")
#
#
# greet_user()

# 8.1.1 Pass information to the function
# def greet_user(username):
#     """显示简单的问候语"""
#     print(f"Hello, {username.title()}!")
#
#
# greet_user('jesse')
# greet_user('sarah')

# 8.1.2 Parameter and Argument
# greet_user('jesse') the jesse is the Argument
# def greet_user(username) the username is the Parameter

# 8.2 Passing arguments
# 8.2.1 Positional arguments
# def describe_pet(animal_type, pet_name):
#     """显示宠物信息"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
#
# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

# 8.2.2 Keyword arguments
# def describe_pet(animal_type, pet_name):
#     """显示宠物信息"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
#
# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='willie', animal_type='dog')

# 8.2.3 Default value
# def describe_pet(pet_name, animal_type='dog'):
#     """显示宠物信息"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
#
# describe_pet(pet_name='willie')
# describe_pet('willie')

# 8.3 return value
# def get_formatted_name(first_name, last_name):
#     """返回整洁的名字"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# def get_formatted_name(first_name, last_name, middle_name=''):
#     """返回整洁的名字"""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
#
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)


# def build_person(first_name, last_name, age=None):
#     """返回一个字典，其中包含有关一个人的信息"""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#
#
# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)


def get_formatted_name(first_name, last_name):
    """返回整洁的名字"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name")
    f_name = input("First Name:")
    l_name = input("Last Name:")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
