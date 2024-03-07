

HTML = int(input("Enter MArks Of HTML :"))
CSS = int(input("Enter Marks of CSS :"))
JS = int(input("Enter Marks Of JS :"))
PY = int(input("Enter Marks of PY :"))

total = HTML+CSS+JS+PY
print("Total MArks Is :",total)

Percentage = (total/400)*100
print("Percentage Is :\t",Percentage)

if(HTML<=32 or CSS<=32 or JS<=32 or PY<=32 ):
    RESULT = "Fail"
    print("Your Result is :",RESULT)
    
elif(Percentage >= 90):
    Grade = "A"
    print( "Your Grade :",Grade)
    
elif(Percentage >= 80):
    Grade = "B"
    print("Your Grade is :",Grade)
elif(Percentage >= 70):
    Grade = "C"
    
elif(Percentage >=60):
    Grade = "D"
    print("Your Grade is :",Grade)
elif(Percentage >=50):
    Grade = "E"
    print("Your Grade is :",Grade)
else:
    Grade = "F"
    # print("Your Grade is :",Grade)
    
    
    print(" Grade is :",Grade)
    