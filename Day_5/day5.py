"""
boolean: True, False
comparision operators: >, <, >=, <=, ==, != => Bool
truthy values: bool(value) = True
if-elif-else
"""

# age = int(input('> '))
#
# if age > 18:
#     print("duoc uong bia")
# elif age > 10:
#     print("uong coca")
# else:
#     print("uong nuoc loc")

name = input("Please enter your name: ")

if name:  # Checks the truth value of name by calling bool
      print(f"You entered {name}")
else:
      print("You didn't type anything")

