conv_fac = 0.621371
# welcome message
print("Hi, Welcome to convertotron 2000! I will convert Kilometers in to miles.")

while True:
    # ask input kilometers
    print("Please enter the amount of Kilometers you want converted :")
# input kilometers
    kilometers = float(input(""))
    # conversion zone and print
    miles = kilometers * conv_fac
    print('%0.2f kilometers is equal to %0.3f miles' % (kilometers, miles))
    # asks for another conversion
    answer = input("would you like another conversion? Please enter y/n").lower()
    if answer == 'n' or answer != 'y':
        break
