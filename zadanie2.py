print("Maximize")
f = True
n = 10
for x in range(ord('a'), ord('a') + n):
    for y in range(1, n + 1):
        if f:
            f = False
        else:
            print('+', end='')
        print(chr(x) + str(y), end='')
print()
print()
print("Subject To")
print()

for x in range(ord('a'), ord('a') + n):
    f = True;
    for y in range(1, n + 1):
        if f:
            f = False
        else:
            print('+', end='')
        print(chr(x) + str(y), end='')
    print("<=1")

print()

for y in range(1, n + 1):
    f = True
    for x in range(ord('a'), ord('a') + n):
        if f:
            f = False
        else:
            print('+', end='')
        print(chr(x) + str(y), end='')
    print("<=1")

print()

for x in range(0, n-2):                                                   #najpierw po pierwszej kolumnie bez najdłuzszej przekatnek
    f = True
    for y in range (0, x+2):
        if f:
            f = False
        else:
            print('+', end='')
        print(chr(ord('a')+y) + str(n-1-x+y), end='')
    print("<=1")

for x in range(0, n-1):                                               #po pierwszym wierszu
    f = True
    for y in range(0, n-x):
        if f:
            f = False
        else:
            print('+', end='')
        print(chr(ord('a') + x + y ) + str(1+y), end='')
    print("<=1")
print()
print()
print()


for x in range(0, n-2):                                                   #najpierw po pierwszej kolumnie bez najdłuzszej przekatnek w dol
    f = True
    for y in range (0, x+2):
        if f:
            f = False
        else:
            print('+', end='')
        print(chr(ord('a')+y) + str(2+x-y), end='')
    print("<=1")


for x in range(0, n-1):
    f = True
    for y in range(0, n-x):
        if f:
            f = False
        else:
            print('+', end='')
        print(chr(ord('a') + x + y) + str(n-y), end='')
    print("<=1")
print()

print("Bounds")
print()
for x in range(ord('a'), ord('a') + n):
    for y in range(1, n + 1):
        print("0<=" + chr(x) + str(y) + "<=1", end=' ')

print()
print("Generals")
for x in range(ord('a'), ord('a') + n):
    for y in range(1, n + 1):
        print(chr(x) + str(y), end=' ')
print()
print("End")
