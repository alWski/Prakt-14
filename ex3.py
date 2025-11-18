def extract_words(text):
    punct = ['.', ',', '!', '?', ';', ':', '(', ')']
    words = text.split()
    
    result = []
    for word in words:
        clean_word = word
        for p in punct:
            clean_word = clean_word.replace(p, '')
        if clean_word:
            result.append(clean_word)
    
    return result

def main():
    s = input()
    print(extract_words(s))

if __name__ == "__main__":
    main()


