# using ** operator 

def power(base, exponent):
    return base ** exponent

base = float(input("Enter the base -> "))
exponent = float(input("Enter the exponent -> "))

ans = power(base, exponent)

print("The result of ",base," raised to the power of ",exponent," is -> ", ans)
