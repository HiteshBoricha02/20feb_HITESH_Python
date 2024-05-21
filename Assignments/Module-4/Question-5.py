

from collections import deque


def read_file(path, n):
    
        with open(path, 'r') as file:
            lines = deque(file, maxlen=n)

        for line in lines:
            print(line, end='')
    

path = 'example.txt'
n = int(input("Enter The line Number :"))


read_file(path, n)
