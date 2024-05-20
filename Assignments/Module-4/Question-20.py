# • Write python program that user to enter only odd numbers, else will
# raise an exception.


def get_number():
    while True:
        try:
            number = int(input("Please enter an odd number: "))
            if number % 2 == 0:
                raise ValueError("That is not an odd number.")
            print(f"Thank you! {number} is an odd number.")
            break
        except ValueError as e:
            print(e)


get_number()
