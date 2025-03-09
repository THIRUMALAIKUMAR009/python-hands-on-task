#wap to check whether the give number is strong or not:
'''def  factorial(ld):
    fact=1
    i=1
    while i<ld:
        fact=fact*i
        i+=1
    return fact
def st(n):
    temp=n
    sum=0
    while n!=0:
        ld=n%10
        sum+=factorial(ld)
        n//=10
    if sum==temp:
        print('it is a strong number')
    else:
       print('it is not a strong number')
st(int(input('enter the value:')))   '''    
#sample amstrong number.
num=int(input('enter the value:'))
temp=0
sum=num
while i> temp:
    digit=temp%10
    sum+= digit**3
    temp//=10
if num==temp:
    print('it is a amstrong number:')
else:
    print('it is not a amstrong number:')
        







        
