print("Thank you for choosng Python Pizza Deliveries!")
bill = 0
size = input("What size of pizza do you want? (S, M, or L)")
add_peperoni = input("Do you want to add peperoni? (Y or N)")
extra_cheese = input ("Do you want to add extra cheese? (Y or N)")

if size == "S" and add_peperoni == "Y":
    bill += 17
elif size == "S" and add_peperoni == "N":
    bill += 15

if size == "M" and  add_peperoni == "Y":
    bill += 23
elif size == "M" and add_peperoni == "N":
    bill +=20       
   
if  size == "L" and add_peperoni == "Y":
    bill += 28
elif size == "L" and add_peperoni == "N":
    bill += 25
   
if extra_cheese == "Y":
    bill += 1

print(f"You bill is ${bill}")