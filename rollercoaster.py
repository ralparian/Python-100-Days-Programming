bill = 0
height = int(input(" What is your height? (cm)"))
age = int(input(" How old are you?: "))


if height < 120:
    print ("You are not allowed to rider!")
elif height > 120 and age < 12:
    bill =+ 5
    print (f"You can ride the rollcoaster! Price is {bill}")
elif height > 120 and age <= 12:
    bill =+ 7
    print (f"You can ride the rollcoaster! Price is {bill}")
elif height > 120 and age <= 18:
    bill =+ 12
    print (f"You can ride the rollcoaster! Price is {bill}")
elif height > 120 and age >= 45 and age <= 55:
    bill =+ 0
    print (f"You can ride the rollcoaster and everything is gonna be alright. Price is {bill}")
else:
    bill += 12
    print (f"You can ride the rollcoaster! Price is {bill}")

add_photo = input("Do you want add for photo? (Y or N): ")
if add_photo == "Y":
    bill += 3
print (f"You total bill is {bill}.")