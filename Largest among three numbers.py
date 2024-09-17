# Function to find the largest of three numbers

def largest(n1, n2, n3):
    
    if n1 >= n2 and n1 >= n3:
        l = n1
        
    elif n2 >= n1 and n2 >= n3:
        l = n2
        
    else:
        l = n3
    
    return l

n1 = int(input("Enter the first number -> "))
n2 = int(input("Enter the second number -> "))
n3 = int(input("Enter the third number -> "))

ans = largest(n1, n2, n3)

print(f"The largest number among  {n1}, {n2} and {n3} is {ans}")
