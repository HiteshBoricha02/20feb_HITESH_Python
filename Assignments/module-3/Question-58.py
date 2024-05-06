#  Write a Python program to read a random line from a file.

import random

def get_random_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_lines = len(lines)
        random_index = random.randint(0, num_lines - 1)
        return lines[random_index]

filename = r'C:\Full Stack\Back End\Python sanket Sir\data.txt'  # Replace 'your_file.txt' with the name of your file
random_line = get_random_line(filename)
print(f"Random line from the file : {random_line}")