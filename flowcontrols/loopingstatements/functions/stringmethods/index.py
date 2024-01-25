# word="hello"
# print(word.index('l'))
# print(word[0])
# word="hello"
# count=len(word)   
# # for i in range(0,count):
# #     print(word[i])

# for i in range(count-1,-1 ,-1) :
#     print(word[i])   

#or
word="hello"
count=len(word)
p_str=""
for i in range(count-1,-1,-1):
    p_str+=word[i]
print(p_str)    