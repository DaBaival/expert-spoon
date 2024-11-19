str = input("请输入一串字符串")
count = 0
for s in str:
    if s.isupper():
       count = count+1
print("大写字母个数:", count)