# 6-8 pets
# pet1 = {'type': 'cat', 'master': 'dylan'}
# pet2 = {'type': 'dog', 'master': 'jane'}
# pet3 = {'type': 'fish', 'master': 'joe'}
#
# pets = [pet1, pet2, pet3]
# for pet in pets:
#     print(pet)


# 6-9 favorite_places
# favorite_places = {
#     'dylan': ['london', 'tokyo'],
#     'jack': ['paris', 'beijing'],
#     'job': ['shanghai'],
# }
#
# for name, places in favorite_places.items():
#     if len(places) == 1:
#         print(f"\n{name.title()}'s favorite place is ")
#         for place in places:
#             print(f"{place.title()}")
#
#     else:
#         print(f"\n{name.title()}'s favorite places are ")
#         for place in places:
#             print(f"{place.title()}")

# 6-11 cities
cities = {
    'beijing': {
        'country': 'china',
        'population': '21 million',
        'fact': 'the capital of china'
    },

    'tokyo': {
        'country': 'japan',
        'population': '14 million',
        'fact': 'the capital of japan'
    },

    'london': {
        'country': 'british',
        'population': '8 million',
        'fact': 'the capital of british'
    }
}


for city in cities.items():
    for city_info in city:
        print(city_info)

