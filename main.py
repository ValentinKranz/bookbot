from stats import count_words, count_chars, sort_char_counts
from pathlib import Path

#main function
def main():
    file_path = Path(__file__).parent/"books"/"frankenstein.txt"
    text = get_book_text(file_path)
    print_report(text)

#Function to read the content of a book from a text file and return it as a string
def get_book_text(file_path):
    # Open the file
    with open(file_path) as f:
        # Read the content of the file
        return f.read()

def print_report(text):
    num_words = count_words(text)
    chars_sorted = sort_char_counts(count_chars(text))

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in chars_sorted:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

if __name__ == "__main__":
    main()  