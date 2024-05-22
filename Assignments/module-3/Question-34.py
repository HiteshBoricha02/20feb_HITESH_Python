# Write a Python script to check if a given key already exists in a dictionary.



course = {1: 'Front End', 2: 'Back End', 3: 'Web design', 4: 'Python', 5: 'java', 6: 'Flutter', 7: 'Android', 8: 'ios', 9: 'Graphics', 10: 'Digital Marketing'}


w = int(input("Enter Key and find The value : ")) 

if w in course.keys():
    
    print(f"{w} : {course[w]}")
    
else :
    print("Key Not Found You Have search")