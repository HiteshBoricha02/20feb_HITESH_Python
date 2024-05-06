# Write a Python function that takes a list and returns a new list with unique
# elements of the first list.

def elements(input_list):
    return(set(input_list))

main_list = [1,2,3,2,1,4]
second_list = elements(main_list)

print("original List :",main_list)
print("Unique list :",second_list)