import math
a=int(input("输S1:"))
b=int(input("输S2:"))
c=int(input("输S3:"))
p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
s=round(s,2)
print("S1a="+str(a)+"S2b="+str(b)+"C3="+str(c)+"F"+str(s))