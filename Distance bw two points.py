import math

def Distance(x1, x2, y1, y2):
    x = x2 - x1
    y = y2 - y1
    
    result = math.sqrt((x**2)+(y**2))
    return result

x1 = float(input("Enter the x-coordinate of the first point (x1) -> "))
y1 = float(input("Enter the y-coordinate of the first point (y1) -> "))

x2 = float(input("Enter the x-coordinate of the second point (x2) -> "))
y2 = float(input("Enter the y-coordinate of the second point (y2) -> "))

ans = Distance(x1, x2, y1, y2)

print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is -> {ans}")


