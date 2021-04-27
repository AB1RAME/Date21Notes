
# prime=int(input('Enter a range: '))
# p=[]
# for j in range(2,prime):
#     for i in range(2,prime):
#         if j!=i:
#             if j%i==0:
#                # print(f'{j} not a prime number')
#                 break
#         else:
#             #print(f'{j} is a prime number')
#             p.append(j)
#
# print(sum(p))

prime=int(input('Enter a number: '))
p=[]
for j in range(2,prime+1):
    for i in range(2,prime+1):
        if j!=i:
            if j%i==0:
                print(f'{j} not a prime number.')
                break
        else:
            p.append(j)
            print(f'{j} is a prime number.')

print(sum(p))


