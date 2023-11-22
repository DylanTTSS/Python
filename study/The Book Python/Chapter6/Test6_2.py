# 6-5 河流
rivers = {'nile': 'egypt', 'yangtze river': 'china', 'amazon river': 'brazil'}

# 使用循环打印每条河流的信息
# for key, value in rivers.items():
#     print(f"The {key.title()} runs through {value.title()}")

# for river in rivers.keys():
#     print(river.title())
#
# for country in rivers.values():
#     print(country.title())

# 6-6 调查
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

invested_persons = ['jen', 'edward', 'dylan']

for invested_person in invested_persons:
    # for favorite_language in favorite_languages:
    #     if invested_person in favorite_language:
    #         print(f"{invested_person.title()}, thank you for your participation!")
    #     else:
    #         print(f"{invested_person.title()}, We want to invite you to join us!")
    #         break

    if invested_person in favorite_languages.keys():
        print(f"{invested_person.title()}, thank you for your participation!")
    else:
        print(f"{invested_person.title()}, We want to invite you to join us!")
        break







