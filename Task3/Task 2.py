
s = 'gm2y2n10'
s1 =''


num = '0123456789'

c=''
let=''

i = 0
while i < len(s):
    let = s[i]
    if i + 1 < len(s) and s[i+1].isdigit():
        c = int(s[i+1])
        s1 += let * c
        i += 2
    else:
        s1 += let
        i += 1

print(s1)