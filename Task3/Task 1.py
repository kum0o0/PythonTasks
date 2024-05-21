
s = input()
s1 =''
c = 1

for i in range(0,len(s)):
    if (i == len(s)-1):
        if c == 1:
            s1+=s[i]
        else:
            s1+=s[i]+str(c)
            c = 1
    elif (s[i] == s[i+1]):
        c+=1
    else:
        if c == 1:
            s1 += s[i]
        else:
            s1 += s[i] + str(c)
            c = 1
print(s1)