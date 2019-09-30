# ch3_01_if_else.py
#
print("if문은 어떻게 사용?")
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


############################
print("if문의 기본 구조")
'''
if 조건문:
    수행할 문장1
    수행할 문장2
    ...
else:
    수행할 문장A
    수행할 문장B
    ...
'''
#
############################
print("들여 쓰기")
# 예-1
money = True
if money:
    print("택시를")
print("타고")
    print("가라")


#
# 예-2
money = True
if money:
    print("택시를")
    print("타고")
        print("가라")
    

###################################
# 조건문 다음에 콜론(:)을 잊지 말자!
###################################

print("조건식: 비교연산자")
# 비교연산자(<, >, ==, !=, >=, <=)를 쓰는 방법
x=3
y=2
x>y

x<y
x==y
x!=y

###################################
# 조건식 만들기
###################################
# "만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어 가라."
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")


###################################
# 복합 조건식: or, and, not
###################################
# 연산자	설명
# x or y  :	x와 y 둘중에 하나만 참이면 참이다
# x and y :	x와 y 모두 참이어야 참이다
# not x	  : x가 거짓이면 참이다
###################################
# or 복합 조건식 이용
# "돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어 가라."
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")


###################################
# 조건식: in, not in
###################################
#   in	          not in
# x in 리스트	x not in 리스트
# x in 튜플	    x not in 튜플
# x in 문자열	x not in 문자열
###################################
# list
1 in [1, 2, 3]
1 not in [1, 2, 3]
# tuple
'a' in ('a', 'b', 'c')
# string
'j' not in 'python'

# in을 이용한 코드
# "만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어 가라."
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")


###################################
# 조건식: pass
###################################
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    # print("택시를 타고 가라")
    pass
else:
    print("걸어가라")


###################################
# 다중 조건식: elif
# 다양한 조건을 판단
###################################
# "주머니에 돈이 있으면 택시를 타고, 
# 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 
# 돈도 없고 카드도 없으면 걸어 가라."
#
pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라")
    else:
        print("걸어가라")


# elif 이용한 코드
pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")


###################################
# if문을 한 줄로 작성하기
###################################
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass
else:
    print("카드를 사용해라.")


# 한줄 코드
if 'money' in pocket: pass
else: print("카드를 사용해라.")


######################################################
# 조건부 표현식 (conditional expression)
# 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
######################################################
score=80
if score >= 60:
    message = "success"
else:
    message = "failure"

print(message)

# 한줄 코드
message = "success" if score >= 60 else "failure"
print(message)


"""
Author: redwoods
파이썬 코드: ch3_01_if_else.py
"""
