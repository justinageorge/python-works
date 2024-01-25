weight_in_kg=78
height_in_cm=165
height_in_m=height_in_cm/100
bmi=(weight_in_kg)/(height_in_m**2)
print(bmi)
if (bmi<20):
    print("underweight")
elif(bmi>=20 and bmi<25):
    print("normal weight")   
elif(bmi>=20 and bmi<30):
    print("overweight")     
else:
    print("obesity")    
