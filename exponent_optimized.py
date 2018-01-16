import math
x=input()          # the base needs to be a 3 digit number atleast
y=input()
if x=='1' or x=='0':
    print (x)
elif y=='1':
    print(x)
elif y=='0':
    print("1")
else:
    inter1=float(y)*(len(x)-1+math.log10(float(x[0]+"."+x[1]+x[2])))
    print(inter1)
    if inter1>0:
        power=math.floor(inter1)
        mantissa=inter1-power
        answer=str(10**mantissa)+"*10^"+str(power)
    elif inter1<0:
        power=math.floor(inter1)
        print(power)
        mantissa=inter1-power
        answer=str(10**mantissa)+"*10^"+str(power)        

    print(answer)
