def get_book_words(book_string):
    words = book_string.split()
    return len(words)

def num_char_appear(book_string):
    converted_string = book_string.lower()
    char_count = {}
    for char in converted_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_chars(char_count):
    dict_list = [{'char': c, 'value': v} for c,v in char_count.items()]
    dict_list.sort(key=lambda dict: dict['value'], reverse=True)
    return dict_list
