from stats import get_book_words
from stats import num_char_appear
from stats import sort_chars
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        count = get_book_words(text)
        char_dict = num_char_appear(text)
        sorted_chars = sort_chars(char_dict)
        print_report(book_path, count, sorted_chars)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for dict in sorted_chars:
        if dict['char'].isalpha() == True:
            print(f"{dict['char']}: {dict['value']}")
    print("============= END ===============")

main()
