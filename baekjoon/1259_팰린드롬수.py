# 회문 검증인데 문제가 시간 복잡도를 요구하지 않아서 reverse ..
def check(num: str):
    before = num
    after = num[::-1]
    if before == after:
        return "yes"
    return "no"

while True:
    num = input()
    if num == '0':
        break
    print(check(num))