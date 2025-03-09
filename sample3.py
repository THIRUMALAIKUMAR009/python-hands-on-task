#wap to print ascil value of a character only if it is uppercsae:
'''char=input("enter the character:")
if 'A'<=char<='Z':
    print(ord(char))'''
#wap to print the cube of  a number only if it is divisible by 9 or 6.
'''a=int(input("enter the value:"));
if a%9==0 or a%6==0:
    print(f"the cube of{a} is {a**3}.")
else :
     print(f"the cube of{a}not is {a**3}.")'''
#wap to check whether the give integer is 3 digit number.
'''
a=int(input("enter the number:"))
if a>=100 and a<=999:
    print('the given number is 3 digit')
    

a=int(input('enter the value'))
b=str(a)
if len(b)==3:
    print('the given number is 3 digits')
'''
#wap to check whether the last digit of a number is 5.
'''a=int(input("enter the number:"))
b=str(a)
if b[-1]=='5':
    print("yes the last digit of number is five")'''
#wap to check whether the given data is float.
'''a=eval(input("enter the value:"))
if type(a)==float :
    print("yes the given data is float")'''
#wap to check whether the data is single value data.
'''a=input("enter the value:")
if len(a)==1:
    print(f"{a} is a single value data")
else:
    print(f"{a}is not a single value data")'''
#wap to check whether the given character is digit or not.
'''a=input("enter the value:")
if a.isdigit():
    print(f"{a} is a digit")
else:
    print(f"{a}is not a digit")'''
#wap to check whether the given integer is multiple of 3.
a=int(input("enter the number:"))
if a%3==0:
    print(f"the {a} is multiple by 3")
else:
    print(f"the {a} is not multiple by 3")


























