with open('input3.txt','r', encoding='UTF8') as file:
    line = file.readlines()
    line.sort(key=lambda x: int(x.split()[2]))
with open('output3.txt', 'w', encoding = 'UTF8') as file:
    file.write('Старший:\t')
    file.write(line[-1])
    file.write('Младший:\t')
    file.write(line[0])