# bmi=weight/ hight*hight
weight = input("what is your weight?")
weight_number = float(weight)
hight = input("what is your hight?")
hight_number = float(hight)
bmi = weight_number / (hight_number * hight_number)
# hight_number**2
print(bmi)
if bmi < 18:
    print("underweight")
elif 18 <= bmi < 25:
    print("normal")
elif 25 <= bmi < 30:
    print("over weight")
else:
    print("obese")
