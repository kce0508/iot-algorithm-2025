import turtle

def draw_debug_fractal(t, length, depth):
    if depth == 0:
        return
    
    # 현재 위치 출력(디버깅)
    print(f"Depth: {depth}, Position:({t.xcor()}, {t.ycor()}), Heading: {t.heading()}")
    turtle.update() # 화면 업데이트

    t.forward(length)
    t.left(60)
    turtle.update() # 화면 업데이트
    draw_debug_fractal(t, length / 2, depth - 1)

    t.right(120)
    turtle.update() # 화면 업데이트
    draw_debug_fractal(t, length / 2, depth - 1)

    t.left(60)
    t.backward(length)
    turtle.update() # 화면 업데이트

# 설정
turtle.tracer(0) # 애니메이션 속도 향상(디버깅용)
screen = turtle.Screen()
screen.bgcolor("white")
screen.title('Fractal debug')
turtle.update() # 화면 업데이트

t = turtle.Turtle()
t.speed(0)
t.penup()
t.goto(-100, 0) # 시작 위치 이동
t.pendown()

turtle.update() # 화면 업데이트

# 프랙탈 그리기 시작(길이 100, 깊이 10)
draw_debug_fractal(t, 100, 10)

turtle.update() # 화면 업데이트
turtle.done()   # 터틀 창 종료하지 않고 유지
