# ch5_01_class.py
#
print("클래스란 무엇인가?")
#######################################
# 클래스(class)
#######################################

print("클래스는 왜 필요한가?")
#######################################
# 지정된 기능을 수행하는 변수와 함수의 모음
# 인스턴스, 즉 객체를 생성하여 기능을 이용
# 코딩을 객체화
#######################################
# 
# [예] 이전에 계산한 결괏값을 기억하고 있는 계산기
# 
result = 0

def add(num):
    global result
    result += num
    return result


# 이전에 계산한 결괏값을 기억
print(add(3))
print(add(4))

# 2대의 계산기가 필요한 상황이 발생하면?
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1


def add2(num):
    global result2
    result2 += num
    return result2



print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

# 계산기 1의 결괏값이 계산기 2에 아무 영향을 끼치지 않음을 확인할 수 있다. 
# 하지만 계산기가 3개, 5개, 10개로 점점 더 많이 필요해진다면 어떻게 해야 할까? 
# 그때마다 전역 변수와 함수를 추가할 것인가? 

#######################################
print("클래스를 사용하면 간단하게 해결")
#######################################
# class Calculator
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
    
    # def sub(self, num):
    #     self.result -= num
    #     return self.result



cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

# 
# 뺄셈(sub)을 추가하고 클래스의 객체를 다시 만들어서 사용한다.
# 

print("클래스와 객체")
#######################################
# 클래스(class)란 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계 도면
# 객체(object)란 클래스로 만든 피조물(과자 틀을 사용해 만든 과자)
#
# 클래스(class) : 과자 틀 
# 객체(object) : 과자 틀을 사용해 만든 과자
#
# 동일한 클래스로 만든 객체들은 서로 전혀 영향을 주지 않는다.
#######################################

# 간단한 클래스와 객체 
class Cookie:
    pass

a = Cookie()
b = Cookie()
id(a), id(b)

# 객체와 인스턴스의 차이
#  a = Cookie() 이렇게 만든 a는 객체이다. 
# 그리고 a 객체는 Cookie의 인스턴스이다. 
# 즉 인스턴스라는 말은 특정 객체(a)가 
# 어떤 클래스(Cookie)의 객체인지를 
# 관계 위주로 설명할 때 사용한다

print("사칙연산 클래스 만들기")
#######################################
# 사칙연산을 가능하게 하는 FourCal 클래스
# class FourCal
#
# Usage:
# a = FourCal()
# a.setdata(4, 2)
# a.add(), a.sub(), a.mul(), a.div()
#
#######################################
print("1. FourCal 클래스 구조 만들기")

class FourCal:
    pass


# 객체 만들기
a = FourCal()
type(a), id(a)

#######################################
print("2. 객체에 숫자 지정할 수 있게 만들기")
# function setdata()  # method

class FourCal:
   def setdata(self, first, second):
       self.first = first
       self.second = second



a = FourCal()
a.setdata(4, 2)

# 객체 변수
a.first    # self.first
a.second   # self.second


# 객체를 이용하기
a = FourCal()
b = FourCal()

a is b

type(a), id(a)
type(b), id(b)

a.setdata(4, 2)
print(a.first)
b.setdata(3, 7)
print(b.first)

print(a.first)  # what value?
# a 객체의 first 값은 b 객체의 first 값에 영향받지 않고 원래 값을 유지
# 클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지

id(a.first), id(b.first)

#######################################
print("3. 더하기 기능 만들기")
# function add()  # method

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    

a = FourCal()
a.setdata(4, 2)
a.add()

#######################################
print("4. 곱하기, 빼기, 나누기 기능 추가")
# function sub(), mul(), div()

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
        
    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result
    

  
a = FourCal()
b = FourCal()

a.setdata(4, 2)
b.setdata(3, 8)

a.add(), a.sub(), a.mul(), a.div()
b.add(), b.sub(), b.mul(), b.div()

#######################################
print("생성자 (Constructor)")
#######################################
#
# __init__()
#

a = FourCal()
a.add()   #  AttributeError

#######################################
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second
        
    def add(self):
        result = self.first + self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result
    

#######################################

a = FourCal()   # TypeError:

a = FourCal(4, 2)
a.first, a.second

a.mul()


#######################################
print("클래스의 상속")
# 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 
# 기존 기능을 변경하려고 할 때 사용
#######################################
# 
# class 클래스 이름(상속할 클래스 이름)
# 
# 클래스 FourCal를 상속하는 
# class MoreFourCal
# FourCal 클래스에 a^b (a의 b제곱)을 구할 수 있는 기능을 추가
#

class MoreFourCal(FourCal):
    pass


a = MoreFourCal(4, 2)
a.add(), a.mul()


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    

a = MoreFourCal(4, 2)
a.add(), a.mul()

a.pow()

# 상속은 MoreFourCal 클래스처럼 기존 클래스(FourCal)는 
# 그대로 놔둔 채 클래스의 기능을 확장시킬 때 주로 사용.

#######################################
print("메서드 오버라이딩")
# 기존의 함수(메소드)를 수정/보완하여 재정의
#######################################
# 
a = FourCal(4, 0)
a.div()  # ZeroDivisionError:

# 메서드 오버라이딩 (Overriding)
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
            print("분모는 0을 사용할 수 없다.")
            return 0
        else:
            return self.first / self.second
    


a = SafeFourCal(4, 0)
a.div()  # 메서드 오버라이딩 사용

#######################################
print("클래스 변수")
# 객체변수와 클래스변수의 차이?
# 객체변수   :   객체.변수
# 클래스변수 : 클래스.변수
#######################################
# 
class Family:
    lastname = "김"   # 클래스변수


# 클래스이름.클래스 변수로 사용
Family.lastname

# 객체변수로 접근
a = Family()
b = Family()

print(a.lastname)
print(b.lastname)
id(a.lastname), id(b.lastname)

# 클래스변수를 변경하면?
Family.lastname = "박"

print(a.lastname)
print(b.lastname)
id(a.lastname), id(b.lastname), id(Family.lastname)
# 클래스 변수가 공유됨을 확인.

# 객체변수를 변경하면?
a.lastname = "이"
a.lastname, b.lastname, Family.lastname
id(a.lastname), id(b.lastname), id(Family.lastname)

# 실무 프로그래밍에는 클래스 변수보다는 객체변수를 많이 사용.


"""
Author: redwoods
파이썬 코드: ch5_01_class.py
"""
