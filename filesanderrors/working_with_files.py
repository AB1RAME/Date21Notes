def open_and_print_file(file='order.txt'):
    try:
        with open(file,'r')as opened_file:
            for line in opened_file.readlines():
                print(line.rstrip('\n'))

    except FileNotFoundError as errmsg:
        print('There has been an error opening  your file')
        print(errmsg)
    finally:
        print('Excecution complete')
#open_and_print_file('order.txt')
order_list=['a','b','c','d']
def write_to_file(order_item,file='order.txt'):
    try:
         with open (file,'a')as opened_file:
             for item in  order_list:
                 opened_file.write(item+ '\n')

    except FileNotFoundError:
        print("File can't be found")
write_to_file('Nothing')


open_and_print_file()