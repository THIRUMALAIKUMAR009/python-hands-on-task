'''i=1
while i<=10:
    print(i)
    i+=1'''
'''i=1
while i<=5:
    print('python')
    i+=1'''
'''l=eval(input("enter the value:"))
out=[]
i=0
while i<len(l):
    if type(l[i])==int:
        out.append((l[i])
    i+=1'''
'''a='abcde'
i=o
out=''
while i<len(a):
    i+=1'''

''''a=135
out=0
while a!=0:
    ld=a%10
    out=(out *10)+ld
    a=a//10
    print(out)'''
 
'''a=123
rev=0
while a!=0:
  ld=a%10
  rev=(rev*10)+ld
  a=a//10
  print(rev)'''

'''for i in range(1,11):
    print(i,"x2=",i*2)'''

'''n=int(input("enter the value:"))
i=1
while i<=10:
    print(f'{n}*{i}={n*i}')
    i+=1'''

'''l=input("enter the character:")
e=' '
i=1
while i<len(l):
    e=e+l[i]
    i+=2
print(e)'''

'''l=input("enter the character:")
e=''
i=0
while i<len(l):
    e=e+l[i]
    i+=2
print(e)'''

'''l=input("enter the character:")
s=' '
i=0
while i<len(l):
    if 'a'<=l[i]<='z':
        s=s+l[i]
    i=i+l
print(s) '''
'''n=int(input('enter the value:'))
fact=1
i=1
while i<=n:
    fact=fact*i
    i+=1
print(fact) '''

'''a=0
while a<5:
    print("python")
    a+=1'''
''''n=int(input('enter a number:'))
i=1
while i<=n:
    print(i,end=" ")
    i+=1'''
'''n=int(input("enter the number:"))
i=1
while i<10:
    print(f"{n}*{i}={n*i}")
    i+=1'''
'''n=int(input("enter a number:"))
sum_n=0
i=1
while i<=n:
    sum_n+=i
    i+=i
print(f"the sum of{n} natural numberis:{sum_n}") '''
'''n=int(input("enter a number:"))
factorial=1
i=1
while i<=n:
    factorial*=i
    i+=1
print(f"the factorial of {n}is:{factorial}")    '''

'''string=input("enter a string:")
i=0
while i<len(string):
    print(string[i])
    i+=1'''
'''string=input("enter the string:")
i=0
lowercase_chars=" "
while i<len(string):
    if string[i].islower():
        lowercase_chars+=string[i]
        i+=1
print("lowercase characters:",lowercase_chars)'''
'''string=input("enter a string:")
i=0
vowels="aeiouAEIOU"
extracted_vowels=""
while i<len(string):
    if string[i] in vowels:
         extracted_vowels+=string[i]
         i+=1
print("vowels:", extracted_vowels) '''
'''n=int(input("enter a number:"))
i=1
while i<=n:
    if n%i==0:
        print(i)
        i+=1'''
'''num=int(input("enter the number:"))
i=1
factorial_sum = 0
while i<n:
    if n % i == 0:
        factors_sum+=i
    i+=1
if factors_sum == n:
    print(f"{n}is a perfect number.")
else:
    print(f"{n}is not a perfect number.")'''
'''correct_otp="12345"
attempts=0
while attempts <3:
    otp =input("enter otp: ")
    if otp == correct_otp:
        print("login successful!")
        break
    else:
        print("incorrect otp .")
    attempts +=1
if attempts==3:
    print("failed to login after 3 attempts.")'''
'''correct_password="password123"
while True:
    password=input("enter password:")
    if password==correct_password:
        print("access granted.")
    else:
        print("incorrect password. try again.")'''

'''#wap to find the sum of cube of a num
a=input('enter the value:')
sum=0
i=0
while i<len(a):
    if '0'<=a[i]<='9':
        sum=sum+int(a[i])**3
        i+=1
print(sum)'''        

'''num=int(input("enter a number:"))
digits=[int(digit) for digit in str(num)]
sum_cubes=sum(d**3 for d in digits)
if sum_cubes==num:
    print(f"{num} is an amstrong number.")
else:
    print(f"{num} is not a amstrong number.")'''

'''A="10011100"
B="00110101"
count=0
for a, b in zip(A, B):
    if a == b:
        count +=1
print("count of positions having the same values:",count)'''

'''a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
while b:
    a,b=b, a % b
print("HCF is:",a) '''

'''string=input("enter a string:")
word_count=len(string.split())
print(f"the number of words in the string is:{word_count}")'''

'''set1={1,2,3,4,5}
set2={4,5,6,7,8}
common_elements=set1 &set2
print("common element:", common_elements)'''
'''num=input("enter the number:")
product=1
for digit in num:
    product *=int(digit)
print(f"the product of the digitnin {num}is :{product}")'''

'''#wap to toggle a string
a=input("enter the string:")
out=''
i=0
while i<len(a):
    if 'A' <=a[i]<='Z':
        out=out+(chr(ord(a[i])+32))
    elif 'a'<=a[i]<='z':
        out=out+(chr(ord(a[i])-32))
    else:
         out=out+a[i]
    i+=1
print(out) '''
'''a=int(input('enter the number:'))
sumofdivisor=0
temp=a
i=1
while i<=a//2:
    if a%i==0:
        sumofdivisor+=i
    i+=1
if sumofdivisor==temp:
    print(f'{a}is a perfect number')
else:
    print(f'{a}is not a perfect number')'''
'''#wap to remove duplicates from a list without converting into set
l=[1,2,3,4,5,5,6,7,7]
out=[]
i=0
while i<len(l):
    if l[i] not in out:
        out.append(l[i])
    i+=1
print(out)'''    
#wap to guess the number.


        
        

    



