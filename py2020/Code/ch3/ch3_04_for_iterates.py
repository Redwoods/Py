# ch3_04_for_iterates.py
#
############################
print("for 문과 itrator")
############################
subjects = ['python', 'english', 'math', 'science']
scores = [88, 77, 66, 95]
#
print("과목명 출력")
for subject in subjects:
    print(subject)


#
print("과목 점수 출력")
for score in scores:
    print(score)


#
print("enumerate()를 이용한 출력")
for position, subject in enumerate(subjects):
    print(position,subject)


#
for position, subject in enumerate(subjects):
    print(subjects[position])


#
print("enumerate()를 이용하여 점수를 출력해보시오.")
#
#


#
############################
print("for 문과 itrator의 응용: 복합 문자열 리스트")
############################
subjects = ['python', 'english', 'math', 'science']
scores = [88, 77, 66, 95]
# Method-1
for position in range(len(subjects)):
    subject = subjects[position]
    score = scores[position]
    print(subject, score)


# Method-2
for position, subject in enumerate(subjects):
    score = scores[position]
    print(subject, score)



# Method-3
for subject, score in zip(subjects, scores):
    print(subject, score)


# 응용 코드 : 평균 성적을 구하시오.
subjects = ['python', 'english', 'math', 'science']
scores = [88, 77, 66, 95]

average = 0
total = 0
for subject, score in zip(subjects, scores):
    total += score
    print(subject, score)

print("평균 점수 = {0}".format(total/len(subjects)))

# Cool! 

"""
Author: redwoods
파이썬 코드: ch3_04_for_iterates.py
"""
