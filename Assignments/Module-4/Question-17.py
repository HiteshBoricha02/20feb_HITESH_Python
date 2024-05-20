# When is the finally block executed?

def test():
    try:
        return "Returning from try block"
    finally:
        print("Finally block executed")

print(test())
