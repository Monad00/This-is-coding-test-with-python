# success
a, b, c = map(int, input().split())
d = list(map(int, input().split()))
print(d)

result = 0
result += max(d) * c * (b%c)
d.remove(max(d))
result += max(d) * (b - c*(b%c))
print(result)