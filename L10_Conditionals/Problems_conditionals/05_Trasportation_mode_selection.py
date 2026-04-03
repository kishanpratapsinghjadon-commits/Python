# problem = choose a mode of transportation based on the distance (eg. <3km:walk , 3-15km: bike,>15km:car).
distance = int(input("Enter distance(value must be in km)"))
if distance <3:
    print("walking distance")
elif distance <=15 :
    print("bike se jao")
else:
    print("car lagegi")        