# Write a Python script to concatenate following dictionaries to create a new one.



frontEnd = {1 : 'HTML',
            2 : 'CSS',
            3 : 'JS',
            4 : 'BootStrap',
            5 : 'jQuery'}

backEnd = {6 : 'C',
           7 : 'C++',
           8 : 'MySQL',
           9 : 'Python',
           10 : 'Django'}


frontEnd.update(backEnd)

print(frontEnd)