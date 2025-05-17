height = input("Enter heigh in meters e.g 1.65:" )
weight = input("Enter weight in kilograms e.g 72:")

BMI = int(weight) // (float(height) ** 2 )
#BMI_int = int(BMI)
if BMI < 18.5:
    print ("You are underweight!")
elif BMI >= 18.5 and BMI < 25:
    print (f"Your BMI  is {BMI} Status: Normal weight!")
elif BMI > 25 and BMI < 30:
    print (f"Your BMI is {BMI} Status: Overweight!")
elif BMI > 30 and BMI < 35:
    print(f"Your BMI is {BMI} Status: Obese!")
else:
    print(f"Your BMI is {BMI} Status: Clinically obese!")


#print (f"Your BMI is {BMI}" )
