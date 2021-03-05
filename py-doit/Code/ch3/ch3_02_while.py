# ch3_02_whie.py
#
print("while 문은 어떻게 사용?")
# 반복해서 문장을 수행해야 할 경우 while문을 사용한다. 
# 그래서 while문을 반복문이라고도 부른다.

############################
print("while문의 기본 구조")
'''
while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
    ...
'''

# "열 번 찍어 안 넘어가는 나무 없다"는 속담을 파이썬 프로그램으로 반복 실행
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")


#
############################
print("while문 만들기")
#
prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0
while number != 4:
    print(prompt)
    # number = int(input())


#
###################################
print("while문 강제로 빠져나가기")
###################################
# 커피 자판기 작동
# 자판기가 제대로 작동하려면 커피가 얼마나 남았는지 항상 검사해야 한다. 
# 만약 커피가 떨어졌다면 판매를 중단하고 "판매 중지" 문구를 사용자에게 보여준다.
#
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break


###################################
# coffee.py
###################################
"""
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break
"""

#
###################################
print("while문의 맨 처음으로 돌아가기: continue")
###################################
# while문을 빠져나가지 않고 while문의 맨 처음(조건문)으로 
# 다시 돌아가게 만들고 싶은 경우가 생기게 된다. 
# 이때 사용하는 것이 바로 continue문이다.
#
# 1부터 10까지의 숫자 중에서 홀수만 출력하는 것을 while문을 사용해서 작성
#
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)


#
###################################
print("while문의 무한 루프")
###################################
#
"""
while True: 
    수행할 문장1 
    수행할 문장2
    ...
"""
# 무한루프 코드의 예 (^C로 중지 !!!)
while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")



"""
Author: redwoods
파이썬 코드: ch3_02_whie.py
"""
