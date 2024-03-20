tuple=("Ice Cream","Taco","Burritos","MilkShake","Cake","Hamburger","Hotdogs")
array=["Jake","Sally","Rick","Morgan","Carol","Jason","Henri"]
for i in range(0,len(array)):
    array.insert(i,array.pop())

print(array)
