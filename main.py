import sys

from stats import get_word_count
from stats import get_character_counts
from stats import sort_characters

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_word_count(book_text)
    character_counts = get_character_counts(book_text)
    sorted_characters = sort_characters(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char in sorted_characters:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["count"]}")

    print("============= END ===============")

main()