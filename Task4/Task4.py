def f(str):
    s = dict()
    for i in str:
        if i in s:
            print(s[i])
            s[i] += 1
        else:
            print(0)
            s[i] = 1



str = "one two one two five"

spl_str =str.split()
ans = f(spl_str)

