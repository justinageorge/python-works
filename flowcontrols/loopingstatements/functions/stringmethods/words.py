text="Your code is designed to split the given text into words and then print any word that "
vowels='a','e','i','o','u'
v_count=0
c_count=0
for ch in text:
    if ch in vowels:
        v_count+=1
    elif ch.isalpha():
        c_count+=1    
print(f"total number of characters{len(text)}")   
print(f"total no of vowels={v_count}")   
print(f"total no of consonants={c_count}")  