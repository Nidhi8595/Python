# Function to calculate the sum of the first n natural numbers
def series_sum(n):
    
    return n * (n + 1) / 2

n = int(input("Enter the number of terms(n) -> "))

result = series_sum(n)

print(f"The sum of the series 1 + 2 + ... + {n} is -> {result}")
