def get_file_contents(url):
    with open(url) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    text_lowered = text.lower()
    for char in text_lowered:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def get_alpha_chars(chars_dict):
    alpha_list = []
    for i in chars_dict.keys():
        if i.isalpha():
            alpha_list.append({"key":i,"value":chars_dict[i]})
    alpha_list.sort(reverse=True, key=get_sort_key)
    return alpha_list

def get_sort_key(dict):
    return dict["value"]

def main():
    book_path = "books/frankenstein.txt"
    text = get_file_contents(book_path)
    word_count = count_words(text)
    char_count = count_characters(text)
    alpha_chars = get_alpha_chars(char_count)
    
    for i in alpha_chars:
        print(f"The \'{i["key"]}\' character was found {i["value"]} times")

main()
