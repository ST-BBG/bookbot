def main():
    bookpath = "books/frankenstein.txt"
    text = read_book(bookpath)
    word_num = count_words(text)
    letter_count = count_letters(text)
    print_report(word_num, letter_count, bookpath)

def read_book(path):
    with open(path) as f:
        return f.read()              

def count_words(text):
    words = text.split()
    return len(words)

def sort(letter_count):
    return letter_count["num"]

def count_letters(text):
    letter_counter = {}
    sorted = []
    lowered_text = text.lower()
    for letters in lowered_text:
        if letters in letter_counter:
            letter_counter[letters] += 1
        else:
            letter_counter[letters] = 1
    for l in letter_counter:
        if l.isalpha():
            sorted.append({"lett": l, "num": letter_counter[l]})
    sorted.sort(reverse=True, key=sort)
    return sorted

def print_report(word_num, letter_count, bookpath):
    print(f"Begin Report of {bookpath}")
    print(f"{word_num} words in the Document")
    for l in letter_count:
        print(f"The Letter", {l["lett"]}, "has been found", {l["num"]}, "times")
    print("Thanks for Reading")     

main()