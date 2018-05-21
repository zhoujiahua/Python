print("请输入内容")
temp =  input()
guess = int(temp)
while guess != 8:
	temp = input("输错了，请输入内容")
	guess = int(temp)
	if guess == 8:
		print("你真聪明")
		print("但是没有奖励")
	else:
		if guess > 8:
			print("输入大了")
		else:
			print("输入小了")
print("游戏结束")
