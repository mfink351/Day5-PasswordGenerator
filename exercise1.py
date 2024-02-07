student_heights = input("Enter student heights: ").split(", ")
total_height = 0

for i in range(0, len(student_heights)):
  total_height += int(student_heights[i])

print(f"Average height is {total_height/len(student_heights)}")