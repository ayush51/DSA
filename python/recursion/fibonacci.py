
def fibonacci(n):
    if n <= 1: 
        return n
    else:
        last = fibonacci(n-1)
        slast = fibonacci(n-2)
        return (last + slast)

n = 5
for i in range(n):
    print(fibonacci(i))
