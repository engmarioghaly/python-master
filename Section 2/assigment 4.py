# Assignment 4:
"""
In the list shown below, replace the letter m with the letter x
and replace the word TV with the word television. Then print my_list.
"""

my_list = [(1, 2), (3, 4), (['c', 'd', 'a', 'm'], [3, 9, 4, 12], 4), 'TV', 42]


# Your Code Below:
my_list[2][0][3] = 'm'
my_list[3]='Televsion'
print(my_list)