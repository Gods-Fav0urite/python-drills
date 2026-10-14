def longest_word(sentence):
    punctuation = '!"#\$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    
    tokens = sentence.split()
    longest = ""
    max_len = 0
    
    for token in tokens:
        cleaned = token.strip(punctuation)
        
        if not cleaned:
            continue
            
        if len(cleaned) > max_len:
            max_len = len(cleaned)
            longest = cleaned
            
    return longest


# Bonus
def longest_words(sentence):
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    tokens = sentence.split()
    
    max_len = 0
    result = []
    
    for token in tokens:
        cleaned = token.strip(punctuation)
        
        if not cleaned:
            continue
            
        if len(cleaned) > max_len:
            max_len = len(cleaned)
            result = [cleaned]
        elif len(cleaned) == max_len:
            result.append(cleaned)
            
    return result
