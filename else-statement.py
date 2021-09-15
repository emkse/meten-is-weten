#else-statement


print("a en b zijn even groot") 

a = int(input("a =  "))

b = int(input("b =  "))

if a > b:
    Max = a
    Min = b
    print("a is het grootste getal: " + str(Max))
elif a < b:
    Max = b
    Min = a
    print("a is het kleinste getal: "+ str(Min))
else: a == b
print("a en b zijn even groot")
