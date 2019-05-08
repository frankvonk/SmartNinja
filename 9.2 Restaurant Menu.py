# Homework assignment for SmartNinja by Frank Vonk.

print('Welcome to Steve\'s Gate to the Bits Of Flavour!')
menu = {'Bits of penne with graded Silicone': '6.95',
        'Soup with magnetic core spices': '4.50',
        'Wafer of chips, 4kb': '3.00',
        'wafer of chips, 8kb': '5.00',
        'RAM on the rocks': '9.50'}

while True:
    dish = input('Please enter a dish: ')
    price = int(input('What is the price of the dish? '))
    menu[dish] = price
    newEntry = input('Would you like to enter another item? y/n ')
    if newEntry == 'y':
        continue
    else:
        break

with open('sort.txt', 'w') as file:
    file.write("___ Today's Menu ___ \n")
    for k in sorted(menu.keys()):
        file.write("%s: %s \n" % (k, menu[k]))
