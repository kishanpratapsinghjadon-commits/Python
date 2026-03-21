a = int(input("Enter a number between 1 and 10: "))

match a:
    case 1:
        print("You won a charger")
    case 3:
        print("You won $3 ")
    case 6:
        print("You won a camera")
    case _:                      # it is like a else statement.
        print("Better Luck Next Time")
    
    