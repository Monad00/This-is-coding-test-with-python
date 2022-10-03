n, m = map(int, input().split())
result = 0
# success
for i in range(n):
    data = list(map(int, input().split))
    v = min(data)
    result = max(result, v)
print(result)
