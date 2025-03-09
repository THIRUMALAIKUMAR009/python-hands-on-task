''''l=eval(input("enter the list:"))
if len(l)%2==1:
    if type(l[len(l)//2])==str:
        print(l[len(l)//2])
    else:
        print('middle value is not a string')
else:
    print('list is not having middle value')'''''
#wap to check whether the charcter is vowel or consonant
'''a=input("enter the character:")
if 'a'<=a<='z' or 'A'<=a<='Z':
    if a in['A','a','E','e','I','i','O','o','U','u']:
        print("It is a vowels")
    else:
        print("it is a consonant")
else:
    print("it is not a  alphabet")'''
#wap to find the greatest of 4 number.
'''a=int(input("enter the value:"))
b=int(input("enter the value:"))
c=int(input("enter the value:"))
d=int(input("enter the value:"))
if a>b:
    if a>c:
        if a>d:
            print(" this is greater :",a)
        else:
           print("this is greater:",d)
    else:
        if c>d:
            print("this is greater:",c)
        else:
            print("this is greater:",d)
else:
    if b>c:
        if b>d:
            print("this is greater:",b)
    else:
        if c>d:
            print("this is greater:",c)
        else:
            print("this is greater:",d)'''
#wap to print the value as it is only if the length of the value is even.
'''a=eval(input("enter the number:"))
if type(a)not in[int,float,complex]:
     if len(a)%2==0:
         print(a)
     else:
         print(" odd")
else:
    print("it is not a collection")'''
#wap to print the last value of a list only if it is palindrome string starting with vowels.
a=eval(input("ENTER THE VALUE:"))
if a[0] in ['A','a','E','e','I','i','O','o','U','u']:
    if a[len(a)-1]not in ['A','a','E','e','I','i','O','o','U','u']:
        if len(a)%2!=0:
            print(a[::-1])
        else:
            print("no middle value")
    else:
        print("not ending with consonent")
else:
    print("not starting with vowels")

#find the second smallest of 4 numbers
    number=int(input("enter the value:"))
    
        
