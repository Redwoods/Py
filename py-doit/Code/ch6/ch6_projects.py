# ch6_projects.py
#
print("파이썬 프로그래밍 연습과 도전")
#######################################
# 짤막한 스크립트와 함수들을 만들어 본다.
# 프로그래밍 감각을 키운다.
#######################################


print("1. 내가 프로그램을 만들 수 있을까?")
#######################################
# "문법도 어느 정도 알겠고, 책 내용도 대부분 이해된다.
# 하지만 이러한 지식을 바탕으로 내가 도대체
# 어떤 프로그램을 만들 수 있을까?"
#######################################
#
# 구구단 출력


def GuGu0(n):
    result = []
    result.append(n * 1)
    result.append(n * 2)
    result.append(n * 3)
    result.append(n * 4)
    result.append(n * 5)
    result.append(n * 6)
    result.append(n * 7)
    result.append(n * 8)
    result.append(n * 9)
    return result


print(GuGu0(2))

#
def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i = i + 1
    return result


print(GuGu(2))


#
#
print("2. 3과 5의 배수 합하기")
#######################################
# 10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다.
# 이들의 총합은 23이다.
#
# 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합을 구하라.
#######################################
#
# Wrong!
result_w = 0
for n in range(1, 1000):
    if n % 3 == 0:
        result_w += n
    if n % 5 == 0:
        result_w += n
print(result_w)  # 266333

# Right!
result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n
print(result)  # 233168

# 검산을 해보시오.
result_3_5 = 0
for n in range(1, 1000):
    if n % 3 == 0 and n % 5 == 0:
        result_3_5 += n
print(result_3_5)

(result_w - result_3_5) == result

#
#
print("3. 게시판 페이징하기")
#######################################
# A 씨는 게시판 프로그램을 작성하고 있다.
# 그런데 게시물의 총 건수와 한 페이지에 보여 줄
# 게시물 수를 입력으로 주었을 때
# 총 페이지 수를 출력하는 프로그램을 만들어보자.
#######################################
#
# 한 페이지에서 보여 줄 게시물 수가 최대 10
#
# 총 페이지 수 = (총 건수 / 한 페이지당 보여 줄 건수) + 1
#
def getTotalPage(m, n):
    return m // n + 1


print(getTotalPage(5, 10))  # 1 출력
print(getTotalPage(15, 10))  # 2 출력
print(getTotalPage(25, 10))  # 3 출력
print(getTotalPage(30, 10))  # 4 출력, Wrong!


def getTotalPage(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1


print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))


#
#
print("4. 간단한 메모장 만들기")
#######################################
# 원하는 메모를 파일에 저장하고 추가 및 조회가
# 가능한 간단한 메모장을 만들어 보자.
#
# 필요한 기능은? 메모 추가하기, 메모 조회하기
# 입력 받는 값은? 메모 내용, 프로그램 실행 옵션
# 출력하는 값은? memo.txt
#######################################
#
# 1. 입력으로 받은 옵션과 메모를 출력하는 코드를 작성
"""
# ./doit/memo.py
import sys

option = sys.argv[1]
memo = sys.argv[2]

print(option)
print(memo)
"""

# 2. memo.py를 작성했다면 다음 명령을 수행
# doit 폴더에서 실행
"""
python memo.py -a "Life is too short"
"""

# 3. 입력으로 받은 메모를 파일에 쓰도록 코드를 변경
"""
# ./doit/memo.py
import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
"""


# 4. 다음과 같은 명령을 수행하여 메모 저장 확인.
# doit 폴더에서 실행
"""
python memo.py -a "Life is too short"

python memo.py -a "You need python"

type memo.txt

"""

# 5. 작성한 메모를 출력
# 메모 출력은 다음과 같이 동작
# 메모 추가는 –a 옵션을 사용하고 메모 출력은 –v 옵션을 사용
"""
python memo.py -v
"""
#
# 메모 출력을 위해 다음과 같이 코드를 변경
#
"""
# ./doit/memo.py
import sys

option = sys.argv[1]

if option == '-a':
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)

"""

# 코드를 수정한 후 다음과 같은 명령을 수행
"""
python memo.py -v
"""

#
#
print("5. 탭을 4개의 공백으로 바꾸기")
#######################################
# 문서 파일을 읽어서 그 문서 파일 안에 있는 탭(tab)을
# 공백(space) 4개로 바꾸어 주는 스크립트를 작성
#
# 필요한 기능은? 문서 파일 읽어 들이기, 문자열 변경하기
# 입력 받는 값은? 탭을 포함한 문서 파일
# 출력하는 값은? 탭이 공백으로 수정된 문서 파일
#######################################
#
# 다음과 같은 형식으로 프로그램이 수행
#
"""
python tabto4.py a.txt b.txt
"""
# 1. tabto4.py는 \doit 디렉터리에 저장
"""
# ./doit/tabto4.py
import sys

src = sys.argv[1]
dst = sys.argv[2]

print(src)
print(dst)
"""
#
# 2. 입력값이 정상적으로 출력되는지 확인
#
"""
python tabto4.py a.txt b.txt
"""

#
# 3. 원본 파일(탭을 포함하는 파일)인 a.txt 작성
"""
Life    is  too short
You need    python
"""

#
# 4. 탭을 공백 4개로 변환할 수 있도록 코드를 변경
"""
# ./doit/tabto4.py
import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4)
print(space_content)
"""

#
# 5. tabto4.py를 위와 같이 변경한 후 다음과 같은 명령을 수행
"""
python tabto4.py a.txt b.txt
"""

#
# 6. 변경된 내용을 b.txt 파일에 저장
"""
# ./doit/tabto4.py
import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4)

f = open(dst, 'w')
f.write(space_content)
f.close()
"""

#
# 7. 다음 명령을 수행하여 코드 완성
"""
python tabto4.py a.txt b.txt
"""
# b.txt 파일을 열어서 탭이 4개의 공백 문자로 변경되었는지 확인


#
#
print("6. 하위 디렉터리 검색하기")
#######################################
# 특정 디렉터리부터 시작해서 그 하위 모든 파일 중
# 파이썬 파일(*.py)만 출력해 주는 프로그램을
# 만들려면 어떻게 해야 할까?
#######################################
#
"""
# ./ch06/sub_dir_search.py
import os

def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py': 
                    print(full_filename)
    except PermissionError:
        pass

search("./")
"""

#
# os.walk 사용
"""
# ./ch06/sub_dir_walk.py
import os

for (path, dir, files) in os.walk("./"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" % (path, filename))


"""


"""
Author: redwoods
파이썬 코드: ch6_projects.py
"""
