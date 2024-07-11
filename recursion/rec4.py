def power(n):
    if n == 0:
        return 1
    else:
        pow = power(n - 1)
        result = pow * 2
        print(f"2^{n} = {result}")  # Print the result of 2^n
        return result

power(3)
