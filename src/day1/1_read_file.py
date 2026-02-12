"""
Note:
    1. f.read() => Read content in the file repidly the save in String format
    2. f.readline() => Read each line then save in the list format (['line1\n', 'line2\n])  
"""


import os

# Normal form 
with open ('sample.txt', 'r') as f:
    content = f.read()
    print(content)
    # do what ever u want