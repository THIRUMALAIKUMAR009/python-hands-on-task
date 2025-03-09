#write a program to print.
'''for i in range(1,6):
    for j in range(1,6):
        print( ' * ',end='')
    print()'''
#wap to print.
'''n=int(input('enter the value:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print(' * ',end='  ')
        else:
            print('   ',end='  ')
    print( ) '''
#3
'''n=int(input('enter the value:'))
for i in range(0,n+1):
    for j in range(1,n+1):
        if i+j==n+1:
            print(' * ',end='  ')
        else:
            print('  ',end='  ')
    print( )'''
#4
'''n=int(input('enter the value:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            print(' * ',end='  ')
        else:
            print('  ',end='  ')
    print( )'''
#5
'''
n=int(input('enter the value:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or i==n or j==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
#6
'''n=int(input('enter the value:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==(n//2)+1 or i==(n//2)+1:
            print(' * ',end='  ')
        else:
            print('   ',end='  ')
    print()'''
#7
'''n=int(input('enter the value:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if  j==(n//2)+1 or i==(n//2)+1 or i==j or i+j==n+1 or i==1 or j==1 or i==n or j==n :
            print(' * ',end='  ')
        else:
            print('   ',end='  ')
    print()'''
'''for i in range(1,6):
    for j in range(1,6):
        if i==1 or j==1 or j==5 or i==5:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print( )'''
#8
'''n=int(input('enter the value:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or j==5 or i==5 or j==(n//2)+1 or i==(n//2)+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print( )'''
#9
'''n=int(input('enter the number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=i:
            print('*',end=' ')
        else:
            print('  ',end='  ')
    print( )'''
#10
'''n=int(input('enter the number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j>=n+1:
            print('*',end=' ')
        else:
            print('  ',end='  ')
    print( )'''
#11
'''n=int(input('enter the number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i<=j:
            print('*',end=' ')
        else:
            print('  ',end='  ')
    print( )'''

#12
'''n=int(input('enter the number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j<=n+1:
            print('*',end=' ')
        else:
            print('  ',end='  ')
    print( )'''
#13
'''n=int(input('enter the number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i==n or j==1:
            print('*',end=' ')
        else:
            print('  ',end='  ')
    print( )'''
#14
'''n=int(input('enter the number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if  i==n or i+j==n+1 or j==n:
            print(' * ',end='  ')
        else:
            print('   ',end='  ')
    print( )'''
#15
'''n=int(input('enter the number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i+j==n+1 or j==1:
            print(' * ',end='  ')
        else:
            print('  ',end='  ')
    print( )'''
#16
'''n=int(input('enter the number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==j or j==n:
            print(' * ',end='   ')
        else:
            print('   ',end='   ')
    print( )'''
#17



