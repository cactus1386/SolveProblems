# Problem Source: https://quera.org/problemset/218361

def eyes(inp, inp2):
    r = 0
    for i in range(0,7):
        if inp[i] == inp2[i] == '1':
            r += 1
    return r

inp = input()
inp2 = input()
print(eyes(inp, inp2))