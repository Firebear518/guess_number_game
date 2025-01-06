def comparing_number(user_guess, answer):
    if user_guess < answer:
        return "정답보다 낮습니다!"
    elif user_guess > answer:
        return "정답보다 높습니다!"
    else:
        return "정답입니다!"
