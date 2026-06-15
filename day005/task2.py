student_scores = [85, 92, 78, 90, 88]

for score in student_scores:
    if score >= 90:
        print(f"Score: {score} - Grade: A")
    elif score >= 80:
        print(f"Score: {score} - Grade: B")
    elif score >= 70:
        print(f"Score: {score} - Grade: C")
    elif score >= 60:
        print(f"Score: {score} - Grade: D")
    else:
        print(f"Score: {score} - Grade: F")
        
exam_scores = [95, 82, 67, 74, 88]
total_score = sum(exam_scores)
average_score = total_score / len(exam_scores)
print(f"Total Score: {total_score}, Average Score: {average_score:.2f}")

max=max(exam_scores)
max_for = 0
for score in exam_scores:
    if score > max_for:
        max_for = score
print(f"Maximum Score: {max}")
print(f"Maximum Score: {max_for}")
