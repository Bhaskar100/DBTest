import os

try:
    print(dir(os))
except IOError as e:
    print(e)

#Modes
"""
r+= read and write
w+ = write and read 
a+= append and read 

"""