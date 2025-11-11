from stats import get_num_words

#main function
def main():
    book_path = "/home/valentinkranz/workspace/github.com/bootdev/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")


#Function to read the content of a book from a text file and return it as a string
def get_book_text(file_path):
    # Open the file
    with open(file_path) as file:
        # Read the content of the file
        return file.read()

main()  