

# • What are negative indexes and why are they used?

str_1 = ''' in a list [1, 2, 3, 4, 5], if you use -1, it means the last item (5), -2 
            means the second-to-last item (4), and so on.'''
            
print(str_1)


ln = int(input("Enter The list of len :"))
list1 = []

for i in range(1,ln+1):
    num = input("Enter Name :")
    num = list1.append(num)
    


print("Your Entered List Is ",list1)
# print("Negative IDX Is ",list1[-5:-1])
w = list1[-1::-1]
print(w)
