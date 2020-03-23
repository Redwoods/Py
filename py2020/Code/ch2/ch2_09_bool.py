# ch2_09_bool.py

print("불: 불 자료형이란?")
# 불(bool) 자료형이란 참(True)과 거짓(False)을 나타내는 자료형이다.
# 불 자료형은 다음 2가지 값만을 가질 수 있다.
# True - 참
# False - 거짓
# True나 False는 파이썬의 예약어로 true, false와 같이 사용하지 말고
# 첫 문자를 항상 대문자로 사용해야 한다.
#
a = True
b = False
type(a), type(b)
#
# 참과 거짓
#
1 == 1
2 > 1
2 < 1
True + 1
False + 1
#
# 자료형의 참과 거짓
#
bool("python")
bool("")
bool([1, 2, 3])
bool([2, 3])
bool([])
bool(())
bool({})
bool(1)
bool(0)
bool(None)
#
# 불 값을 이용한 코드
#
a = [1, 2, 3, 4]
#
while a:
    print(a.pop())


#
if []:
    print("참")
else:
    print("거짓")


############################
#  Representation error
## double precision representation of floating-point numbers
############################
1-0.9
# 0.09999999999999998
1-0.9==.1
# False

#####
import decimal
x=decimal.Decimal(3.14)
y=decimal.Decimal(2.74)
x,y

x*y
# Decimal('8.603600000000001010036498883')
decimal.getcontext().prec=4
x*y
# Decimal('8.604')
#
"""
Author: redwoods
파이썬 코드: ch2_09_bool.py
"""
