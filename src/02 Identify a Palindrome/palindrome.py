import re

def is_palindrome(phrase):
    cleaned_text = re.sub(r'[^\w]', '', phrase)  
    cleaned_text = re.sub(r'\s+', '', cleaned_text) 
    cleaned_text = cleaned_text.lower()
    start, end = 0 , len(cleaned_text)-1
    while start < end:
        if cleaned_text[start] != cleaned_text[end]:
            return False
        start+=1
        end-=1
    return True


# commands used in solution video for reference
if __name__ == '__main__':
    print(is_palindrome('hello world'))  # false
    print(is_palindrome("Go hang a salami, I'm a lasagna hog."))  # true
    print(is_palindrome("go."))  # false
    print(is_palindrome(""))  # true
    print(is_palindrome("g"))  # true
    print(is_palindrome("gOG"))  # true
