num=10
add=[]

while num>0:
    if num%3==0 or num%5==0:
        add.append(num)


output=sum(add)
print(output)


