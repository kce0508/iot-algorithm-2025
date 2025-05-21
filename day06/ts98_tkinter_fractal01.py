import tkinter as tk

def draw_fractal(canvas, x, y, size, depth):
    if depth == 0:
        return
    
    # 정사각형 그리기
    canvas.create_rectangle(x, y, x + size, y + size, outline='black', width=1)

    new_size = size / 2
    # 4개의 방향에 재귀적으로 더 작은 정사각형을 그림
    draw_fractal(canvas, x - new_size / 2, y - new_size / 2, new_size, depth - 1)
    draw_fractal(canvas, x + size - new_size / 2, y - new_size / 2, new_size, depth - 1)
    draw_fractal(canvas, x - new_size / 2, y + size - new_size / 2, new_size, depth - 1)
    draw_fractal(canvas, x + size - new_size / 2, y + size - new_size / 2, new_size, depth - 1)

# 설정
root = tk.Tk()
root.title("Fractal Example")

canvas = tk.Canvas(root, width=600, height=600, bg='white')
canvas.pack()

draw_fractal(canvas, 200, 200, 200, 4)

root.mainloop()