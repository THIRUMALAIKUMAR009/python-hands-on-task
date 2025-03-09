'''for i in range(1,21):
    if i%2==1:
        continue
    else:
        print(i)'''

'''a='abcdef'
b='fdacbe'
count=0
for i in range(0,len(a)):
    if a[i]==b[i]:
        continue
    else:
        count+=1
print(count)
(or)
a='abcdef'
b='fdacbe'
count=0
i=0
while i<len[a]:
    if a[i]==b[i]:
        i+=1
        continue
    else:
        count+=1
        i+=1
print(count) '''       

'''s='python is easy'
out={}
for i in s.split():
    count=0
    for j in i:
       # print(j)
       if j in 'aeiouAEIOU':
        count+=1
        #print(count)
        #print(j)
    out[i]=[i[::-1],count,i[::2]]
    print(out)'''

'''l=[100,200,35,40,60]
out=[]

for i in l:
    sum=0
    for j in l:
        sum+=j
        out.append(sum-i)
print(out)'''
'''# wap to get the following output,without length function.
s='power star'
out={}
count=0
for i in s.split( ):
    count=0
    for j in i:
        count+=1
    out[i]=count
print(out)    '''
'''#wap to get the following output
s='power star'
out={}
for i in s.split():
    count=0
    for j in i:
        if j in 'aeiouAEIOU':
            count+=1
            out[i]=  count
print(out)'''

'''#wap to get the following output.
s='kabab is love'
out={}
for i in s.split():
    count=0
    a=''
    for j in i:
        if j in i:
            if j not in 'aeiouAEIOU':
                count+=1
                a=a+j
            out[i[0]+i[-1]]=[a,count,a[::-1]]
print(out)      '''

a='bacbcaabbaa'
out=[]
for i in a:
    if a[i]==len(str):
        count=0
        out=a+a[i]
        count+=1
print(out)        
        
        

      

    
        
        
    
