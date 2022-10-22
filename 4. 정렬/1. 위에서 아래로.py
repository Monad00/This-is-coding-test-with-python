#success
n = int(input())

n_list = []
for _ in range(n):
    n_list.append(int(input()))

for i in sorted(n_list, reverse= True):
    print(i, end = " ")
