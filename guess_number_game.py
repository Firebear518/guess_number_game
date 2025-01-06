from comparing2 import comparing_number
from randomize import get_random

print("----------------------------------")
print("[#] Guess Number Game")
print("----------------------------------")

print("[#] 시작, 끝 범위를 입력해주세요.")
start, end = map(int, input("Input: ").split())
random_number = get_random(start, end)
print("[#] 숫자가 생성되었습니다.")

while(True):
    ipt = 0
    print("----------------------------------")
    ipt = int(input("Your Input: "))
    if comparing_number(random_number, ipt) == "정답입니다!":
        print("[#] 맞추셨습니다.")
        break
    else:
        print("[#] " + comparing_number(random_number, ipt))
    print("----------------------------------")