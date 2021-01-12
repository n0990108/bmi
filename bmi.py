height = input('請輸入身高(公分): ')
weight = input('請輸入體重(公斤): ')
height = float(height)
weight = float(weight)
height = height / 100 #換成公尺
bmi = weight / height / height # 不支援^

if bmi < 18.5:
	print('您的bmi值為', bmi, ',屬體重過輕')
elif bmi >= 18.5 and bmi < 24:
	print('您的bmi值為', bmi, ',屬正常範圍')
elif bmi >= 24 and bmi < 27:
	print('您的bmi值為', bmi, ',屬過重')
elif bmi >= 27 and bmi < 30:
	print('您的bmi值為', bmi, ',屬輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('您的bmi值為', bmi, ',屬中度肥胖')
else: # or elif >= 35: (用else就不能打其他東西)
	print('您的bmi值為', bmi, ',屬重度肥胖')