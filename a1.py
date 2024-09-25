# Here, the user will input each of their grades
lab = int(input("Enter the number of labs completed:"))
if lab > 6:
    lab = 6
quiz = int(input("Enter the number of quizzes completed:"))
if quiz > 6:
    quiz = 6
assi1 = float(input("Enter grade for Assignment 1:"))
assi2 = float(input("Enter grade for Assignment 2:"))
assi3 = float(input("Enter grade for Assignment 3:"))
assi4 = float(input("Enter grade for Assignment 4:"))

mid1 = float(input("Enter grade for Midterm 1:"))
mid2 = float(input("Enter grade for Midterm 2:"))

final = float(input("Enter grade for Final Exam:"))

mid_fin_prep = float(input("Enter grade for Midterms and Final Preparation:"))


# Here, the weight of each evaluation will be calculated
w_lab = (lab / 6 * 100) * 0.2
w_quiz = (quiz / 6 * 100) * 0.15
w_assi = (assi1 + assi2 + assi3 + assi4) / 4 * 0.16
w_mid = (mid1 + mid2) / 2 * 0.25
w_final = final * 0.18
w_prep = mid_fin_prep * 0.06


# Here, the overall grade will be calculated
overall_grade = w_lab + w_quiz + w_assi + w_mid + w_final + w_prep
int_overall_grade = int(overall_grade) # The final grade has to be an integer, not a float
print(f"Your grade is: {int_overall_grade}")

