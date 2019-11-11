# ch5_06_external_functions.py
#
print("외장 함수")
###########################################################
# 파이썬 사용자들이 만든 유용한 프로그램을 모아 놓은 것이
# 바로 파이썬 라이브러리
# 외장 모듈은 'import module_name' 형식으로 불러와서 사용
###########################################################
#

print("os")  # ***
###########################################################
# OS 모듈은 환경 변수나 디렉터리, 파일 등의 OS 자원을
# 제어할 수 있게 해주는 모듈
###########################################################
#
# 내 시스템의 환경 변수값을 알고 싶을 때 - os.environ
import os

os.environ

# 시스템의 PATH 환경 변수 내용
os.environ["PATH"]

# 현재 디렉터리 위치 확인 - os.getcwd()
os.getcwd()

# 시스템 명령어 호출하기 - os.system
os.system("dir")

# 디렉터리 위치 변경하기 - os.chdir('directory')
os.chdir("ch05")

# 기타 유용한 os 관련 함수
# os.mkdir(디렉터리)
# os.rmdir(디렉터리)
# os.rename(src, dst)


print("sys")  # ***
###########################################################
# sys 모듈은 파이썬 인터프리터가 제공하는 변수와 함수를
# 직접 제어할 수 있게 해주는 모듈
###########################################################
#
# argv_test.py
import sys

print(sys.argv)

# 강제로 스크립트 종료하기 - sys.exit
import sys

sys.exit()  # ^Z


import sys

sys.path

import os

os.getcwd()

import sys

sys.path.append("C:/doit/mymod")
# C:/doit/Mymod 디렉터리에 있는 파이썬 모듈을 불러와서 사용.


print("pickle")
###########################################################
# pickle은 객체의 형태를 그대로 유지하면서 파일에 저장하고
# 불러올 수 있게 하는 모듈
###########################################################
#
import pickle

# 객체 그대로 유지하면서 파일에 저장
f = open("test.txt", "wb")
data = {1: "python", 2: "you need"}
pickle.dump(data, f)
f.close()


# pickle.load를 사용해서 원래 있던 딕셔너리 객체(data) 상태 그대로 불러오기
f = open("test.txt", "rb")
data = pickle.load(f)
f.close()

print(data)
# pickle 모듈로 어떤 자료형이든 저장하고 불러올 수 있다.


print("shutil")
###########################################################
# shutil은 파일을 복사해 주는 파이썬 모듈
###########################################################
#
import shutil

os.system("dir")
shutil.copy("test.txt", "zest.txt")
os.system("dir")  # 확인


print("glob")
###########################################################
# 특정 디렉터리에 있는 파일 이름 모두 확인하는 파이썬 모듈
# 디렉터리에 있는 파일들을 리스트로 만들기 - glob(pathname)
###########################################################
#
import glob

glob.glob("*.txt")  # txt 파일 목록 확인
# ['test.txt', 'zest.txt']


print("tempfile")
###########################################################
# 파일을 임시로 만들어서 사용할 때 유용한 모듈
###########################################################
#
import tempfile

filename = tempfile.mktemp()
filename

# tempfile.TemporaryFile()은 임시 저장 공간으로 사용할 파일 객체를 돌려준다.
# 이 파일은 기본적으로 바이너리 쓰기 모드(wb)를 갖는다.
# f.close()가 호출되면 이 파일 객체는 자동으로 사라진다.
import tempfile

f = tempfile.TemporaryFile()
f.close()


print("time")  # ***
###########################################################
# 시간과 관련된 time 모듈
###########################################################
#
# time.time()
#
# time.time()은 UTC(Universal Time Coordinated 협정 세계 표준시)를
# 사용하여 현재 시간을 실수 형태로 돌려주는 함수이다.
# 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 돌려준다.
import time

time.time()

# time.localtime()
# time.localtime은 time.time()이 돌려준 실수 값을 사용해서
# 연도, 월, 일, 시, 분, 초, ... 의 형태로 바꾸어 주는 함수
time.localtime(time.time())
# time.struct_time(tm_year=2019, tm_mon=10, tm_mday=30,
# tm_hour=21, tm_min=18, tm_sec=15, tm_wday=2, tm_yday=303, tm_isdst=0)

# time.asctime
# 위 time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서
# 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수
time.asctime(time.localtime(time.time()))
# 'Wed Oct 30 21:19:52 2019'

# time.ctime
# time.asctime(time.localtime(time.time()))은 time.ctime()과 같다.
time.ctime()

# time.strftime
# time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))
# strftime 함수는 여러 가지 포맷 코드로 시간에 관계된 것을 세밀하게 표현

# 시간에 관계된 것을 표현하는 포맷 코드
##############################################################
# 포맷코드	설명	예
# %a	요일 줄임말	Mon
# %A	요일	Monday
# %b	달 줄임말	Jan
# %B	달	January
# %c	날짜와 시간을 출력함	06/01/01 17:22:21
# %d	날(day)	[01,31]
# %H	시간(hour)-24시간 출력 형태	[00,23]
# %I	시간(hour)-12시간 출력 형태	[01,12]
# %j	1년 중 누적 날짜	[001,366]
# %m	달	[01,12]
# %M	분	[01,59]
# %p	AM or PM	AM
# %S	초	[00,59]
# %U	1년 중 누적 주-일요일을 시작으로	[00,53]
# %w	숫자로 된 요일	[0(일요일),6]
# %W	1년 중 누적 주-월요일을 시작으로	[00,53]
# %x	현재 설정된 로케일에 기반한 날짜 출력	06/01/01
# %X	현재 설정된 로케일에 기반한 시간 출력	17:22:21
# %Y	년도 출력	2001
# %z	시간대 출력	대한민국 표준시
# %y	세기부분을 제외한 년도 출력	01
##############################################################

import time

time.strftime("%x", time.localtime(time.time()))

time.strftime("%c", time.localtime(time.time()))

time.strftime("%z", time.localtime(time.time()))


# time.sleep
# time.sleep 함수는 주로 루프 안에서 많이 사용한다.
# 이 함수를 사용하면 일정한 시간 간격을 두고 루프를 실행
# sleep1.py
import time

for i in range(10):
    print(i)
    time.sleep(1)  # delay = 1 s


print("calendar")
###########################################################
# 파이썬에서 달력을 볼 수 있게 해주는 모듈
###########################################################
#
import calendar

print(calendar.calendar(2019))

calendar.prcal(2019)

calendar.prmonth(2019, 11)

# calendar.weekday
# calendar 모듈의 또 다른 유용한 함수를 보자.
# weekday(연도, 월, 일) 함수는 그 날짜에 해당하는 요일 정보를 돌려준다.
# 월요일은 0, 화요일은 1, 수요일은 2, 목요일은 3, 금요일은 4,
# 토요일은 5, 일요일은 6이라는 값을 돌려준다.
calendar.weekday(2019, 12, 25)


# calendar.monthrange
# monthrange(연도, 월) 함수는 입력받은 달의 1일이 무슨 요일인지와
# 그 달이 며칠까지 있는지를 튜플 형태로 돌려준다.
calendar.monthrange(2019, 12)


print("random")  # ***
###########################################################
# 난수(규칙이 없는 임의의 수)를 발생시키는 모듈
# 마구잡이 수 발생
# random(), randint()
###########################################################
#
import random

# random() : 0.0에서 1.0 사이의 실수 중에서 난수 값을 생성
random.random()

# randint(start, end) : start에서 end 사이의 정수 중에서 난수 값을 생성
random.randint(1, 10)

for i in range(6):
    print(random.randint(1, 45), end=",")

print()

#####
# random 모듈을 사용해서 재미있는 함수
#
# random_pop.py
import random


def random_pop(data):
    number = random.randint(0, len(data) - 1)
    return data.pop(number)


if __name__ == "__main__":
    data = list(range(1, 10))  # [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data), end=" ")
    print()

# 리스트의 요소 중에서 무작위로 하나를 선택하여 꺼낸 다음 그 값을 돌려준다.
# 물론 꺼낸 요소는 pop 메서드에 의해 사라진다.


# random_pop 함수는 random 모듈의 choice 함수를 사용하여
# 다음과 같이 좀 더 직관적으로 만들 수도 있다.


def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number


random_pop([1, 2, 3, 4, 5])

if __name__ == "__main__":
    data = list(range(1, 10))  # [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data), end=" ")
    print()


#####################################################
# 다음의 의미
# if __name__ == "__main__":
# https://pinocc.tistory.com/175
#
# Filename: using_name.py
"""
if __name__ == '__main__':
	print 'This program is being run by itself'
else:
	print 'I am being imported from another module'
"""
# 직접 실행
# python using_name.py
# This program is being run by itself

# 모듈로 import 되어 실행
# >>> import using_name
# >>> I am being imported from another module
#####################################################


#
# 리스트의 항목을 무작위로 섞고 싶을 때는 random.shuffle 함수를 사용
#
import random

data = [1, 2, 3, 4, 5]
random.shuffle(data)
data


print("webbrowser")
###########################################################
# webbrowser는 자신의 시스템에서 사용하는 기본 웹 브라우저를
# 자동으로 실행하는 모듈
###########################################################
#
import webbrowser

webbrowser.open("http://google.com")
# 새로운 창/탭으로 열기
webbrowser.open_new("http://google.com")

## end of ch.05
# 스레드를 다루는 threading 모듈 (study!!)
#


"""
Author: redwoods
파이썬 코드: ch5_06_external_functions.py
"""
