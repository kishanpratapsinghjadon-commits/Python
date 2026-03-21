marks = [5, 2, 21, 5, 7]
extra_marks = [53, 23, 32]

print(marks)
marks.append(63) # this will change the original list and adds the value at the last.
marks.pop() #this removes the last element from the list
marks.extend(extra_marks) # it added all the elements of 2nd list to the end of first list
print(marks)
extra_marks.sort(reverse=True) # and this will arrange the elements in descending order.
print(extra_marks)
marks.sort() # this will arrange all the elements in the ascending order.
print(marks)