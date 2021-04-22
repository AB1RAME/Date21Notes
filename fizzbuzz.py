# num=[1,2,3,4,5,6,7,8,9,10]
#
# for i in num:
#     if i%3==0:
#         print('Fizz')
#     elif i%5==0:
#         print('Buzz')
#     else:
#         print(i)

# n=int(input('enter a range:'))
def fizzbuzz(n):
    result=[]
    for x in range(1,n+1):
     if x%3==0 and x%5==0:
      result.append('Fizzbuzz')
     elif x%3==0:
      result.append('Fizz')
     elif x%5==0:
      result.append('Buzz')
     else:
      result.append(x)
    return result

print(fizzbuzz(10))

#try and get them to display one after the other