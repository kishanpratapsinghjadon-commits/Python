# String formatting

template = "Dear {}, You are awesome. Take this {}$ bag"
a = "kishan"
a1 = 100000
b = "ishan"
b1 = 1000
c = "MAMTA"
c2 = 300

s1 = template.format(b, a1)  # this is the old method or u can say its the method 1
print(s1)

print(f"{b} you are awesome and take this {a1}$ bag") # this is the new method or you can say method 2


print(ord('A')) # character encoding
print(chr(65)) # ASCII value american standard code for information interchange.