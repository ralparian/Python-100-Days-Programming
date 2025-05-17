print ("The love calculator is calculating your score...")
count = 0
name1 = input("Your name: ")
upper_names = name1.upper()

for char in name1:
    if char == 't':  
        count += 1
    elif char == 'r':
        count += 1
    elif char == 'u':
        count += 1
    elif char == 'e':
        count += 1
name2 = input("Crush name:")
upper_names1 = name2.upper()
for char in name2:
    if char == 't':  
        count += 1
    elif char == 'r':
        count += 1
    elif char == 'u':
        count += 1
    elif char == 'e':
        count += 1
#print(count)

count1 = 0
for char in name1:
    if char == 'l':  
        count1 += 1
    elif char == 'o':
        count1 += 1
    elif char == 'v':
        count1 += 1
    elif char == 'e':
        count1 += 1
for char in name2:
    if char == 'l':  
        count1 += 1
    elif char == 'o':
        count1 += 1
    elif char == 'v':
        count1 += 1
    elif char == 'e':
        count1 += 1
#print (count1)
   
love_score = str(count) + str(count1)
#print (love_score)

if  int(love_score) < 10 and int(love_score) > 90:
 print (f"Love score is {love_score} you go to together live coke and mentos.")
elif int(love_score) >= 40 and int(love_score) >= 50:
    print( f"You love score is {love_score} you are alright together" )
else:
    print( f"You love score is {love_score}")
    