#1
'''n=int(input('enter the value:'))
for i in range(1,n+1):
    for j in range(n-i):
        print('  ',end='  ')
    for j in range(i):
        print(' * ',end='   ')
    print()
for k in range(1,n+1):
    for l in range(k):
        print('   ',end=' ')
    for m in range(n-k):
         print(' * ',end='  ')
    print()  '''
#2
'''n=int(input('enter the value:'))
for i in range(1,n+1):
    for j in range(n-i):
        print('  ',end='  ')
    for j in range(i):
        print(' * ',end='   ')
    print()'''

#3
'''n=eval(input('enter the character:'))
for i in range(n,n+1):
    for j in range(1,n+1):
       if i+j==n+1 or i==n or j-1==n-i:
           print()'''
#task wap to print all characters .[A-Z &0-9]
#task wap to print your name.
#G
'''for i in range(1,8):
    for j in range(1,6):
        if(j==1 and 2<=i<=6)or(i==1 and 2<=j<=4)or(j==5 and 2<=i<=3):
               print(' * ',end='  ')
        else:
            print('  ',end=' ')
            print() '''


 
#1
for i in range(1,4):
    for j in range(1,4):
        print(j,end=' ')
    print()
#2
for i in range(1,4):
    for j in range(1,4):
        print(i,end=' ')
    print()
#3
for i in range(1,6):
    k=1+i-1
    for j in range(1,6):
        if  j<=i:
            print(k,end=' ')
        else:
            print('   ',end='  ')
        k+=1
    print()  
#4
for i in range(1,6):
    n=1
    for j in range(1,6):
        if j<=i:
            print(n,end=' ')
        else:
            print(' ',end=' ')
        n+=1
    print()
#6
for i in range(1,6):
    n=2
    for j in range(1,6):
        if j<=i:
            print(n,end=' ')
        else:
            print(' ',end=' ')
        n+=1
    print()
#7
for i in range(1,6):
    n=ord('A')
    for j in range(1,6):
        if j<=i:
            print(chr(n),end=' ')
        else:
            print(' ',end=' ')
        n+=1
    print()
#8
for i in range(1,6):
    n=1
    for j in range(1,6):
        if i<=j:
            print(n,end=' ')
        else:
            print(' ',end=' ')
        n+=1
    print()
#9
for i in range(1,6):
    n=1
    for j in range(1,6):
        if i<=j:
            print(n**2,end=' ')
        else:
            print(' ',end=' ')
        n+=1
    print()
#10
for i in range(1,6):
    n=ord('m')
    for j in range(1,6):
        if j<=i:
            print(chr(n),end=' ')
        else:
            print(' ',end=' ')
        n+=1
    print()
#11
for i in range(1,6):
    n=1+i-1
    for j in range(1,6):
        if j<=i:
            if i%2==0:
                print(n**2,end=' ')
            else:
                print(n,end=' ')
        else: 
           print(' ',end=' ')
        n+=1
    print()










