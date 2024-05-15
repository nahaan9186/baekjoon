s = input()

def reverse(s, word) :
    if len(s) == 0 :
        return word
    word += s[-1]
    # print(f'word:{word},s:{s}')
    return reverse(s[:-1], word)

i=0
while s[i] == '<':
    
li_s = s.split()
# print(li_s)

res = []
word = str()
for i in range(len(li_s)):
    res.append(reverse(li_s[i], word))
# print(res)
print(str(' '.join(res)))