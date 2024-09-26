student_scores= [150,149,120,183,125,99,199]
#summation
print(sum(student_scores))
#or
sum=0
for i in student_scores:
    sum +=i
print(sum)

#maximum in the list
print(max(student_scores))
#or
max_score=0
for i in student_scores:
    if i>max_score:
        max_score=i
        
print(max_score)