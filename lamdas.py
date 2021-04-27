# def addition(num1, num2):
#     return num1+num2
#
# add= lambda num1 , num2 : num1+num2
#
# print(add(2,3))

savings=[234,555,674,78]
n=len(savings)
x=[]
for i in range(0,n):
    y=savings[i]*1.1
    x.append(y)


#print(x)

bonus =list(map(lambda x:x*1.1, savings))
print(bonus)

