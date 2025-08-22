from stats import get_number_of_words
from stats import get_book_text
from stats import get_number_of_chars
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book_path = sys.argv[1] 
    print(f"Analyzing book found at {book_path}")
    print("------------ Word Count ---------")
    text = get_book_text(book_path)
    number_of_words = get_number_of_words(text)
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    chars_dict = get_number_of_chars(text)
    sorted_chars_dict = dict(sorted(chars_dict.items(),reverse = True, key = lambda item: item[1]))
    for char in sorted_chars_dict:
        print(f"{char}: {sorted_chars_dict[char]}")
    print("=========== END =================")

main()
