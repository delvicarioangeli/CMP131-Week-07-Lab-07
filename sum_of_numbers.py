#Angelina Del Vicario
#10/14/26
#CMP131
#Lab 07
#Sum Of Numbers

user = int(input("Enter a positive integer: "))

total = 0

current = 1

while current <= user:
    total = total + current
    current = current + 1

print("The total sum is: ", total)