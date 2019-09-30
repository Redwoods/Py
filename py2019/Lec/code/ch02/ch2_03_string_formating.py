# ch2_03_string_formating.py

print("문자열: 포매팅이란?")
# 1. 숫자 바로 대입
"I eat %d apples." % 3

# 2. 문자열 바로 대입
"I eat %s apples." % "five"

# 3. 숫자 값을 나타내는 변수로 대입
number = 3
"I eat %d apples." % number

# 4. 2개 이상의 값 넣기
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % number  # , day   # Error
"I ate %d apples. so I was sick for %s days." % (number, day)
# 소괄호 안에 콤마(,)로 구분하여 각각의 값을 넣어 준다.

print("문자열: 포맷 코드")
# %d, %s, %c, %f, %o, %x, %%
# %s, 묵시적 형변환
"I have %s apples" % 3
"rate is %s" % 3.234

"Error is %d%." % 98
"Error is %d%%." % 98

###############################################-p60
print("문자열: 포맷 코드와 숫자 함께 사용하기")
# 1. 정렬과 공백
"%10s" % "hi"
"%-10sjane." % "hi"
# 2. 소수점 표현하기
"%0.4f" % 3.42134234
"%10.4f" % 3.42134234

print("문자열: format 함수를 사용한 포매팅")
# 1. 숫자 바로 대입하기
"I eat {0} apples".format(3)
"I eat {0} {1} apples".format(3, 4)

# 2. 문자열 바로 대입하기
"I eat {0} apples".format("five")
"I eat {0} apples from {1} boxes".format("five", "three")

# 3. 숫자 값을 가진 변수로 대입하기
number = 3
"I eat {0} apples".format(number)
"I eat {0} apples".format(number + 1)

# 2개 이상의 값 넣기
number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)
# 이름으로 넣기
"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
# 인덱스와 이름을 혼용해서 넣기
"I ate {0} apples. so I was sick for {day} days.".format(10, day=3)
#
######################################
# 왼쪽 정렬/ 오른쪽 정렬
"{0:<10}".format("hi")
"{0:>10}".format("hi")
# 가운데 정렬
"{0:^10}".format("hi")
# 공백 채우기
"{0:=^10}".format("hi")
"{0:!<10}".format("hi")
# 도전하기
# "{0:<10}{1:>10}".format("hi",'hcit')

#########################################

# 소수점 표현하기
y = 3.42134234
"{0:0.4f}".format(y)
"{0:10.4f}".format(y)
# { 또는 } 문자 표현하기
"{{ and }}".format()

##########################
##### f 문자열 포매팅 #####
##### .format() 대체
##########################
print("문자열: f 문자열 포매팅")
name = "홍길동"
age = 30
f"나의 이름은 {name}입니다. 나이는 {age}입니다."

age = 30
f"나는 내년이면 {age+1}살이 된다."

# 딕셔너리는 f 문자열 포매팅에서 다음과 같이 사용
d = {"name": "홍길동", "age": 30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
# 정렬
f'{"hi":<10}'  # 왼쪽 정렬
f'{"hi":>10}'  # 오른쪽 정렬
f'{"hi":^10}'  # 가운데 정렬
# 공백 채우기
y = 3.42134234
f"{y:0.4f}"  # 소수점 4자리까지만 표현
f"{y:10.4f}"  # 소수점 4자리까지 표현하고 총 자리수를 10으로 맞춤
# { } 문자를 표시
f"{{ and }}"

##############################################
print("문자열: 관련 내장 함수들")
# 문자 개수 세기(count)
a = "hobby"
a.count("b")
# 위치 알려주기1(find)
a = "Python is the best choice"
a.find("b")
a.find("k")  # what value?
# 위치 알려주기2(index)
a = "Life is too short"
a.index("t")
a.index("k")

# 문자열 삽입(join)
",".join("abcd")
",".join(["a", "b", "c", "d"])
# 소문자를 대문자로 바꾸기(upper)
a = "hi"
a.upper()
# 대문자를 소문자로 바꾸기(lower)
a = "IoT"
a.lower()
# 왼쪽 공백 지우기(lstrip)
a = " hi "
a.lstrip()
# 오른쪽 공백 지우기(rstrip)
a.rstrip()
# 양쪽 공백 지우기(strip)
a.strip()
# 문자열 바꾸기(replace)
a = "Life is too short"
a.replace("Life", "Your leg")

# 문자열 나누기(split) -> 리스트로 변환하여 반환
a = "Life is too short"
a.split()
b = "a:b:c:d"
b.split(":")

#### 도전하기 #####
# format 함수 또는 f 문자열 포매팅을 이용해서 '!!!python!!!' 문자열을 출력해보시오.
"{0:!^12}".format("python")
f'{"python":!^12}'


"""
Author: redwoods
파이썬 코드: ch2_03_string_formatting.py
"""
