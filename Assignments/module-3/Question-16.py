
# Write a Python program to check whether a list contains a sub list

def common_elements(main_list, sublist):
    common = [item for item in sublist if item in main_list]
    return common


main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sub_list = [4, 5, 6]

common_elements_list = common_elements(main_list, sub_list)

if common_elements_list:
    print("Common elements between the main list and the sub list:", common_elements_list)
else:
    print("There are no common elements.")
    
    