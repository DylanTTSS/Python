# alien_0 = {'color': 'green', 'points': '5'}
# print(alien_0)

# print(alien_0['color'])
# print(alien_0['points'])

# 访问字典中的值
# new_points = alien_0['points']
# print(f"You just earned {new_points} points")

# 添加键值对
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
#
# print(alien_0)

# 创建空键值对、修改字典中的值
# alien_0 = {}
#
# alien_0['color'] = 'green'
# alien_0['points'] = '5'
#
# print(f"The alien is {alien_0['color']}")
#
# alien_0['color'] = 'yellow'
# print(f"The alien is {alien_0['color']}")

# aline_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
# print(f"Original x_position: {aline_0['x_position']}")
#
# if aline_0['speed'] == 'slow':
#     x_increment = 1
# elif aline_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
#
# aline_0['x_position'] = aline_0['x_position'] + x_increment
# print(f"New x_position: {aline_0['x_position']}")

# 删除键值对
# alien_0 = {'color': 'green', 'points': '5'}
# print(alien_0)
#
# del alien_0['points']
# print(alien_0)

# 由类似对象组成的语言
# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }
#
# language = favorite_language['sarah'].title()
# print(f"Sarah's favorite language is {language}")

# 使用get()来访问值
# alien_0 = {'color': 'green', 'points': '5'}
# speed_value = alien_0.get('speed', 'No speed value assigned')
# print(speed_value)

# 遍历字典
# 遍历所有键值对
# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }
#
# for key, value in user_0.items():
#     print(f"\nKey:{key}")
#     print(f"Value:{value}")

# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

# for name, language in favorite_language.items():
#     print(f"{name.title()}'s favorite language is {language.title()}")

# for name in favorite_language.keys():
#     print(name.title())

# friends = ['phil', 'sarah']
# for name in favorite_language.keys():
#     print(f"Hi {name.title()}")
#
#     if name in friends:
#         language = favorite_language[name].title()
#         print(f"\t{name.title()}, I see you love {language}")

# if 'eric' not in favorite_language:
#     print("Eric, please take our poll")

# 按特定顺序遍历字典中所有键
# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }

# 利用sorted()函数进行排序
# for name in sorted(favorite_language.keys()):
#     print(f"{name.title()}, thank you for taking the poll")

# 遍历字典中所有的值
# print("The following languages have been mentioned:")

# 遍历所有的值，包括重复的值
# for language in favorite_language.values():
#     print(language.title())

# 使用sorted()遍历所有的值，不包含重复的值
# for language in set(favorite_language.values()):
#     print(language.title())

# 嵌套
# 列表嵌套字典
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
#
# aliens = [alien_0, alien_1, alien_2]
#
# for alien in aliens:
#     print(alien)

aliens = []

# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
#
# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['points'] = 10
#         alien['speed'] = 'slow'
#
# for alien in aliens[:5]:
#     print(alien)
# print("...")
#
# print(f"Total number of aliens: {len(aliens)}")

# 字典内嵌套列表
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print(f"You ordered a {pizza['crust']} - crust pizza"
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

favorite_language = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_language.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is:")
        for language in languages:
            print(f"\t{language.title()}")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")

# 字典中存储字典
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'maire',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = user_info['first'] + user_info['last']
    location = user_info['location']

    print(f"Full name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
