
def Func(x, n):
    series = 1
    for i in range(1, n+1):
        series += x ** i

    return series


n = int(input("Enter a number -> "))
x = int(input("Enter the value of x -> "))

ans = Func(x, n)

print("The Sum of series is -> ",ans)
