n = int(input())
pos = [-1]*n

def is_safe(pos, col, row):
    for i in range(row):
        if pos[i] == col or abs(row - i) == abs(col - pos[i]):
            return False
    return True

def count_sol(pos, row, n):
    if row == n:
        return 1
    count = 0
    for col in range(n):
        if is_safe(pos, col, row):
            pos[row]  = col
            count+=count_sol(pos, row + 1, n)
    return count

print(count_sol(pos, 0, n))
