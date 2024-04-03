n = int(input())
s = set()
for i in range(0,n):
    city = input()
    if city in s:
        print("REPEAT")
    else:
        s.add(city)
        print("OK")
print(s)