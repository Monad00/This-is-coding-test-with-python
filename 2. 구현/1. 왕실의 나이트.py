# success
l = input()
alpha = [0,'a','b','c','d','e','f','g','h']
move_type = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
count = 0
for i in move_type:
    column = alpha.index(l[0])
    row = int(l[1])
    column += i[0]
    row += i[1]
    if column > 0 and row > 0 and column <= 8 and row <= 8:
        count += 1
print(count)

# answer
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1
                    
steps = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 16

print(result)