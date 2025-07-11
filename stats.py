def counting_words(book_text):
    # This function counts the number of words in a string.
    lower_case = book_text.lower()
    words = lower_case.split()
    total_words = len(words)
       
    return total_words

def char_count(file_contents):
    # This function counts the occurrences of each letter in a string.
    lower_case = file_contents.lower()
    letters = "abcdefghijklmnopqrstuvwxyzæâêëô"
    char_count = {letter: 0 for letter in letters}
    
    for char in lower_case:
        if char in char_count:
            char_count[char] += 1
            
    return char_count

def sorted_char_count(char_count_dict):
    # This function sorts the character count dictionary alphabetically by letter.
    sorted_count = sorted(char_count_dict.items(), key=lambda item: item[1], reverse=True)
    char_result = [{"char": char, "num": num} for char, num in sorted_count]
        

    return char_result
