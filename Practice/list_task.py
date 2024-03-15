

id = []
Name = []

stud = int(input("Enter A number of elements :"))

for idx in range(stud):
    num = int(input("Enter Your id :"))
    id.append(num)
    
    
    for N in range(1):
        fn = input("Enter Name :")
    Name.append(fn)
    
    

print(id)
print(Name)

for ind_no in range(stud):
    print(f"student{ind_no+1}:{Name[ind_no]}")

