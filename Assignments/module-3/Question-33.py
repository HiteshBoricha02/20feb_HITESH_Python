# Write a Python script to concatenate following dictionaries to create a new one.



Faculty = {1 : 'Shanket sir',
            2 : 'Meet sir',
            3 : 'Mitesh sir',
            4 : 'jaydip sir',
            5 : 'prakruti maam'}

COurse = {6 : 'Python',
           7 : 'C++',
           8 : 'Graphics',
           9 : 'Front End',
           10 : 'Java,flutter'}


Faculty.update(COurse)

print(Faculty)