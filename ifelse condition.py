#wap to check whether the given value is mutable data type or not.
'''a=eval(input("enter the value:"))
if type(a) in[list,set,dict]:
    print('yes the given value is mutable')
else:
    print('the give value is immutable')'''
#wap to check whether the given number is even(or)odd.
'''a=int(input("enter the number:"))
if a%2==0:
    print("the given value is even")
else:
    print("the given value is odd")'''
#wap to check whether the given character is uppercase (or) not .if it is a uppercase print ascii value.else print character.
'''char=input("enter the character:")
if 'A'<=char<='Z':
    print(ord(char))
else:
    print(char)'''
#wap to check wheather the given number is positive (or)negative.5
'''a=int(input("enter the number:"))
if a>=0:
    print("the given value is positive")
else:
    print("the given value is negative")'''
#wap to check wheather the given character is special char or not.
'''a=input("enter the value:")
if('a'<=a<='z') or('A'<=a<='Z') or ('0'<=a<='9'):
    print('it is not a special character')
else:
    print('it is a special character')'''
#wap to consider two inputs.the two value are pointing to some memory location (or)not.
'''a=eval(input("enter the value:"))
b=eval(input("enter the value:"))
if id(a)==id(b):
    print("the value is in same memory location")
else:
    print("the value is not in same memory location")'''
#wap to check whether a list consists of middle value or not.
'''a=eval(input("enter the value:"))
if len (a)%2==1:
    print("the value consists of middle value")
else:
    print("the value not consists if middle value")'''

#wap to check whether the string is palindrome or not.
a=input("enter the value:")
if a==a[::-1]:
    print("it is a palindrome")
else:
    print("it is a not palindrome")
    















    
