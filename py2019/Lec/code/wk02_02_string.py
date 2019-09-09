# wk02_02_string.py
# "Life is too short, you need python"
# 'Life is too short, you need python'
# """Life is too short, you need python"""
# '''Life is too short, you need python'''


print("문자열: '")
food = "Python's favorite food is perl"
food

food = 'Python's favorite food is perl'  # Error

say = '"Python is very easy." he says.'

print("문자열: \ 이용")
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."

# 이스케이프 코드
print("문자열: 이스케이프 코드 이용")
multiline = "Life is too short\nYou need python"
multiline
print(multiline)
# 여러줄 문자열 처리
multiline = '''
... Life is too short
... You need python
... '''
multiline
print(multiline)
################################################
print("문자열 연산: 더하기")
head = "Python"
tail = " is fun!"
head + tail

print("문자열 연산: 곱하기")
a = "python"
a * 2

#####################################
# multistring.py
print("=" * 50)
print("I am now coding Python!")
print("=" * 50)
#####################################

# 내장함수: len()
print("문자열 연산: 길이 구하기 - len()")
a = "Life is too short"
len(a)


"""
Author: redwoods
파이썬 코드: wk02_02_string.py
"""
