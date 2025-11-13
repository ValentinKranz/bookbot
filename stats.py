#Function to count words in file
def count_words(text):
    words = text.split()
    return len(words)

#Function to count characters
def count_chars(text):
    count = {}
    for char in text:
        char = char.lower()
        if char.isalpha(): # only letters
            #if char not in count:
            #    count[char] = 0
            #count[char] += 1
            count[char] = count.get(char, 0) + 1 #simplify
    return count

#A function that takes a dictionary and returns the value of the "num" key
#This is how the `.sort()` method knows how to sort the list of dictionaries
def _by_num(char_dict):
    return char_dict["num"]

#Takes the dictionary of characters and their counts and returns a sorted list of dictionaries.
def sort_char_counts(char_count):
    #for char, num in char_count.items():
    #    items.append({"char": char, "num": num})
    items = [{"char": char, "num": num,} for char, num in char_count.items()] #simplify
    items.sort(reverse=True, key=_by_num)
    return items