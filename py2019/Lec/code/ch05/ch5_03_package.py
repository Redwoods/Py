# ch5_03_package.py
#
print("패키지란 무엇인가?")
#######################################
# 파이썬 모듈들을 모아놓은 폴더로 구성
# 유사한 기능을 가진 모듈들을 묶어서 구성
#######################################
#
# 가상의 game 패키지 예
#
"""
game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py
"""
# game 디렉터리가 이 패키지의 루트 디렉터리이고
# sound, graphic, play는 서브 디렉터리이다.

print("패키지 만들기")
#######################################
# 패키지 기본 구성 요소 준비하기
#######################################
# 1. 루트폴더, 서버폴더 만들기
# 2. *.py 소스파일 준비

#
# 1. 루트폴더, 서버폴더 만들기
"""
./game/__init__.py
./game/sound/__init__.py
./game/sound/echo.py
./game/graphic/__init__.py
./game/graphic/render.py
"""

#
# 2. *.py 소스파일 준비
"""
각 디렉터리에 __init__.py 파일을 만들어 놓기만 하고 
내용은 일단 비워 둔다.
# echo.py
def echo_test():
    print ("echo")

# render.py
def render_test():
    print ("render")

"""
# 현재 폴더 내에 game 폴더가 포함됨.
#


print("패키지 안의 함수 실행하기")
#######################################
# package를 import하여 내부 함수 실행
#######################################
#
# 1. echo 모듈을 import하여 실행
import game.sound.echo

game.sound.echo.echo_test()

# 2. echo 모듈이 있는 디렉터리까지를 from ... import하여 실행
from game.sound import echo

echo.echo_test()

# 3. echo 모듈의 echo_test 함수를 직접 import하여 실행
from game.sound.echo import echo_test

echo_test()


#
# 다음과 같이 echo_test 함수를 사용하는 것은 불가능
import game

game.sound.echo.echo_test()

import game.sound.echo.echo_test  # ModuleNotFoundError:


print("__init__.py 의 용도")
#######################################
# __init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할
# 만약 game, sound, graphic 등 패키지에 포함된 디렉터리에
# __init__.py 파일이 없다면 패키지로 인식되지 않는다.
#######################################
#
from game.sound import *

echo.echo_test()


print("relative 패키지")
#######################################
# 만약 graphic 디렉터리의 render.py 모듈이
# sound 디렉터리의 echo.py 모듈을 사용
#
# render.py를 수정
#######################################
#
from game.graphic.render import render_test

render_test()

# .. : parent folder
#  . : current folder
"""
# render.py
from ..sound.echo import echo_test

def render_test():
    print ("render")
    echo_test()
"""


"""
# render.py
from game.sound.echo import echo_test
def render_test():
    print ("render")
    echo_test()
"""


"""
Author: redwoods
파이썬 코드: ch5_03_package.py
"""
