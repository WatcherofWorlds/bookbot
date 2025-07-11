def get_book_text(path_to_file):
   # This function reads the contents of a file and returns it as a string.
    with open(path_to_file) as f:
         # f is a file object
         file_contents = f.read()
    return(file_contents)



path_to_file = "./books/frankenstein.txt"

def main():
    
    from stats import char_count, sorted_char_count, counting_words
    book_text = get_book_text(path_to_file)
    counts= char_count(book_text)
    sorted_counts = sorted_char_count(counts)
    total_words = counting_words(book_text)


    print("=========== BOOKBOT ===========")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for item in sorted_counts:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()