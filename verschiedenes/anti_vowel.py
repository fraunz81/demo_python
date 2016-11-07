def anti_vowel(text):
    result = ""
    for char in text:
        #charL = char.lower()
        #if charL != "a" and charL != 'e' and charL != 'i' and charL != 'o' and charL != 'u':
        if char not in "aeiouAEIOU":
            result += char
    
    return result


print (anti_vowel("Hey you!"))
