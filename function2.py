'''def con(s):
    count=0
    for i in s:
        if 'A'<=i<='Z':
            count+=1
    return count
print(con(input('enter the value:')))'''
#2
'''def aru(a):
    b=len(a)//2
    return a[b]
c=eval(input())
print(aru(c))'''
#3
'''def d(s):
    out=[]
    for i in range(0,len(s)):
     if type (s[i])==str and i%2==0:
        out.append(s[i])
    return out
print(d(eval (input('enter the list:'))))'''

'''#4
def f(n):
    fact=1
    i=1
    while i<=n:
        fact=fact*i
        i+=1
        return fact
    print(f(int(input('enter the number:'))))'''

#5
'''def s(k):
    rev=" "
    for i in k:
        rev=i+rev
    return rev    
print(s(input('enter the value:')))'''
#6
'''def python(s):
    a=s.split()
    out={}
    for i in a:
        if len(i)%2==0:
            out[i]=[i[0],i[-1]]
        elif len(i)%2!=0:
            out[i]=i[::-1]
    return out
print(python(input("enter the value:")))'''


