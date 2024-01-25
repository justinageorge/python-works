# sum=int(input("enter sum"))
# arr=[2,4,5,6,8]
# sorted_arr=sorted(arr)
# low=0
# upp=len(arr)-1
# while(low<upp):
#     currsum=sorted_arr[low]+sorted_arr[upp]
#     if currsum==sum:
#         print(f"pairs {(sorted_arr[low],sorted_arr[upp])}")
#         break
#     elif currsum<sum:
#         low+=1
#     else:
#         upp-=1        

#to search all pairs
sum=int(input("enter sum"))
arr=[2,4,5,6,8]
sorted_arr=sorted(arr)
low=0
upp=len(arr)-1
while(low<upp):
    currsum=sorted_arr[low]+sorted_arr[upp]
    if currsum==sum:
        print(f"pairs {(sorted_arr[low],sorted_arr[upp])}")
        low+=1
        upp-=1
    elif currsum<sum:
        low+=1
    else:
        upp-=1        
