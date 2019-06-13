import csv

Menu = '''\nPlease select one option from the following:
    1) Add New Product
    2) Update product quantity
    3) Update Cost Price
    4) Update Selling Price
    5) Show Info about one product
    6) Show all Stock
    7) Save and Exit'''


def outflow(name, oqty):
    products[name][0] -= oqty
    if products[name][0] < 0:
        print('Error !!')
        print('\nThis product quantity is now Negative!!!')
        print('The new', name, ' quantity is: ', products[name][0])
    else:
        print("The new product (", name, ") quantity in stock is", products[name][0])


def inflow(name, iqty):
    products[name][0] += iqty
    print('The current ', name, ' quantity in stock is', products[name][0])


def updateCP(name, newCP):
    products[name][1] = newCP


def updateSP(name, newSP):
    products[name][2] = newSP


def CheckInfo(name):
    print('The product name is: ', name)
    print('/nThe product Cost Price is: ', products[name][1])
    print('/nThe Product Selling price is: ', products[name][2])
    print('/nThe Product Quantity in stock is: ', products[name][0])


products = {}

with open("stock.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, skipinitialspace=True)

    for line in csv_reader:
        print(line)
        products[line[0]] = line[1]
    print(products)

while True:
    print(Menu)
    option = input('Your choice: ')
    if option == '1':
        Name = input('\nEnter product Name:')
        if Name in products.keys():
            print('\n\nError, This product already exists.\n\n')
            continue
        Quantity = int(input('Enter Product Quantity: '))
        CP = float(input('Enter Product Cost Price: '))
        SP = float(input('Enter Product Selling Price: '))
        details = [Quantity, CP, SP]
        products[Name] = details
        with open("stock.csv", "a+") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([Name, details])
    elif option == '2':
        pname = input('Enter Product Name: ')
        if pname in products.keys():
            print('Current product Quantity is: ', products[pname][0])
            check2 = input('\nIs the product being (A)dded or (R)emoved? ')
            if check2 == 'A' or check2 == 'a':
                qty = int(input('Enter Quantity Brought in: '))
                inflow(pname, qty)
                print('Product quantity updated successfully')
            elif check2 == "R" or check2 == 'r':
                qty = int(input('Enter Quantity sent out: '))
                outflow(pname, qty)
                print('Product quantity updated successfully')
            else:
                print('Error !!')
                print('Please enter correct response. a/A for added, o/O for outgoing')
        else:
            print('Error !!!')
            print('Please check the product name. Such product doesn\'t exist in the given stock')
    elif option == '3':
        pname = input('Enter Product Name: ')
        if pname in products.keys():
            newprice = float(input('Please enter New CP: '))
            updateCP(pname, newprice)
            print('Product Cost Price Updated.')
        else:
            print('Error !!')
            print('No such product exists in the current stock. Please check the product name again.\n\n')
    elif option == '4':
        pname = input('Enter Product Name: ')
        if pname in products.keys():
            newprice = float(input('Please enter New SP: '))
            updateSP(pname, newprice)
            print('Product Selling Price Updated.')
        else:
            print('Error !!')
            print('No such product exists in the current stock. Please check the product name again.')
    elif option == '5':
        pname = input('Enter Product Name: ')
        if pname in products.keys():
            CheckInfo(pname)
        else:
            print('\nError!!')
            print('Product name does not exist.\n')
    elif option == '6':
        print(products)
        for key in products:
            length = len(key)
            print('Name:', key, ' ' * (10 - length), ' Quantity:', products[key][0], ' CP:', products[key][1], ' SP: ',
                  products[key][2])
    elif option == '7':
        with open("stock.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file)
            for key in products:
                csv_writer.writerow([key, products[key]])
        print('You have chosen to save and exit.')
        print('Have a nice day.')
        print('Saving.......')
        break
    else:
        print('\nPlease enter the correct option number.')
