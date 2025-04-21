def get_word_count(book_text):
    words = book_text.split()
    return len(words)

def get_character_counts(book_text):
    counts = {}

    for char in book_text:
        lc = char.lower()
        if lc in counts:
            counts[lc] += 1
        else:
            counts[lc] = 1

    return counts

def sort_characters(char_dict):
    def sort_on(dict):
        return dict["count"]

    char_list = []

    for char in char_dict:
        char_list.append({"char": char, "count": char_dict[char]})

    char_list.sort(reverse=True, key=sort_on)

    return char_list