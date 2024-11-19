n = int(input("正整数n(n>=2):"))
i = 2
while i <= int(n/2):
   if n % i == 0:
      print(n,"不是素数")
      break
   i = i+1
else:
   print(n,"是素数")