#Angelina Del Vicario
#10/14/26
#CMP131
#Lab 07
#Shipping Charges


print("Welcome to the Fast Freight Shipping Company")

weight = float(input('Please enter the Weight of the Package(In Kilograms):'))
while (weight < 0 or weight >20):
    print ("your weight is invalid please try again") 
    weight = float(input('Please enter the Weight of the Package(In Kilograms):'))

distance = int(input("Please enter the distance the package has to go(in miles):"))
while (distance <10 or distance >3000):
    print("Error: Distance invalid please try again")
    distance = int(input("Please enter the distance the package has to go(in miles):"))

if weight <=2:
    rate = 1.10
elif weight <=6:
    rate = 2.20
elif weight <= 10:
    rate = 3.70
else:
    rate = 4.80
shippingCharge = rate * (distance / 500)

print("______Shipping_Reciept_______")
print("____Package Weight:  "  , weight , "kg")
print("____Shipping Distance: " , distance , "miles")
print("____Shipping Rate:  " , rate)
print("________Total Charges:  $" , shippingCharge)