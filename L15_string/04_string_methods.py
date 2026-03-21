# s = "pushpendra singh rajput" # Strings are immutable

# # s[0] = "R" #you cannot to this , keep in mind

# a = len(s)
# print(a)
# # print(s.upper(), s) # s.upper is a new string, s is still immutable 
# print(s.upper())
# print(s.lower())
# print(s.capitalize()) # capitalize() converts the first character of a string to uppercase.
# print(s.title()) 




# text = " \nhello world "
# print(text.strip())
# print(text.lstrip())  #strip() removes leading and trailing whitespaces from a string -- whitespaces is a blank spaces, tabs, or newlines in text.
# print(text.rstrip())
# print(text)




# text = "Python is fun and fun and fun" #first is alwsys starts with zero
# print(text.find("is")) # Output: 7 Index of first occurence
# print(text.replace("fun", "awesome")) # it will change all the fun into awesome not only the first occuring fun.




# text = "Apples,Bananas,pineapple"
# print(text.split(","))
# print(",".join(['Apples', 'Bananas', 'pineapple']))



text = "pyhton123" # these commands will only true and false as a output.
print(text.isalpha()) # is all the chracter present in text are alphabet
print(text.isdigit()) # is all the chracter present in text are digit
print(text.isalnum()) # is all the charcetr present in text are only alphabet or number or both 
print(text.isspace()) #is all the characters are whitespaces or not



