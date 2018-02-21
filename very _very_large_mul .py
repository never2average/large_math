x=list(map(int, input()))
y=list(map(int, input()))
"""
This algorithm works on the basis of the multiplication of very very large numbers by converting them to lists
and applying the school multiplication methods.
"""
x.reverse()
y.reverse()
n=len(x)
m=len(y)
z=[0]*(m+n+1)
for i in range(m):
    for j in range(n):
        temp=x[j]*y[i]
        if temp<10:
            z[j+i]+=temp
        else:
            z[j+i]+=temp%10
            z[j+i+1]+=(temp//10)
    for k in range(m+n+1):
        if z[k]>=10:
            z[k+1]+=(z[k]//10)
            z[k]=(z[k]%10)
    
z.reverse()
Str=''
for I in range(m+n+1):
    if z[I]!=0:
        for J in range(I,m+n+1):
            Str+=str(z[J])
        break
print(Str)
