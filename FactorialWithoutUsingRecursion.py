def factorial(n):
    fact = 1
    if n < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif n == 0 or n == 1:
        print("The factorial is 1")
    else:
        for i in range( 2, n + 1):
            fact = fact*i
        return fact
    
num = int(input("Enter a number -> "))

ans = factorial(num)

print("The factorial of", num, "is -> ", ans)