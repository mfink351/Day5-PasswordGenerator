student_scores = input("Enter student's scores: ").split(", ")
highest_score = 0

for i in range(0, len(student_scores)):
  if int(student_scores[i]) > highest_score:
    highest_score = int(student_scores[i])

print(f"Highest score is {highest_score}")