from itertools import product

def count_solutions(n):
    def is_safe(pole):
        N = len(pole)
        for row1 in range(N):
            for row2 in range(row1+1, N):
                if pole[row1] == pole[row2] or abs(row1 - row2) == abs(pole[row1] - pole[row2]):
                    return False
        return True

    count = 0
    # Генерируем все возможные комбинации позиций
    for current in product(range(n), repeat=n):
        if len(set(current)) == n and is_safe(current):
            count += 1
    return count

n = int(input())
print(count_solutions(n))
