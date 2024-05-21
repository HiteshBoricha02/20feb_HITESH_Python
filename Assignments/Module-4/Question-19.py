# How Do You Handle Exceptions With Try/Except/Finally In Python?
# Explain with coding snippets.

num = int(input('Enter an Value : '))

try:
    if (num%2 != 0):
         print('Number is odd Number')
    
    else:
        print('Number is even Number ')

except Exception as e:

    print(e)

finally:
    print("Thanks for check number....")
