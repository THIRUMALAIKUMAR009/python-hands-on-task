#continue
'''for i in range(1,11):
    if i==5:
        continue
    print(i)'''
#break
'''for i in range(1,11):
    if i==5:
        break
    print(i)'''
'''for i in range(1,11):
    print(i)
else:
    print("else clause is executed")'''
'''lst=[10,30,40,60]
for i in lst:
    if i==40:
        break
    else:
        print('40')'''
#loop
'''for i in range(5):
    print("tool geek")'''
'''for i in range(0,10,2):
    print(i)'''
'''i=0
while i<10:
    print(i)
    i+=1'''
'''a='abcde'
i=0
out=' '
while i<len(a):
    out=a[i]+out
    i+=1
print(out)   '''

'''l=input('enter the character:')
e=' '
i=1
while i<len(l):
    e=e+l[i]
    i+=2
print(e)   '''

'''a='suresh'
out=' '
for i in range (len(a)):
    out=a[i]+out
    i+=1
print(out)  '''





'''for i in range(1,8):
    for j in range(1,6):
        if(j==1 and 2<=i<=6)or(i==1 and 2<=j<=4)or(j==5 and 2<=i<=3):
               print(' * ',end='  ')
        else:
            print('  ',end=' ')
            print()'''

n=int(input("enter the value:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print( ' * ',end=' ')
        else:
            print('  ',end=' ')
print()            
        
























       
    

