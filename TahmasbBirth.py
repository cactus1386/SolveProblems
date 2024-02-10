# Problem Source: https://quera.org/problemset/193462


def BiggestPart(n, degree):
    a = []
    b = []
    for word in degree.split():
        a.append(float(word))

    a = sorted(a)
    for i in range(len(a)):
        if i == 0:
            b.append(a[i])

        else:
            b.append(a[i] - a[i - 1])

        b.append(360 - a[-1])

    persent = max(b) / 3.6
    print(persent)


first = int(input())
second = input()
BiggestPart(first, second)
