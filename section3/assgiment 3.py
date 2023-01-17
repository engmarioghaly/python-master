# Assignment 3:
"""
Create a function called multi_merge that takes a list and a string
as arguments.
The function is supposed to return a merged list
containing the original list argument as well as each of the words that are in
the string argument in addition to each of the characters in the string
argument as individual elements in the list.
"""
# Your Code Below:


def myltimerge (lisst,str):
    return lisst + str.split() + list(str)

print(myltimerge([1,2,3],"Hello My name is mario"))