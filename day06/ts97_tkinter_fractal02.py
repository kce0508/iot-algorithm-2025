import tkinter as tk
# Sierpinski 삼각형을 그리는 재귀함수
def draw_sierpinski(canvas, x, y, size, depth):
    if depth == 0:  # depth가 0이면 최종 삼각형을 그림
        canvas.create_polygon(
            x, y + size,
            x + size / 2, y,
            x + size, y + size,
            outline='black', fill='', width=1
        )
        return
    
    # 삼각형의 한 변을 절반으로 줄여서 3개의 하위 삼각형으로 나눔
    new_size = size / 2
    draw_sierpinski(canvas, x, y + new_size, new_size, depth - 1)               # 왼쪽 아래 삼각형
    draw_sierpinski(canvas, x + new_size / 2, y, new_size, depth - 1)           # 위쪽 삼각형
    draw_sierpinski(canvas, x + new_size, y + new_size, new_size, depth - 1)    # 오른쪽 아래 삼각형

# 설정
root = tk.Tk()
root.title("Sierpinski Triangle Fractal")

canvas = tk.Canvas(root, width=600, height=600, bg='white')
canvas.pack()
# Sierpinski 삼각형 그리기 (시작 위치 x=50, y=50, 한 변 길이=500, 깊이=7단계)
draw_sierpinski(canvas, 50, 50, 500, 7)

root.mainloop()