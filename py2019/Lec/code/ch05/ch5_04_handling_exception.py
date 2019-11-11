# ch5_04_handling_exception.py
#
print("예외 처리")
#######################################
# 빈번히 발생하는 오류를 처리
# try, except, finally 를 사용
#######################################
#

print("오류는 어떤 때 발생하는가?")
#######################################
# 오류가 발생하는 사례
#######################################
#
# 1. 디렉터리 안에 없는 파일을 열려고 시도했을 때
# 
f = open("나없는파일", 'r')   # FileNotFoundError:

# 2. 0으로 다른 숫자를 나누는 경우 (division by zero)
4 / 0   # ZeroDivisionError:

# 범위를 벗어 난 인덱싱 (list index out of range)
a = [1,2,3]

a[3]  # IndexError:


print("오류 예외 처리 기법")
#######################################
# 유연한 프로그래밍을 위한 오류 처리 기법
#######################################
#
# 1. try, except문
#
# try, except문의 기본 구조
'''
try:
    ...
except [발생 오류[as 오류 메시지 변수]]:
    ...
'''
# try 블록 수행 중 오류가 발생하면 except 블록이 수행된다. 
# 하지만 try 블록에서 오류가 발생하지 않는다면 
# except 블록은 수행되지 않는다.

# ZeroDivisionError:
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)


# division by zero


# IndexError:
a = [1, 2, 3]
try:
    a[3]
except IndexError as e:
    print(e)


# list index out of range


#
# 2. try, finally문
#
# try문에는 finally절을 사용할 수 있다. 
# finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행
#

try:
    f = open('goo.txt', 'w')
    # 무언가를 수행한다.
finally:
    f.close()


#
# 3. 여러개의 오류처리하기
#
# try문 안에서 여러 개의 오류를 처리하는 방법
#
'''
try:
    ...
except 발생 오류1:
   ... 
except 발생 오류2:
   ...
'''

try:
    a = [1,2]
    print(a[2])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")


# 인덱싱 오류가 먼저 발생했으므로 
# 4/0으로 발생되는 ZeroDivisionError 오류는 발생하지 않았다.

try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)


# 2개 이상의 오류를 동시에 처리
try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)


print("오류 회피하기")
#######################################
# 특정 오류가 발생할 경우 그냥 통과시키는 방법.
#######################################
#
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass



print("오류 일부러 발생시키기")
#######################################
# 일부러 발생시키는 오류
# raise 오류 
#######################################
#
# Bird 클래스를 상속받는 자식 클래스는 반드시 
# fly라는 함수를 구현하도록 만들고 싶은 경우
#
class Bird:
    def fly(self):
        raise NotImplementedError


# Bird 클래스를 상속받는 자식 클래스는 
# 반드시 fly 함수를 구현해야 한다

class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()

# NotImplementedError가 발생되지 않게 하려면 
# 다음과 같이 Eagle 클래스에 fly 함수를 반드시 구현
class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()


print("예외 만들기: 사용자 정의 예외")
#######################################
# 사용자가 정의해서 만들고 발생시키는 오류
# 파이썬 내장 클래스인 Exception 클래스를 상속하여 만든다.
# raise User_Error() 
#######################################
#
class MyError(Exception):
    pass


def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)


#######################################
print("사용자 정의 예외 처리")
#######################################
try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")


#######################################
print("사용자 정의 예외 메시지 출력")
# 오류 메시지: __str__ 메서드를 구현
#######################################
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."


# 
try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)


"""
Author: redwoods
파이썬 코드: ch5_04_handling_exception.py
"""
