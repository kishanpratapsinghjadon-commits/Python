age = int(input("Enter your age: "))

if(age>18):
    print("You can drive")  #python interpretor will check from 1st if statement and will answer accordingly, like in Try.py we can see if we give input 0 than according to condition 1 we gets the result.
elif(age == 18):
    print("Let's schedule an interview")
elif(age == 0):
    print("NA MANEE!!!")
else:
    print("Sorry Ladle")