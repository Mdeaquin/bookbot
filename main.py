from stats import get_book_words
from stats import num_char_appear

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_book_words(text)
    char_dict = num_char_appear(text)
    print(f"{count} words found in the document")
    print(char_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
