print ("The love calculator is calculating your score...")
count = 0
name1 = input("Your name: ")
name2 = input("Crush name:")
combined_name = name1 + name2
lower_names = combined_name.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

love_score =int(str(first_digit) + str(second_digit))

if  love_score < 10 or love_score > 90:
 print (f"Love score is {love_score} you go to together live coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print( f"You love score is {love_score} you are alright together" )
else:
    print( f"You love score is {love_score}")
    