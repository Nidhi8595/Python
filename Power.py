def power(base, exponent):
    return base ** exponent

base = int(input("Enter the base -> "))
exponent = int(input("Enter the exponent -> "))

ans = power(base, exponent)

print(f"{base} raised to the power of {exponent} is {ans}")
