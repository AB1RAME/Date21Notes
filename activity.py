
name_check=True
while name_check:
    name=input('Please enter your name: ')
    if name.isalpha():
        name_check=False
    else:
        print('Please use alphabets')
price=[6.00,7.95,5.00]
age_prompt=True
while age_prompt:
    age=input('What is you age? ')
    if age.isdigit():
        age_prompt=False
        print('you have entered the correct age')
        if int(age)>64:
            print(name +" you belong in the senior category,and the price of your ticket is " +str(price[0]))
        elif int(age)>14:
            print(name +" you belong in the general category,,and the price of your ticket is " +str(price[1]))
        else :
            print(name +" you belong in the child category,,and the price of your ticket is " +str(price[2]))
    else:
        print('please provide your age as a digit.')




