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
    inter1=float(y)*(len(x)-1+math.log(float(x[0]+"."+x[1]+x[2])))
    if inter1>0:
        power=math.floor(inter1)
        mantissa=power-inter1
        answer=str(math.exp(mantissa))+"e^"+str(power)
    elif inter1<0:
        power=math.ceil(inter1)-1
        mantissa=inter1-power
        answer=str(math.exp(mantissa))+"e^"+str(power)        

    print(answer)
