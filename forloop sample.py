'''user_name="arun"
while True:
    un=input("enter the user_name:")
    if un==user_name:
        print('valid user_name:')
        break'''

'''import random
a=random.randint(1,100)
print(a)'''

'''a='abcdef'
for i in a:
    if 'A'<=i<='Z':
        print('it doesnt contain only lower case')
        break
else:
    print('it contains only lower case')'''

'''l=eval (input('enter the value:'))
for i in range(0,len(l)):
    if type(l[0])!=type(l[i]):
            print('hetrogeneous')
            break
else:
    print('homogeneous')'''
'''----------------------------------------'''
'''#85
S="banana"
char='a'
count=S.count(char)
print(count)'''

'''#88
s="Power Star"
result=s.swapcase()
print(result)'''

'''#94
s="hello"
result=s[::-1]
print(result)'''

'''#77
a=int(input("enter the value:"))
b=str(a)
for i in b:
    l=int(i)
if l%2==0:
    print('even')
else:
    print('odd')'''

'''#78
a={'a':1,'b':2,'c':3}
for i in a:
    value=a[i]
    if type(i)==str and type(value)==int:
print(i,value)'''

'''#79
d={'a':1,'b':2,'c':3}
for i in d:
    value=d[i]
    if i==value:
print(i,value)'''

'''#82
a=[0, { },' ',1,4,'sd']
b=[]
for i in a:
    if i not in [0,False,' ',0.0,{ }]:
        b.append(i)
print(b)'''      
    

