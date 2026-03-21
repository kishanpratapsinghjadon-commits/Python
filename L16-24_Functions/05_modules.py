# Two types of modules in python:
#   - built in modules
#   - External modules 
# List of all built in modules --- https://docs.python.org/3/py-modindex.html

import math # here math is a built in module.
import os # color isliye alag h kyuki tumne os import to karlia h per tum usse use nhi kar rahe ho.
import mymodule
import requests


print(math.sqrt(16)) # we using libraries here , 
mymodule.RAM()
r = requests.get("https://www.google.com") # we get html code for the link we have used.
print(r.text)