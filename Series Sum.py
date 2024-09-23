
def Series_Sum(x, n):
    series = 1
    for i in range(1, n+1):
        series += x ** i

    return series

x = int(input("Enter the value of x -> "))
n = int(input("Enter a number (n) -> "))

ans = Series_Sum(x, n)

print("The sum of the series 1 + x + x^2 + ... + x^",n," is -> ",ans)
