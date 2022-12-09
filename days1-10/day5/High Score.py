# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

#Write your code below this row 👇

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# fastest way
# print(sorted(student_scores))
# sorted_scores = sorted(student_scores)
# print(f"The highest score in the class is: {sorted_scores[-1]}")

# do the same in loop

highestScore = 0
for score in student_scores:
  if score > highestScore:
    highestScore = score

print(f"The highest score in the class is: {highestScore}")










