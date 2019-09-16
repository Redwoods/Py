# wk03_02_list_operations.py

print("리스트: 리스트 연산하기")
#
# 리스트 더하기(+)
#
a = [1, 2, 3]
b = [4, 5, 6]
a + b
#
# 리스트 반복하기(*)
#
a * 3
#
# 리스트 길이구하기
#
len(a)
#
# 초보자가 범하기 쉬운 리스트 연산 오류
#
a = [1, 2, 3]
a[2] + "hi"
str(a[2]) + "hi"
#
# 리스트의 수정과 삭제
#
a = [1, 2, 3]
a[2] = 4  # list is mutable!!!
a

#
# del 함수 사용해 리스트 요소 삭제하기
#
a = [1, 2, 3]
del a[1]
a
a = [1, 2, 3, 4, 5]
del a[2:]
a

#
"""
Author: redwoods
파이썬 코드: wk03_02_list_operation.py
"""
