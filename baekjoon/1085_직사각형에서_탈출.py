x, y, w, h = map(int, input().split())
print(min(min(x, abs(w - x)), min(y, abs(y - h))))
