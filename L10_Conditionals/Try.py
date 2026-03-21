age = int(input("Enter your age: "))

if(age>1 and age<18):
    print("You cannot drive")
elif(age == 18):
    print("Let's schedule an interview")
elif(age == 0):
    print("NA MANEE!!!")
else:
    print("You can drive")