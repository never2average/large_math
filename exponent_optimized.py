import math

x=input()
n=len(str(int(float(x))))
y=input()

if x=='1' or x=='0':
    print (x)
elif y=='1':
    print(x)
elif y=='0':
    print("1")
else:
    if n>=3:
       a=float(x[0]+"."+x[1]+x[2])
    elif n==2:
       a=float(x[0]+"."+x[1]+"0")
    elif n==1:
       a=float(x[0]+".00")

    inter1=float(y)*(n-1+math.log10(a))
    power=math.floor(inter1)
    mantissa=inter1-power
    answer=str(10**mantissa)+"*10^"+str(power) 
    print(answer)

"""
This program has been created in order to 
calculate very very large exponentials
and has a time complexity o(1).
I have used the lpgarithmic approach for 
the process and instead of finding the antilog 
of the whole number i have divided it into mantissa
and power in order to only find antilog of mantissa
and therefore draatically cutting down operations.
"""