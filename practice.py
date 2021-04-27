def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

y=[]
x = int(input('Enter the value:'))
for i in range(x):
    a=(fibonacci(i + 2))
    print(a)
    if fibonacci(i + 2)%2==0:
        y.append(fibonacci(i + 2))
    if fibonacci(i + 2)>4000001:
        break

print(sum(y))
