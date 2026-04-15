# problem = calculate thr sum of even numbers upto to agiven number n.

n =int(input("Enter a number: "))
even_sum = 0
for i in range(1, n+1):
    if i % 2 == 0:
        even_sum += i
print("The sum of even numbers is:", even_sum)

