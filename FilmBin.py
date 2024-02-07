# Problem Source: https://quera.org/problemset/655

def Sort(n):
    r = []
    for i in range(n):
        a = input()
        result = a[0].upper() + a[1:].lower()
        r.append(result)
    
    for x in r:
        print(x)
    
n = int(input())
Sort(n)