import re
import os

pattern = r'\[.*?\]\(.*?\)'
fname="name_of_file.txt"
while fname=="" or fname=="name_of_file.txt":
    fname=input("enter file name")
    if fname:
        pass
    elif fname=="":
        print("enter valid file name,")

    else:
        print("enter valid file name")

with open(fname, 'r') as file:
    for line in file:
        if re.search(pattern, line):
            print(line.strip())
