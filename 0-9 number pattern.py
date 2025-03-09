# 0
for i in range(1, 10):
    for j in range(1, 8):
        if (i == 1 and j > 1 and j < 7) or (i == 9 and j > 1 and j < 7) or (j == 1 and i > 1 and i < 9) or (j == 7 and i > 1 and i < 9):
            print('°', end='')
        else:
            print(' ', end='')
    print()
print('--------------------------------0--------------------------------')

# 1
for i in range(1, 10):
    for j in range(1, 8):
        if (j == 4) or (i == 9) or (i == 1 and j == 3):
            print('°', end='')
        else:
            print(' ', end='')
    print()
print('--------------------------------1--------------------------------')

# 2
for i in range(1, 10):
    for j in range(1, 8):
        if (i == 1 and j > 1) or (i == 5 and j > 1 and j < 7) or (i == 9 and j < 7) or (j == 7 and i > 1 and i < 5) or (j == 1 and i > 5 and i < 9):
            print('°', end='')
        else:
            print(' ', end='')
    print()
print('--------------------------------2--------------------------------')

# 3
for i in range(1, 10):
    for j in range(1, 8):
        if (i == 1 and j > 1) or (i == 5 and j > 1 and j < 7) or (i == 9 and j > 1) or (j == 7 and i > 1 and i < 9):
            print('°', end='')
        else:
            print(' ', end='')
    print()
print('--------------------------------3--------------------------------')

# 4
for i in range(1, 10):
    for j in range(1, 8):
        if (j == 7) or (i == 5) or (j == 1 and i < 5):
            print('°', end='')
        else:
            print(' ', end='')
    print()
print('--------------------------------4--------------------------------')

# 5
for i in range(1, 10):
    for j in range(1, 8):
        if (i == 1 and j > 1) or (i == 5 and j > 1 and j < 7) or (i == 9 and j < 7) or (j == 1 and i > 1 and i < 5) or (j == 7 and i > 5 and i < 9):
            print('°', end='')
        else:
            print(' ', end='')
    print()
print('--------------------------------5--------------------------------')

# 6
for i in range(1, 10):
    for j in range(1, 8):
        if (i == 1 and j > 1) or (i == 5 and j > 1 and j < 7) or (i == 9 and j > 1) or (j == 1 and i > 1 and i < 9) or (j == 7 and i > 5 and i < 9):
            print('°', end='')
        else:
            print(' ', end='')
    print()
print('--------------------------------6--------------------------------')

# 7
for i in range(1, 9):
    for j in range(1, 9):
        if (i == 1) or (i+j==9):
            print('°', end='')
        else:
            print(' ', end='')
    print()
print('--------------------------------7--------------------------------')

# 8
for i in range(1, 10):
    for j in range(1, 8):
        if (i == 1 and j > 1 and j < 7) or (i == 5 and j > 1 and j < 7) or (i == 9 and j > 1 and j < 7) or (j == 1 and i > 1 and i < 9) or (j == 7 and i > 1 and i < 9):
            print('°', end='')
        else:
            print(' ', end='')
    print()
print(' --------------------------------8--------------------------------')

# 9
for i in range(1, 10):
    for j in range(1, 8):
        if (i == 1 and j > 1 and j < 7) or (i == 5 and j > 1 and j < 7) or (i == 9 and j > 1 and j < 7) or (j == 7 and i > 1 and i < 9) or (j == 1 and i > 1 and i < 5):
            print('°', end='')
        else:
            print(' ', end='')
    print()
print('--------------------------------9--------------------------------')
