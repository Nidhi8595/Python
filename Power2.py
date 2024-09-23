# using pow() method 

def power(base, exponent):
    return pow(base,exponent)

base = float(input("Enter the base -> "))
exponent = float(input("Enter the exponent -> "))

ans = power(base, exponent)

print("The result of ",base," raised to the power of ",exponent," is -> ", ans)