def count_otv(text):
    letter = {'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'}
    
    otv_count = 0
    no_otv_count = 0
    words_otv = []
    
    words = text.split()
    
    for word in words:
        words_otv_count = 0
        
        for char in word:
            if char in letter:
                otv_count += 1
                words_otv_count += 1
            else:
                no_otv_count += 1
        
        if words_otv_count >= 2:
            words_otv.append(word)
    
    return otv_count, no_otv_count, words_otv

s = input().lower()

otv, no_otv, words_list = count_otv(s)

print(otv)
print(no_otv)
print(words_list)
