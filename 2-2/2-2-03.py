# 외부 모듈 선언
import turtle
import numpy as np

pixelSize = 10                          # pixel 사이즈의 반지름

def putPixel(x, y, pSize, pCol):        # 메인 소스 코드에서 호출하는 Pixel 채우기 함수
    turtle.penup()                      # 좌표 이동을 위해 펜기능을 비활성화
    turtle.goto(x*pSize, (-1)*y*pSize)   # 주어진 좌표로 이동
    turtle.pendown()                    # 펜기능을 다시 활성화
    turtle.begin_fill()                 # 다각형을 그릴 때 내부를 채우기
    turtle.fillcolor(pCol)              # 다각형의 채움색 설정하기
    turtle.setheading(45)               # 시작각도
    turtle.circle(pSize/2, steps = 4)   # 정사각형 픽셀 그리기
    turtle.end_fill()                   # 채우기 끝

# --------------------------------------------------------------------------------------

faceImg = np.array(                                      # 46쪽 (a) 도형을 나타내는 이미지 데이터 행렬 
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
     [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

smileImg = np.array(                                     # 46쪽 (b) 도형을 나타내는 이미지 데이터 행렬
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 2, 2, 0, 0, 2, 2, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 2, 2, 2, 0, 2, 2, 2, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
     [0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])


for j in range (0, 16) :                                 # (a) faceImage 이미지 출력
    for i in range (0, 16) :
        if (faceImg[j][i] > 0):
            putPixel(i,j, pixelSize, "orange")           # 각 배열 요소의 값이 0보다 크면 오렌지색으로 출력
        else:
            putPixel(i,j, pixelSize, "white")            # 각 배열 요소의 값이 0이면 흰색으로 출력

for j in range (0, 16) :                                 # smileImage 출력
    for i in range (0, 16) :
        if (smileImg[j][i] > 0):
            putPixel(i+20,j, pixelSize, "red")           # 각 배열 요소의 값이 1보다 크면 빨간색으로 출력
        else:
            putPixel(i+20,j, pixelSize, "white")         # 각 배열 요소의 값이 1보다 작으면 흰색으로 출력
            

