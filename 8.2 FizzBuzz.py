fizzbuzz = int(input("Please enter your fizzbuzz challenge number here... "
                     "A number between 1 and 100 :"))
for engine in range(1, fizzbuzz + 1):
    if engine % 3 == 0 and engine % 5 == 0:
        print("fizzbuzz")
    elif engine % 3 == 0:
        print("fizz")
    elif engine % 5 == 0:
        print("buzz")
    elif fizzbuzz >= 101:
        print("must be below 101")
        break
    else:
        print(engine)
