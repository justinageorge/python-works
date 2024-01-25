lst1=[10,13,15,20,25]
lst2=[12,13,20,25,30]
lst_1=sorted(lst1)
lst_2=sorted(lst2)
i=0
j=0
while(i<len(lst_1)) and j<len(lst_2):
        if (lst_1[i]==lst_1[j]):
            print(lst_1[i],"common")
            
            i+=1
            j+=1
        elif (lst_1[i]<lst_2[j]):
            i+=1
        else:
            j+=1

        
