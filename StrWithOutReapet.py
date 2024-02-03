s = "abccdcab"
result = ""

for i in s:
    if i in result:
        pass
    else:
        result += i

print(len(result))
