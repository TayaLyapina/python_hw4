# Пример:
# 5 1 1 3 3 3 1 1 2

# 1-ый раз: 5 1 1 1 1 2
# 2-ой раз: 5 2
# Ответ: 7

n = int(input('Введите количество шариков: '))
balls = list()
balls_1 = list()
for i in range(n):
    ball = int(input('Введите номер шарика от 0 до 9: '))
    balls.append(ball)
    balls_1.append(ball)

while len(balls) >= 3:
    ball_prev = balls[0]
    count = 1 
    i = 1
    for ball in balls[1:]:
        if ball == ball_prev:
            count += 1
        else: 
            if count >= 3:
                break
            else:
                ball_prev = ball
                count = 1
        i += 1
    if count >= 3:
        del balls[i-count:i] 
    else:
        break
print(len(balls_1) - len(balls))