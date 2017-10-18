#根据身高体重判断BMI(肥胖)值
#BMI值计算公式: 
#    BMI = 体重(公斤) / 身高2(公尺2)

#例如：一个52公斤的人，身高是155公分，则BMI为 :

#    52(公斤)/1.552 ( 公尺2 )= 21.6

#体重正常范围为  BMI=18.5～24 
height=float(input('请输入你的身高（米）：'))
weight=float(input('请输入你的体重（千克）：'))
h=float(height)
w=float(weight)
bmi=w/(h**2)
print('您的BMI指数为：''%.2f%%'%bmi )
if bmi<18.5 :
    print ('您的体重过轻')
elif bmi >18.5 and bmi <25 :
     print ('您的体重正常')
elif bmi >25 and bmi <28:
	 print ('您的体重过重')
elif bmi >28 and bmi <32 :
    print ('您的体重肥胖') 
else:
    print ('您的体重严重肥胖')
