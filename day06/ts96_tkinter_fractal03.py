import tkinter as tk

# 코흐 곡선 그리는 재귀 함수
def draw_koch(canvas, x1, y1, x2, y2, depth):
    if depth == 0:
        canvas.create_line(x1, y1, x2, y2, fill='black', width=1)
        return
    # 시작점과 끝점 사이의 벡터 계산
    dx = x2 - x1
    dy = y2 - y1
    # 3등분한 지점 계산
    x3 = x1 + dx / 3
    y3 = y1 + dy / 3
    x5 = x1 + 2 * dx / 3
    y5 = y1 + 2 * dy / 3
    # 가운데 정삼각형의 꼭짓점 좌표 계산(회전 공식 활용) 
    x4 = (x3 + x5) / 2 - (y5 - y3) * (3 ** 0.5) / 2
    y4 = (y3 + y5) / 2 + (x5 - x3) * (3 ** 0.5) / 2
    # 4개 구간으로 나누어 재귀 호출
    draw_koch(canvas, x1, y1, x3, y3, depth - 1)
    draw_koch(canvas, x3, y3, x4, y4, depth - 1)
    draw_koch(canvas, x4, y4, x5, y5, depth - 1)
    draw_koch(canvas, x5, y5, x2, y2, depth - 1)

# 설정
root = tk.Tk()
root.title("Koch snowflake Fractal")

canvas = tk.Canvas(root, width=600, height=600, bg='white')
canvas.pack()

x_start, y_start = 50, 300
x_end, y_end = 550, 300
depth = 6

draw_koch(canvas, x_start, y_start, x_end, y_end, depth)

root.mainloop()
