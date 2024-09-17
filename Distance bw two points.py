import math

def Distance(x1, x2, y1, y2):
    x = x2 - x1
    y = y2 - y1
    
    ans = math.sqrt((x**2)+(y**2))
    return ans

x1 = int(input("Enter the value of x1 -> "))
x2 = int(input("Enter the value of x2 -> "))

y1 = int(input("Enter the value of y1 -> "))
y2 = int(input("Enter the value of y2 -> "))

ans = Distance(x1, x2, y1, y2)

print("Distance -> ",ans)


