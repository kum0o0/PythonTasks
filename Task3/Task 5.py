def proportion(a):
    if(a[0][0] / a[0][1] == a[1][0] / a[1][1] == a[2][0] / a[2][1]):
        return True
    if(a[0][0] / a[0][2] == a[1][0] / a[1][2] == a[2][0] / a[2][2]):
        return True
    return False

def func(mat):
    if proportion(mat):
        print('Линейно зависимые')
    else:
        print('Линейно независимые')

    for i in mat:
        print(i)


mat1 = [
    [1,3,3],
    [2,6,20],
    [6,18,0]
]

mat2 = [
    [1,1,1],
    [1,1,1],
    [13,13,13]
]


mat3 = [
    [10,20,30],
    [213,1230,120],
    [703,803,4410]
]

func(mat1)
func(mat2)
func(mat3)