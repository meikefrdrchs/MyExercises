def numberconversion():

    number = input("Type a number!\n")

    if number.isdigit() is True:
        newnumber = int(number)
        print("Cool, your number is",newnumber)
    else:
        print("Sorry, that sucks.")

numberconversion()
