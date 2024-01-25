n1=int(input("enter first number"))
n2=int(input("enter second number"))
# lg_no=n1 if n1>n2 else n2
# hcf=1
# sm_no=n1 if n1<n2 else n2
# for i in range(1,sm_no+1):
#     if n1%i==0 and n2%i==0:
#         hcf=i
#         break
# print(hcf)  
# lcm=n1*n2/hcf      
# print(lcm)
#another method
lcm=1
lg_num=n1 if n1>n2 else n2
for i in range(lg_num,(n1*n2)+1):
    if n1%i==0 and n2%i==0:
        lcm=i
        break
print(lcm)        
