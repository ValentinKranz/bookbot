from stats import count_words, count_chars, sort_char_counts
import sys # Import the built-in sys module, which lets us access command-line arguments

# Check that the user provided exactly one argument (the book path)
# sys.argv[0] is always the script name, so we expect 2 total items: ["main.py", "<path_to_book>"]
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>") # If the user forgot to include the path, print a helpful usage message
    sys.exit(1) # Exit the program with a non-zero status code (1 means 'error')

book_path = sys.argv[1]

#main function
def main():
    file_path = book_path
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