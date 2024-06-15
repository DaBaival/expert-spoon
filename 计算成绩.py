smax=0
smin=100
count=0
slist=[]

# 循环输入成绩，直到输入空字符串为止
s=input("输入成绩:")
while len(s)>0:
    # 将输入的字符串转换为浮点数
    score=float(s)
    # 将成绩添加到列表中
    slist.append(score)
    # 计数器加1
    count=count+1
    # 更新最大成绩
    if smax<score:
       smax=score
    # 更新最小成绩
    if smin>score:
       smin=score
    # 继续输入成绩
    s=input("输入成绩:")

# 计算平均成绩
savg=sum(slist)/count
print("成绩列表:",slist)
# 输出最大成绩、最小成绩和平均成绩
print('最高分,最低分,平均分 {} {} {:.2f}'\
      .format(smax,smin,savg))
