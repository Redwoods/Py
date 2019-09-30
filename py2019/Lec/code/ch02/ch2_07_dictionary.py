# ch2_07_dictionary.py

print("딕셔너리: 딕셔너리(Dictionary)란?")
# 딕셔너리란 대응 관계를 나타내는 자료형.
# 연관 배열(Associative array) 또는 해시(Hash)
# 딕셔너리는 Key와 Value를 한 쌍으로 갖는 자료형
#
# 기본 딕셔너리의 모습
# {Key1:Value1, Key2:Value2, Key3:Value3, ...}
# Key와 Value의 쌍 여러 개가 { }로 둘러싸여 있다.
# 각각의 요소는 Key : Value 형태로 이루어져 있고 쉼표(,)로 구분
dic = {"name": "pey", "phone": "0119993323", "birth": "1118"}
# Key는 각각 'name', 'phone', 'birth'
# 각 Key에 해당하는 Value는 'pey', '0119993323', '1118'

# 여러 가지 딕셔너리
a = {1: "hi"}
a[1]
a = {"a": [1, 2, 3]}  # value에는 복합 자료형도 사용된다.
len(a)
a[a]  # TypeError
a["a"]
#
# 딕셔너리 쌍 추가하기
#
a = {1: "a"}
a[2] = "b"
a["name"] = "pey"
a
a[3] = [1, 2, 3]
a
#
# 딕셔너리 쌍 삭제하기
#
del a[1]
a
#
print("딕셔너리: 사용 방법")
d = {"김연아": "피겨스케이팅", "류현진": "야구", "손흥민": "축구", "귀도": "파이썬"}
d
d["손흥민"]
#
# 딕셔너리에서 Key 사용해 Value 얻기
#
grade = {"pey": 10, "julliet": 99}
grade["pey"]
grade["julliet"]
#
a = {1: "a", 2: "b"}
a[1]  # 1은 key
#
a = {"a": 1, "b": 2}
a["b"]
a[b]  # TypeError
#
dic = {"name": "pey", "phone": "0109993323", "birth": "1118"}
dic["birth"]
dic["phone"]
#
# 딕셔너리 만들 때 주의할 사항
# 딕셔너리에서 Key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면
# 하나를 제외한 나머지 것들이 모두 무시된다
#
a = {1: "a", 1: "b"}
a[1]
#
print("딕셔너리: 관련 내장 함수들")
#
# Key 리스트 만들기(keys)
#
a = {"name": "pey", "phone": "0119993323", "birth": "1118"}
a.keys()
list(a.keys())
#################################################
# 기본적인 반복(iterate) 구문(예: for문)을 실행
#################################################
for k in a.keys():
    print(k)



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
a = {"name": "pey", "phone": "0119993323", "birth": "1118"}
a.get("name")  # a['name']
a.get("phone")  # a['phone']

print(a["nokey"])  # KeyError
#
# get(x, '디폴트 값')
#
# 딕셔너리 안에 찾으려는 Key 값이 없을 경우
# 미리 정해 둔 디폴트 값을 대신 가져오게 설정.
#
a.get("foo", "bar")
a.get("name", "bar")
#
# 해당 Key가 딕셔너리 안에 있는지 조사하기(in)
#
a = {"name": "pey", "phone": "0119993323", "birth": "1118"}
"name" in a
"foo" in a

#
#
"""
Author: redwoods
파이썬 코드: ch2_07_dictionary.py
"""
