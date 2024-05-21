with open("input2.txt","r") as file:
    mas=[int(line) for line in file]
with open("output2.txt", 'w') as file:
    file.writelines(str(i)+'\n' for i in sorted(mas))