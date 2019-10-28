# ch4_01_function.py
#
print("함수란 무엇인가?")
#######################################
# 입력값을 가지고 어떤 일을 수행한 다음에 
# 그 결과물을 내어놓는 것
#######################################

print("함수를 사용하는 이유는 무엇일까?")
#######################################
# 반복되는 부분을 함수로 전환.
# 코딩을 모듈화
#######################################


print("파이썬 함수의 구조")
#######################################
"""
def 함수명(매개변수):
    <수행할 문장1>
    <수행할 문장2>
    ...
"""
#######################################
# add() 함수를 정의
def add(a, b): 
    return a + b


# add() 함수를 사용
a=3
b=4
c=add(a,b)
print(c)

x=[1,2,3]
y=[4,5,6]
z=x+y
print(z)
#

print("매개변수와 인수릐 차이를 이해하자!")
#######################################
# 매개변수는 함수에 입력으로 전달된 값을 받는 변수
# 인수는 함수를 호출할 때 전달하는 입력값을 의미
#######################################
# add() 함수에서의 매개변수와 인수
"""
def add(a, b):  # a, b는 매개변수
    return a+b

print(add(3, 4))  # 3, 4는 인수

"""

print("입력값과 결괏값에 따른 함수의 형태")
#######################################
# 입력값 ---> 함수 ----> 결괏값
#######################################
# 일반적인 함수
# 입력값과 결괏값이 있는 함수
"""
def 함수이름(매개변수):
    <수행할 문장>
    ...
    return 결과값
"""

def add2(a, b): 
    result = a + b 
    return result


# 입력값과 결괏값이 있는 함수의 사용법
# 결괏값을 받을 변수 = 함수이름(입력인수1, 입력인수2, ...)
a = add2(3, 4)
print(a)

#######################################
# 입력값이 없는 함수

def say(): 
    return 'Hi'


# 입력값이 없는 함수의 사용법
# 결괏값을 받을 변수 = 함수이름()
a = say()
print(a)


#######################################
# 결괏값이 없는 함수

def add3(a, b): 
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))


# 결괏값이 없는 함수의 사용법
# 함수이름(입력인수1, 입력인수2, ...)
add3(3, 4)

# 다음 결과는 무엇인가?
a = add3(3, 4)
print(a)
# 

#######################################
# 입력값도 결괏값도 없는 함수

def say2(): 
    print('Hi')


# 입력값도 결괏값도 없는 함수의 사용법
# 함수이름()
say()

#######################################
print("매개변수의 값을 지정하여 호출하기")
#######################################
def add4(a, b):
    return a+b


result = add4(a=3, b=7)  # a에 3, b에 7을 전달
print(result)
# 매개변수의 순서에 상관없이 사용
result = add4(b=5, a=3)  # b에 5, a에 3을 전달
print(result)
#######################################

#######################################
print("입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?")
#######################################
"""
def 함수이름(*매개변수): 
    <수행할 문장>
    ...
"""

def add_many(*args):
    result = 0 
    for i in args: 
        result = result + i 
    return result 


add_many(1, 2, 3)
add_many(1, 2, 3, 4, 5, 6, 7, 8, 9)

result = add_many(1,2,3,4,5,6,7,8,9,10)
print(result)


#######################################
print("여러 개의 입력을 처리하는 함수(*args)")
#######################################

def add_mul(choice, *args):
    if choice == "add":
        result = 0 
        for i in args:
            result = result + i 
    elif choice == "mul":
        result = 1 
        for i in args: 
            result = result * i 
    return result 

# add
result = add_mul('add', 1,2,3,4,5)
print(result)
# multiply
result = add_mul('mul', 1,2,3,4,5)
print(result)

#
#######################################
print("키워드 파라미터 kwargs")
#######################################

def print_kwargs(**kwargs):
    print(kwargs)


# print_kwargs 함수는 매개변수 kwargs를 출력하는 함수
#
print_kwargs(a=1)

print_kwargs(name='foo', age=3)

#
# **kwargs처럼 매개변수 이름 앞에 **을 붙이면 매개변수 
# kwargs는 딕셔너리가 되고 모든 key=value 형태의 결괏값이 
# 그 딕셔너리에 저장된다.
#

#######################################
print("함수의 결괏값은 언제나 하나")
#######################################
#
def add_and_mul(a,b): 
    return a+b, a*b


# add_and_mul() 사용 1.
result = add_and_mul(3,4)

print(result)

# add_and_mul() 사용 2.
result1, result2 = add_and_mul(3, 4)

result1, result2

#######################################
print("잘못된 함수")
#######################################
def add_and_mul2(a,b): 
    return a+b 
    return a*b  # Not working!!


result = add_and_mul2(2, 3)
print(result)

#######################################
print("return 의 용도: 함수 실행 종료")
#######################################
def say_nick(nick): 
    if nick == "바보": 
        return 
    print("나의 별명은 %s 입니다." % nick)


say_nick("홍길동")
say_nick("바보")

#----------------------------------------
#######################################
print("매개변수에 초깃값 미리 설정하기")
#######################################
def say_myself(name, old, man=True): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % old) 
    if man: 
        print("남자입니다.")
    else: 
        print("여자입니다.")
    

say_myself("박응용", 27)
say_myself("박응용", 27, True)

say_myself("박응용", 27, False)

"""
def say_myself2(name, man=True, old): 
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % old) 
    if man: 
        print("남자입니다.") 
    else:
        print("여자입니다.")
    


"""
# 초깃값을 설정해 놓은 매개변수 뒤에 
# 초깃값을 설정해 놓지 않은 매개변수는 사용할 수 없다
# 초기화시키고 싶은 매개변수를 항상 뒤쪽에 놓는다.


#######################################
print("함수 안에서 선언한 변수의 효력 범위")
# 전역변수
# 지역 변수, 자동 변수
#######################################

# vartest.py
a = 1
def vartest(a):
    a = a +1

vartest(a)
print(a)

# vartest_error.py
def vartest2(z):
    z = z + 1

vartest2(3)
print(z)  # Error


#######################################
print("함수 안에서 함수 밖의 변수를 변경하는 방법")
# return 사용
# global 변수 사용
#######################################
# 1. return 사용하기
a = 1 
def vartest3(a): 
    a = a +1 
    return a

a = vartest3(a) 
print(a)

# 2. global 명령어 사용하기
a = 1 
def vartest4(): 
    global a 
    a = a+1

vartest4() 
print(a)


#--------   lambda  -------------------
#######################################
print("lambda")
#######################################
# lambda는 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다. 
# 보통 함수를 한줄로 간결하게 만들 때 사용한다.
#
# lambda 사용법
#
# lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식
#
print("lambda를 이용한 add 함수")

add = lambda a, b: a+b

result = add(3, 4)
print(result)

# lambda 예약어로 만든 함수는 return 명령어가 없어도 결괏값을 돌려준다.

################################
# lambda 함수의 응용
#
models = ['K-3000', 'N-1000', 'T-2000', 'X-5000']
sorted(models, key=lambda x: x[-4:])

# So cool!!!

"""
Author: redwoods
파이썬 코드: ch4_01_function.py
"""
