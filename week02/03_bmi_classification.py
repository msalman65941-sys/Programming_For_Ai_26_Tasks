weight=float(input("Enter Wieght in Kilograms: "))
height=float(input("Enter Height in Metres: "))

bmi=(weight/height)**2
if(bmi<18.5):
    status="Underweight"
elif(bmi<25):
    status="Normal"
elif(bmi<30):
    status="Overweight"
else:
    status="Obese"

print(status)