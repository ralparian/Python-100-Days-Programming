
###Input list of user height spaces in between
student_heights = input("Enter list of height in CM: ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

#compute each heigh input.
total_height = 0
for height in student_heights:
  total_height += height
print(f"tota height = {total_height}")

#count the number of students base on the number of height input. Sample [156, 178, 165, 171, 187] number of student is 5
number_stud = 0
for student in student_heights:
  number_stud += 1
print(f"number of students = {number_stud}")

#computation of the average height total height / number of students
average_height = round(total_height / number_stud)
print(f"average heigh = {average_height}")


# mylist = []
# shopping = (input("Enter 5 items on shopping list: "))
# for i in range(5): # range starts from 0 and ends at 5-1 (so 0, 1, 2, 3, 4 executes your loop contents 5 times)
#     shopping = str(raw_input())
#     mylist.append(shopping) # add input to the list

# print (mylist) # at this point your list contains the 5 things entered by user

