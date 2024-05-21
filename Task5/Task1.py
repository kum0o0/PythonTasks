with open("input1.txt","r") as file:
    mult = 1
    for x in file.readline().split():
        mult*=int(x)


f = open("output1.txt","w")
f.write(str(mult))
f.close()
