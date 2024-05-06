# Write a Python script to sort (ascending and descending) a dictionary by
# value.

    
def sort_dict_ascending(d):
    return dict(sorted(d.items(), key=lambda item: item[1]))


def sort_dict_descending(d):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))


sample_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 3, 'mango': 1}


sorted_dict_ascending = sort_dict_ascending(sample_dict)
print("Dictionary sorted in ascending order:", sorted_dict_ascending)


sorted_dict_descending = sort_dict_descending(sample_dict)
print("Dictionary sorted in descending order:", sorted_dict_descending)
