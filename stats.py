def get_num_words(book_contents):
    words = book_contents.split()
    num_words = len(words)
    return num_words


def get_num_characters(book_contents):
    lowered_contents = book_contents.lower()

    characters = {}

    for char in lowered_contents:
        if char.isalpha():
            if char not in characters:
                characters[char] = 1
            else:
                characters[char] += 1

    return characters


def convert_to_list_dict(single_dict):
    list_of_dicts = [{k: v} for k, v in single_dict.items()]
    return list_of_dicts


def sort_on(dic):
    return next(iter(dic.values()))
