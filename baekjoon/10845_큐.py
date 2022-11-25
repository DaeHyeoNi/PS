import sys
from typing import Optional

input = sys.stdin.readline


def _push(number: int) -> None:
    queue.append(number)


def _pop() -> int:
    if _is_empty():
        return -1
    else:
        temp = queue[0]
        del queue[0]
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
    elif cmd == "front":
        print(_get_index(0))
    elif cmd == "back":
        print(_get_index(-1))


queue = []
N = int(input())
for _ in range(N):
    command = list(input().split())
    if len(command) == 1:
        command.append(None)
    command_processor(command[0], command[1])
