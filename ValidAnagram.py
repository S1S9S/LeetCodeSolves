s = "anagram"
t = "nagaram"

if len(s) != len(t):
    print(False)

count_s = {}
count_t = {}

for ch in s:
    count_s[ch] = count_s.get(ch,0)+1

for ch in t:
    count_t[ch] = count_t.get(ch,0)+1

print(count_s == count_t)
