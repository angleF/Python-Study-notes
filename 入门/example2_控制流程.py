# 编写一个程序，获取一个用户输入的整数，然后通过程序显示这个数是奇数还是偶数
# input_str=input("请输入一个整数：")
# to_int=int(input_str)
# if to_int % 2 ==0 :
# 	print("这是一个偶数：",to_int)
# else:
# 	print("这是一个奇数:",to_int)

# 编写一个程序，检查任意一个年份是否是闰年，如果一个年份可以被4整除不能被100整除，或者可以被400整除，这个年份就是闰年
# year=2016
# if (year % 4 ==0 and year % 100 !=0 ) or year % 400 ==0 :
# 	print("闰年")
# else:
# 	print("平年")

# 从键盘输入一个分数，等于100，奖励一辆BMW,80-99,奖励一台iPhone,60-79,奖励一本参考书，其他的，什么都没有

# score_input=input("输入分数：")
# score_int=int(score_input)
# if score_int==100:
# 	print("奖励一辆BMW")
# elif score_int>=80 and score_int<=99 :
# 	print("奖励一台iPhone")
# elif score_int>=60 and score_int<=79:
# 	print("奖励一本参考书")
# else:
# 	print("还需努力")

# 求100以内所有奇数之和
# sum_=0
# i=0
# while i<100:
# 	if i%2!=0 :
# 		sum_+=i
# 	i+=1
# print(sum_)
# 求100以内所有7的倍数之和，以及个数
# sum_=0
# count_sum=0
# i=0
# while i<100:
# 	if i%7==0:
# 		count_sum+=1
# 		sum_+=i
# 	i+=1
# print("个数：",count_sum,"，和：",sum_)

# 打印乘法表
i = 1;
while i < 10:
    j = 1
    while j < 10:
        if j > i: break
        print(str(i), "*", str(j), "=", str((i * j)), end="	")
        j += 1
    print()
    i += 1
