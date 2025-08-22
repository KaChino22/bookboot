def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()
    
def get_number_of_words(text):
    number_of_words = 0
    words = text.split()
    for word in words:
        number_of_words += 1
    return number_of_words
 
def get_number_of_chars(text):
    number_of_chars = 0
    chars_dict = {}
    words = text.split()   
    for word in words:
        for char in word: 
            char = char.lower()
            if char in chars_dict:
                chars_dict[char] += 1
            else:
                chars_dict[char] = 1
    return chars_dict