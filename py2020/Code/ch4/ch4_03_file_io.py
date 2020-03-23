# ch4_03_file_io.py
#
print("파일 읽고 쓰기")
#######################################
# 파일을 통한 입출력 방법에 대해 알아보자.
#######################################

print("파일 쓰기(생성하기)")
#
# 파일 객체 = open(파일 이름, 파일 열기 모드)
#
# 파일열기모드
# r	읽기모드 - 파일을 읽기만 할 때 사용
# w	쓰기모드 - 파일에 내용을 쓸 때 사용
# a	추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용
#

f = open("새파일.txt", "w")
f.close()
# 파일이 어디에 만들어졌는 지 확인하시오!!!

# 다른 폴더에 파일 생성
"""
f = open("C:/doit/새파일.txt", 'w')
f.close()
"""


print("파일을 쓰기 모드로 열어 출력값 적기")
#######################################
# 프로그램의 출력값을 파일에 직접 써 보자.
#######################################
# 모니터에 출력
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    print(data)


# 파일에 기록(출력)
# writedata.py
f = open("./새파일.txt", "w")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)


f.close()

# 출력 파일의 한글이 깨지면
# 파일 > 기본설정 > 설정 > Files: Auto Guess Encoding 을 지정(check)
#

###################################################
print("파일 읽기")
#
# 파일 객체 = open(파일 이름, 파일 열기 모드)
#
# 파일읽기
# readline() 함수 이용하기
# readlines 함수 사용하기
# read 함수 사용하기
#
# 1. readline() 함수
# readline_test.py
f = open("새파일.txt", "r")
line = f.readline()
print(line)
f.close()

# readline_all.py
f = open("새파일.txt", "r")
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

# 사용자 입력을 이용한 화면 출력
while 1:
    data = input()
    if not data:
        break
    print(data)


# 2. readlines() 함수
f = open("새파일.txt", "r")
lines = f.readlines()
for line in lines:
    print(line)  # , end="")
f.close()

# 3. readl() 함수
f = open("새파일.txt", "r")
data = f.read()
print(data)
f.close()

###################################################
print("파일에 새로운 내용 추가하기")
#
# 파일에 원래 있던 값을 유지하면서 단지 새로운 값만 추가
# 파일을 추가 모드('a')로 열고 쓴다.
#
# adddata.py
f = open("새파일.txt", "a")
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# 수정된 파일 확인
f = open("새파일.txt", "r")
data = f.read()
print(data)
f.close()

###################################################
print("with문과 함께 사용하기")
#
# with문을 사용하면 with 블록을 벗어나는 순간
# 열린 파일 객체 f가 자동으로 close 된다.
#
f = open("foo.txt", "w")
f.write("Life is too short, you need python")
f.close()

with open("foo1.txt", "w") as f:
    f.write("Life is too short, you need python")

###################################################
print("sys 모듈로 매개변수 주기")
#
"""
#sys1.py
import sys

args = sys.argv[1:]
for i in args:
    print(i)
"""

######
"""
#sys2.py
import sys
args = sys.argv[1:]
for i in args:
    print(i.upper(), end=' ')
"""


"""
Author: redwoods
파이썬 코드: ch4_03_file_io.py
"""
