# Movie tickets are priced based on age: $12 for adults (18 and over ), $8 for children . Everyone gets $2 discount on wednnesday.

print("Welcome to the Movie Theater!")
age = int(input("Please enter your age: "))
day = input("Please enter the day of the week:")

if day.lower() == "wednesday":
    if age >= 18:
        print("Your ticket price is $10.")
    else:
        print("Your ticket price is $6.")
else:
    if age >= 18:
        print("Your ticket price is $12.")
    else:
        print("Your ticket price is $8.")