# sequence of characters
# methods-those are inside the class they are methods
# those are defined in the class are called fuctions
name="luminar"
# print(name.casefold())
# # change all letter to LOWERCASE letter
# name1='JAVA'
# print(name1.casefold())
# # objectname.methodname
# print(name.capitalize())#convert only first character to uppercase
# print(name.count('a'))

# print(name.startswith("lu"))
# print(name.endswith('lab'))
# print(name.casefold().count('l'))
# print(name.isalpha())#check whether name has only alphabets
# java="hi123"
# print(java.isdigit())#check whether given name has only number
# print(java.isalnum())#alpha numeric
# name="hello goodmorning all"
# words=name.split(" ")
# print(words)
name="hello,good,morning,all"
words=name.split(',')
print(words)
for w in words:
    print(w)