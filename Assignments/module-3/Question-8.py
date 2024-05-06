# Write a Python program to check a list is empty or not

def is_list_empty(input_list):
    if not input_list:
        return True
    else:
        return False

my_list = []

if is_list_empty(my_list):
    print("The list is empty.")
else:
    print("The list is not empty.")


