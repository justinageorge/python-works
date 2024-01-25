source_word="chicken"#supervisor
target_word="hen"#superior
for ch in target_word:
    if ch in source_word:
       source_word=source_word.replace(ch,"",1)
    else:
        print("not kagaroo")
        break  
else:
    print(" kangaroo")      