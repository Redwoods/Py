# ch2_05_list_functions.py

print("리스트: 내부 함수 이용")
#
# 리스트에 요소 추가(append)
#
a = [1, 2, 3]
a.append(4)
a
# 리스트 안에는 어떤 자료형도 추가할 수 있다.
# 리스트에 다시 리스트를 추가한 결과
a.append([5, 6])
a
#
# 리스트 정렬(sort)
#
a = [1, 4, 3, 2]
a.sort()
a

s = ["a", "c", "b"]
s.sort()
s
#
# 리스트 뒤집기(reverse)
#
a = ["a", "c", "b"]
a.reverse()
a
#
# 위치 반환(index)
#
a = [1, 2, 3]
a.index(3)
a.index(1)
a.index(0)

s = ["a", "c", "b"]
s.index(3)  # Error
s.index(a)  # Error
s.index("a")

#
# 리스트에 요소 삽입(insert)
#
a = [1, 2, 3]
a.insert(0, 4)
a
a.insert(3, 5)
a


#
# 리스트 요소 제거(remove)
#
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
a
# 3을 리스트 a에서 완전히 제거
a.remove(3)
a
a.remove(3)  # ValueError
#
# 리스트 요소 끄집어내기(pop)
#
a = [1, 2, 3]
a[2] + "hi"  # TypeError
str(a[2]) + "hi"
#
# 리스트의 수정과 삭제
#
a = [1, 2, 3]
# pop()은 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제한다.
a.pop()
a
#
a = [1, 2, 3]
# pop(x)는 리스트의 index가 x인 요소를 돌려주고 그 요소는 삭제한다.
a.pop(1)
a
a.pop(2)  # IndexError

#
# 리스트에 포함된 요소 x의 개수 세기(count)
#
a = [1, 2, 3, 1]
a.count(1)
#
# 리스트 확장(extend)
#
a = [1, 2, 3]
a.extend([4, 5])
a  # a.extend([4, 5])는 a += [4, 5]와 동일

b = [6, 7]
a.extend(b)
a

#
#
"""
Author: redwoods
파이썬 코드: ch2_05_list_functions.py
"""
