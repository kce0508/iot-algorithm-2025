import tkinter as tk
import random

# Barnsley Fern을 생성하는 함수
def barnsley_fern(canvas, x, y, iterations):
    points = [(x, y)]
    # 지정된 반복 횟수만큼 점을 생성
    for _ in range(iterations):
        x, y = points[-1]   # 이전 점의 좌표
        r = random.random() # 0.0 ~ 1.0 사이의 난수 생성
        # 확률에 따라 변환 규칙 적용
        if r < 0.01:    # 줄기 부분
            new_x = 0
            new_y = 0.016 * y
        elif r < 0.86:  # 왼쪽 큰잎
            new_x = 0.85 * x + 0.04 * y 
            new_y = -0.04 * x + 0.84 * y + 1.6
        elif r < 0.93:  # 오른쪽 작은 잎
            new_x = 0.2 * x - 0.26 * y
            new_y = 0.23 * x + 0.22 * y + 1.6
        else:           # 왼쪽 작은 잎
            new_x = -0.15 * x + 0.28 * y
            new_y = 0.26 * x + 0.24 * y + 0.44
        # 새 점 추가
        points.append((new_x, new_y))   
    # 모든 점을 캔버스에 그리기
    for px, py in points:
        canvas.create_oval(300 + px * 50, 550 - py * 50, 301 + px * 50, 551 - py * 50, fill='green', outline='green')

# tkinter 기본 설정
root = tk.Tk()
root.title("Barnsley Fern Fractal")
# 캔버스 생성
canvas = tk.Canvas(root, width=600, height=600, bg='white')
canvas.pack()
# 프랙탈 그리기 시작
barnsley_fern(canvas, 0, 0, 40000)
# tkinter 이벤트 루프 실행
root.mainloop()
