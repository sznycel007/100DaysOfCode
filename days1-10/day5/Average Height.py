# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# 180 124 165 173 189 169 146

# print(dir(student_heights))

# print(len(student_heights))
# print(sum(student_heights))
print(round(sum(student_heights)/len(student_heights)))

total = 0
for i in student_heights:
  total += i

number_of_students = 0
for student in student_heights:
  number_of_students +=1

print(round(total/number_of_students))
