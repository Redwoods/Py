# wk03_06_set.py

print("집합: 집합(Set)이란?")
# 집합에 관련된 것을 쉽게 처리하기 위해 만든 자료형
# 중복된 값을 허용하지 않는다.
#
# set 키워드를 사용해서 집합자료형을 만든다.
#
s1 = set([1, 2, 3])
s1
s1n = set([1, 2, 3, 2])
s1n
s2 = set("Hello")
s2

#
# 집합 자료형의 특징
# 1. 중복을 허용하지 않는다.
# 2. 순서가 없다(Unordered).
# *** set 자료형은 순서가 없기(unordered) 때문에 인덱싱으로 값을 얻을 수 없다.
#
s1 = set([1,2,3])
s1[0]
l1=list(s1)
l1
l1[0]
#
t1=tuple(s1)
t1
t1[0]
#
# 교집합, 합집합, 차집합 구하기
#
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
# 
# 1. 교집합
#
s1 & s2
s1.intersection(s2)
# 
# 2. 합집합
#
s1 | s2
s1.union(s2)
# 
# 3. 차집합
#
s1 - s2
s2 - s1
s1.difference(s2)
s2.difference(s1)

#
print("집합 (set): 관련 내장 함수들")
#
# 값 1개 추가하기(add)
#
s1 = set([1, 2, 3])
s1.add(4)
s1
#
# 값 여러 개 추가하기(update)
#
s1 = set([1, 2, 3])
s1.update([4,5,6])
s1
#
# 특정 값 제거하기(remove)
#
s1 = set([1, 2, 3])
s1.remove(2)
s1
#################################################
# 기본적인 반복(iterate) 구문(예: for문)을 실행
#################################################
for k in a.keys():
    print(k)
#
#
# Value 리스트 만들기(values)
#
a.values()
#
# Key, Value 쌍 얻기(items)
#
a.items()  # Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.
#
#
# Key: Value 쌍 모두 지우기(clear)
#
a.clear()
a
#
# Key로 Value얻기(get)
#
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a.get('name')    # a['name']
a.get('phone')   # a['phone']

a = {'name': 'pey', 'phone'
print(a['nokey'])
#
# get(x, '디폴트 값')
#
# 딕셔너리 안에 찾으려는 Key 값이 없을 경우
# 미리 정해 둔 디폴트 값을 대신 가져오게 설정.
#
a.get('foo', 'bar')
a.get('name', 'bar')
#
# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
#
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
'name' in a
'foo' in a

#
#
"""
Author: redwoods
파이썬 코드: wk03_06_set.py
"""
