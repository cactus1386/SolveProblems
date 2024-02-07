# Problem Source: https://leetcode.com/problems/longest-substring-without-repeating-characters/description
s = "abccdcab"
result = ""

for i in s:
    if i in result:
        pass
    else:
        result += i

print(len(result))
