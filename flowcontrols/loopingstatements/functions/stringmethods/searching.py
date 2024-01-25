lst=[10,12,14,11,15]
element=int(input("enter a number"))
is_present=False
for i in range(0, len(lst)):
    if(element==lst[i]):
        is_present=True
        break
print(is_present)    