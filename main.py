def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = get_book_words(text)
    print(f"{count} words found in the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_book_words(book_string):
    word_count = 0
    words = book_string.split()
    for word in words:
        word_count += 1
    return word_count

main()
