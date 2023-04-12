from typing import List
import sys

input = sys.stdin.readline


class Set:
    def __init__(self):
        self.data = []

    def command_handler(self, command: List[str]):
        if command[0] == "add":
            self._add(int(command[1]))
        elif command[0] == "remove":
            self._remove(int(command[1]))
        elif command[0] == "check":
            self._check(int(command[1]))
        elif command[0] == "toggle":
            self._toggle(int(command[1]))
        elif command[0] == "all":
            self._all()
        elif command[0] == "empty":
            self._empty()

    def _add(self, x: int):
        if x not in self.data:
            self.data.append(x)

    def _remove(self, x: int):
        if x in self.data:
            self.data.remove(x)

    def _check(self, x: int):
        if x in self.data:
            print(1)
        else:
            print(0)

    def _toggle(self, x: int):
        if x in self.data:
            self.data.remove(x)
        else:
            self.data.append(x)

    def _all(self):
        self.data = [i for i in range(1, 21)]

    def _empty(self):
        self.data = []


if __name__ == "__main__":
    s = Set()
    for _ in range(int(input())):
        s.command_handler(input().split())
