# 7-4 the ingredients of pizza

prompt = "\nPlease add the ingredients u want to the pizza:"

while True:
    ingredients = input(prompt)

    if ingredients == 'quit':
        print("Thanks for your order")
        break
    else:
        print(f"We'll add {ingredients.title()} to the pizza")

# 7-5 movie tickets
# prompt = "\nPlease enter the age:"
#
# while True:
#     age = int(input(prompt))
#
#     if (age >= 3) and (age < 12):
#         print("The ticket costs 10$")
#     elif age >= 12:
#         print("The ticket costs 15$")

