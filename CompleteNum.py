def is_complete(n):
    result = 0

    for i in range(1, n // 2 + 1):
        if n % i == 0:
            result += i

    return result == n


n = int(input())
if is_complete(n):
    print("YES")
else:
    print("NO")
