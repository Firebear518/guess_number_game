from ? import ?
from comparing2 import comparing_number

print("----------------------------------")
print("[#] Guess Number Game")
print("----------------------------------")

print("[#] 시작, 끝 범위를 입력해주세요.")
start, end = map(int, input("Input: ").split())
random_number = randomize(start, end)
print("[#] 숫자가 생성되었습니다.")

while(True):
    ipt = 0
    print("----------------------------------")
    ipt = int(input("Your Input: "))
    comparing(random_number, ipt)
    print("----------------------------------")