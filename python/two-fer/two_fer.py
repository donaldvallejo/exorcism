import sys

def two_fer(name='you'):
    return (f'One for {name}, one for me.')

# more ways to solve the problem

# 1
# def two_fer(name):
#     if not name:
#         return"One for you, one for me."
#     else:
#         return "One for " + name + ", one for me!"
# print(name)


# 2
# name = sys.argv[1]
# print(f"One for {name}, one for me!")

