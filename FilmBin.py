# Problem Source: https://quera.org/problemset/655

def Sort(n):
    r = []
    u = ''
    for i in range(n):
        a = input().split()
        for word in a: 
            result = word[0].upper() + word[1:].lower()
            u += result + ' '
        r.append(u)
        u = ''
    
    for x in r:
        print(x)
    
n = int(input())
Sort(n)