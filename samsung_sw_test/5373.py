import sys, copy
input = lambda: sys.stdin.readline().rstrip()

def rotate(arr, clock=True):
    tmp = [[0 for _ in range(3)] for _ in range(3)]
    
    if clock:
        for i in range(3):
            for j in range(3):
                tmp[j][2-i] = arr[i][j]
    else:
        for i in range(3):
            for j in range(3):
                tmp[2-j][i] = arr[i][j]
    return tmp

def up(clock=True):
    cube['U'] = rotate(cube['U'], clock)
    if clock:
        cube['F'][0], cube['L'][0], cube['B'][0], cube['R'][0] = cube['R'][0][:], cube['F'][0][:], cube['L'][0][:], cube['B'][0][:]
    else:
        cube['F'][0], cube['L'][0], cube['B'][0], cube['R'][0] = cube['L'][0][:], cube['B'][0][:], cube['R'][0][:], cube['F'][0][:]

def down(clock=True):
    cube['D'] = rotate(cube['D'], clock)
    if clock:
        cube['F'][2], cube['L'][2], cube['B'][2], cube['R'][2] = cube['L'][2][:], cube['B'][2][:], cube['R'][2][:], cube['F'][2][:]
    else:
        cube['F'][2], cube['L'][2], cube['B'][2], cube['R'][2] = cube['R'][2][:], cube['F'][2][:], cube['L'][2][:], cube['B'][2][:]

def left(clock=True):
    cube['L'] = rotate(cube['L'], clock)
    cube_seq = ['B', 'U', 'F', 'D'] if clock else ['U', 'B', 'D', 'F']
    tmp = []
    last_cube = copy.deepcopy(cube)
    for i in range(3):
        tmp.append(cube[cube_seq[-1]][i][0])
    for s in cube_seq:
        if s=='B':
            for i in range(3):
                cube[s][2-i][2], tmp[i] = tmp[i], last_cube[s][i][2]
            tmp = tmp[::-1]
        else:
            for i in range(3):
                cube[s][i][0], tmp[i] = tmp[i], last_cube[s][i][0]


def right_(clock=True):
    cube['R'] = rotate(cube['R'], clock)

    cube_seq = ['U', 'B', 'D', 'F'] if clock else ['B', 'U', 'F', 'D']
    tmp = []
    last_cube = copy.deepcopy(cube)
    last_cube['B'] = last_cube['B'][::-1]
    for i in range(3):
        tmp.append(cube[cube_seq[-1]][i][2])
    
    for s in cube_seq:
        
        if s=='B':
            for i in range(3):
                cube[s][2-i][0], tmp[i] = tmp[i], last_cube[s][2-i][0]
            tmp = tmp[::-1]
        else:
            for i in range(3):
                cube[s][i][2], tmp[i] = tmp[i], last_cube[s][i][2]
            

def front(clock=True):
    cube['F'] = rotate(cube['F'], clock)

    last_cube = copy.deepcopy(cube)
    tmp = []
    tmp.append(last_cube['U'][2])
    tmp.append([last_cube['R'][i][0] for i in range(3)])
    tmp.append(last_cube['D'][0][::-1])
    tmp.append([last_cube['L'][i][2] for i in range(2, -1, -1)])

    if clock:
        for i in range(3):
            cube['R'][i][0] = tmp[0][i]
        cube['D'][0] = tmp[1][::-1]
        for i in range(3):
            cube['L'][2-i][2] = tmp[2][i]
        cube['U'][2] = tmp[3][:]
    else:
        for i in range(3):
            cube['L'][2-i][2] = tmp[0][i]
        cube['U'][2] = tmp[1][:]
        for i in range(3):
            cube['R'][i][0] = tmp[2][i]
        cube['D'][0] = tmp[3][::-1]
            

def back(clock=True):
    cube['B'] = rotate(cube['B'], clock)

    last_cube = copy.deepcopy(cube)
    tmp = []
    tmp.append(last_cube['U'][0])
    tmp.append([last_cube['R'][i][2] for i in range(3)])
    tmp.append(last_cube['D'][2])
    tmp.append([last_cube['L'][i][0] for i in range(3)])

    if clock:
        for i in range(3):
            cube['L'][i][0] = tmp[0][2-i]
        cube['U'][0] = tmp[1]
        for i in range(3):
            cube['R'][i][2] = tmp[2][2-i]
        cube['D'][2] = tmp[3]
    else:
        for i in range(3):
            cube['R'][i][2] = tmp[0][i]
        cube['D'][2] = tmp[1][::-1]
        for i in range(3):
            cube['L'][i][0] = tmp[2][i]
        cube['U'][0] = tmp[3][::-1]


def print_cube(side='U'):
    for row in cube[side]:
        print(*row, sep='')

sides = ['U', 'D', 'F', 'L', 'B', 'R']

def oper(op):
    if op == 'L+': left()
    elif op == 'L-': left(False)
    elif op == 'R+': right_()
    elif op == 'R-': right_(False)
    elif op == 'F+': front()
    elif op == 'F-': front(False)
    elif op == 'B+': back()
    elif op == 'B-': back(False)
    elif op == 'U+': up()
    elif op == 'U-': up(False)
    elif op == 'D+': down()
    elif op == 'D-': down(False)

T = int(input())
for tc in range(T):
    cube = {
        'U': [['w' for j in range(3)] for i in range(3)],
        'D': [['y' for j in range(3)] for i in range(3)],
        'F': [['r' for j in range(3)] for i in range(3)],
        'B': [['o' for j in range(3)] for i in range(3)],
        'L': [['g' for j in range(3)] for i in range(3)],
        'R': [['b' for j in range(3)] for i in range(3)],
    }
    n = int(input())
    opers = input().split()
    for op in opers:
        oper(op)
    print_cube()