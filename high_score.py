student_scores = input("Enter student scores list: ").split()
for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])

max_score = student_scores[0]
for number in student_scores:
    if number > max_score:
        max_score = number
print(max_score)

