while True:
    try:
        a = float(input("Enter a number: "))
        b = float(input("Enter another number: "))

        result = a / b
        print(f"Result: {result}")

    except ZeroDivisionError as e:
        print(f"Error: {e}")
        print("Please enter a non-zero denominator.")
