import sys
from collections import deque

input = sys.stdin.readline


class Deck:
    def __init__(self):
        self.deq = deque()

    def push_front(self, x):
        self.deq.appendleft(x)

    def push_back(self, x):
        self.deq.append(x)

    def pop_front(self):
        if self.deq:
            return self.deq.popleft()
        else:
            return -1

    def pop_back(self):
        if self.deq:
            return self.deq.pop()
        else:
            return -1

    def size(self):
        return len(self.deq)

    def empty(self):
        if self.deq:
            return 0
        else:
            return 1

    def front(self):
        if self.deq:
            return self.deq[0]
        else:
            return -1

    def back(self):
        if self.deq:
            return self.deq[-1]
        else:
            return -1


def main():
    n = int(input())
    deck = Deck()

    for _ in range(n):
        command = input().split()

        if command[0] == "push_front":
            deck.push_front(command[1])
        elif command[0] == "push_back":
            deck.push_back(command[1])
        elif command[0] == "pop_front":
            print(deck.pop_front())
        elif command[0] == "pop_back":
            print(deck.pop_back())
        elif command[0] == "size":
            print(deck.size())
        elif command[0] == "empty":
            print(deck.empty())
        elif command[0] == "front":
            print(deck.front())
        elif command[0] == "back":
            print(deck.back())


if __name__ == "__main__":
    main()
