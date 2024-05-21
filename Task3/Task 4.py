_input = ['abc', 'abd', 'bcd', 'abc', ' ', 'abd', 'dcd', 'abc']

d = {}

for i in _input:
    if i in d:
      d[i] += 1
    else:
       d[i] = 1

print(d)