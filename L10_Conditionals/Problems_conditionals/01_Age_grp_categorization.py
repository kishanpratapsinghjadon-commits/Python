# classify a person's age group :child(<13), teenager(13-19), adult(20-59), senior(60+)
 
age = float(input("Enter your Age: "))
if age < 13:
    print("You are a child.")
elif age in range(13,20):
    print("You are a teenager.")
elif age in range(20,60):
    print("You are an adult.")
else:    print("You are a senior.") 
