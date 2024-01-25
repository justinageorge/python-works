gender="male"
tummy_size=34
buttock_size=68
value=tummy_size/buttock_size
print(value)
if(gender=="male"):
    if (value<0.95):
        print("low")
    elif(value>=0.95 and value<1):
        print("moderate")
    else:
        print("high")    
elif(gender=="female"):
    if(value<0.80):
        print("low")            
    elif(value>=0.80 and value<=0.85):
        print("moderate")
    else:
        print("high")    