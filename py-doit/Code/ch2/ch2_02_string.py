# ch2_02_string.py
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

#####################################
#
# 문자열 인덱싱과 슬라이싱
#
#####################################
print("문자열: 인덱싱이란?")
a = "Life is too short, You need Python"
a[3]
a[15]

# "파이썬은 0부터 숫자를 센다."
print("문자열: 인덱싱 활용")

a = "Life is too short, You need Python"
a[0]

a[12]

a[-1]

# a[-0]
a[-2]
a[-5]
a[-12]

#####################################
print("문자열: 슬라이싱이란?")
a = "Life is too short, You need Python"
# Life 를 뽑아낼려면 어떻게?
b = a[0] + a[1] + a[2] + a[3]  # 문자열 뎌하기 연산
b
# slicing (슬라이싱)
a[0:4]  # 0 <= index < 4

a[0:5]
a[5:7]
a[12:17]
# : 의 사용
a[:4]
a[19:]
a[:17]

a[:]

# a[19:-7] ?
a[19:-7]

print("문자열: 슬라이싱 응용?")
a = "20190909Sunny"
date = a[:8]
weather = a[8:]
date
weather

a = "20190917Rainy"
year = a[:4]
day = a[4:8]
weather = a[8:]
year,day,weather

# "Pithon"이라는 문자열을 "Python"으로 바꾸려면?
a = "Pithon"
a[1]
a[1] = 'y'  # Error (immutable한 자료형)
#################
a = "Pithon"
a[:1]
a[2:]
a[:1] + 'y' + a[2:]  # Python

"""
Author: redwoods
파이썬 코드: ch2_02_string.py
"""
