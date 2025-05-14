def count_words(content):
    words_list = content.split()
    num_words = len(words_list)
    print(f"{num_words} words found in the document")


def count_chars(content):
    char_list = list(content)
    char_index = {}
    for char in char_list:
        convert_char = char.lower()
        if convert_char in char_index:
            char_index[convert_char] += 1
        else:
            char_index[convert_char] = 1
    return char_index


def sort_and_print_dict(content):
    transform_dict = count_chars(content)
    transform_dict = [
        {"name": k, "num": v} for k, v in transform_dict.items() if k.isalpha()
    ]
    transform_dict.sort(reverse=True, key=sort_on)
    
    
    [print(f"{d['name']}: {d['num']}") for d in transform_dict]

def sort_on(dict):
    return dict["num"]
