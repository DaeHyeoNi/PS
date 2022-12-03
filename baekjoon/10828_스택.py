import sys
from typing import Optional

input = sys.stdin.readline


# 10845_큐.py 에서 만들어둔 구조를 재활용이 가능해서
# 푸는데 20초 밖에 걸리지 않았다 .. ㅋㅋ


def _push(number: int) -> None:
    queue.append(number)


def _pop() -> int:
    if _is_empty():
        return -1
    else:
        temp = queue[-1]
        del queue[-1]
        return temp


def _get_size() -> int:
    return len(queue)


def _is_empty() -> bool:
    return len(queue) == 0


def _get_index(index: int) -> int:
    # index: 0 = front, -1 = back
    return -1 if _is_empty() else queue[index]


def command_processor(cmd: str, number: Optional[int]) -> None:
    if cmd == "push":
        _push(number)
    elif cmd == "pop":
        print(_pop())
    elif cmd == "size":
        print(_get_size())
    elif cmd == "empty":
        print(1 if _is_empty() else 0)
    elif cmd == "top":
        print(_get_index(-1))


queue = []
N = int(input())
for _ in range(N):
    command = list(input().split())
    if len(command) == 1:
        command.append(None)
    command_processor(command[0], command[1])
