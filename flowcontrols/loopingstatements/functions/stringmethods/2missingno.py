# when only one number is missing
# lst=[1,2,4,5,6]
# max_no=max(lst)
# total_sum=max_no*(max_no+1)/2
# cur_sum=sum(lst)
# diff=total_sum-cur_sum
# if diff==0:
#     print(f"{max_no+1} is missing")
# else:
#     print(f"{diff} is missing")    


#when 2 number is missing
lst=[1,2,3,5,6]
limit=len(lst)-1
i=0
while(i<limit):
    j=i+1
    diff=lst[j]-lst[i]
    if(diff==1):
        i+=1
    else:
        print(lst[i]+1 ,"is missing")   
        break 
    
