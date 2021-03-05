# ch5_02_module.py
#
print("모듈이란 무엇인가?")
#######################################
# 모듈이란 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일
#######################################

print("모듈 만들기")
#######################################
# 간단한 모듈을 한번 만들어 보자.
#######################################
# 

# mod1.py를 현재 폴더에 저장
'''
# mod1.py
def add(a, b):
    return a + b

def sub(a, b): 
    return a-b
'''

# 파이썬 확장자 .py로 만든 파이썬 파일은 모두 모듈이다.

print("모듈 불러오기")
#######################################
# import 모듈명
# import는 이미 만들어 놓은 파이썬 모듈을 사용할 수 있게 해주는 명령어
#######################################
# 
# 현재 폴더에 있는 모듈, mod1.py를 연결하기.
#
import mod1
print(mod1.add(3, 4))

print(mod1.sub(7, 2))

#######################################
# 모듈 내부 함수 이용
# from 모듈이름 import 모듈함수
#######################################
#
from mod1 import add
add(3, 4)

# from 모듈이름 import *
# from mod1 import add, sub
from mod1 import *

add(3, 4)
sub(7, 3)


print("if __name__ == "__main__": 의 의미")
#######################################
# import 모듈명
# import는 이미 만들어 놓은 파이썬 모듈을 
# 사용할 수 있게 해주는 명령어
#######################################
# 

# mod1.py 파일을 다음과 같이 변경해 보자.
'''
# mod1.py 
def add(a, b): 
    return a+b

def sub(a, b): 
    return a-b

print(add(1, 4))
print(sub(4, 2))
'''

###################################
# cmd에서 실행하시오.
# python mod1.py
###################################
'''
python mod1.py
5
2
'''

import mod1
# 5
# 2
print(__name__)

'''
# mod2.py 
def add(a, b): 
    return a+b

def sub(a, b): 
    return a-b

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))
'''

import mod2
print(__name__)
# if __name__ == "__main__"을 사용하면 C:\doit>python mod1.py처럼 
# 직접 이 파일을 실행했을 때는 __name__ == "__main__"이 참이 되어 
# if문 다음 문장이 수행된다. 
# 반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 때는 
# __name__ == "__main__"이 거짓이 되어 if문 다음 문장이 수행되지 않는다.
#


print("클래스나 변수 등을 포함한 모듈")
#######################################
# 클래스나 변수 등을 포함하는 모듈
#######################################
# 
'''
# mod3.py 
PI = 3.141592

class Math: 
    def solv(self, r): 
        return PI * (r ** 2) 

def add(a, b): 
    return a+b 
'''

import mod3

print(mod3.PI)

a = mod3.Math()
print(a.solv(2))

print(mod3.add(mod3.PI, 4.4))

print("다른 파일에서 모듈 불러오기")
#######################################
# 다른 파이썬 파일에서 이전에 만들어 놓은 
# 모듈을 불러와서 사용하는 방법
#######################################
# 
'''
# modtest.py
import mod2
result = mod2.add(3, 4)
print(result)
'''
###################################
# cmd에서 실행하시오.
# python modtest.py
###################################
# 참고: 현재 폴더로 경로 설정 (path)
# import sys
# sys.path.append("current_path")
# sys.path

"""
Author: redwoods
파이썬 코드: ch5_02_module.py
"""
