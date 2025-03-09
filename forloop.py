'''a='vishwanath'
for i in a:
    print(i,end=" ")'''
'''#1
input_string=input()
total_sum=0
for char in input_string:
    if'0'<=char<='9':
        digit = int(char)
        total_sum+=digit ** 3
print(f"the sum of the cubes of the digits in'{input_string}' is:{total_sum}")'''

'''l="suresh"
out=''
for i in range(len(l) -1,-1,-1):
    out+=l[i]
print(out)'''    

'''s1="1110011001"
s2="1100010001"
count=0
if len(s1)==len(s2):
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            count=count+1
print(count) '''       


'''a='power star'
out={}
for i in a.split():
    out[i]=len(i)
print(out)'''

'''a='push maadi kusi padi'
out={}
for i in a.split():
    if len(i)%2==0:
        out[i]=i[0]+i[-1]
    else:
        out[i]=i[len(i)//2]
print(out)  '''

'''l=eval(input ("enter the dictionary:"))
out={}
for i in l:
       if type(i)==str:
           if type(l[i])==int:
               out[i]=l[i]
print(out)''' 

'''a=input('enter the string:')
b=input('enter the specified character:')
count=0
for i in a:
    if i==b:
        count+=1
print(count) '''

'''l=('enter the str')
m=' '
s=' '
d=' '
sp=' '
for i in l:
    is 'A'<=s<='Z':
        m=m+s
        elif 'a' <=s='z':
            m=m+s
            elif '0' <=s ='9'
            d=d+m
            else:
                sp=sp+m
                print('the uppercase char:'m)
                print('the lowercase char: 'l)
                print('the digit char: 'd)
                print('the special char: 'sp)'''
       
'''a=12345
b=a%10
if b%2==0:
    print('last digit is even')
else:
    print('last digit is odd')'''

'''l=[1,2,3,4,5,5,6,7,7]
b=list(set(l))
print(b)'''

s=['jiocinema.com','file.py','web.html','amazon.com','www.org']
out=[]
for file in s:
    a=file.split('.')[-1]
    if a not in out:
         out.append(a)
print(out)   
   
   
   













   
