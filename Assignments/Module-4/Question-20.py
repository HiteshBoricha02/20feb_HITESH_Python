# • Write python program that user to enter only odd numbers, else will
# raise an exception.


def number():
    while True:
        try:
            number = int(input("Please enter an odd number: "))
            if number % 2 == 0:
                print("That is not an odd number.")
            print(f"{number} is an odd number.")
            break
        except Exception as e:
            print(e)


number()
