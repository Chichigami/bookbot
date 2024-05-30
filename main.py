def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    book_report(book_path, word_count(text), alphabet_dict(text))

def word_count(text):
    return len(text.split())

def alphabet_dict(text):
    alphabet = {}
    text = text.lower()
    for char in text:
        if char in alphabet:
            alphabet[char] += 1
        else:
            alphabet[char] = 1
    return alphabet

def get_book_text(path):
    with open(path) as f:
        return f.read()

def book_report(path, count, alphabet):
    #sort the dictionary based on value desc
    alphabet = dict(sorted(alphabet.items(), key=lambda item: item[1], reverse=True))
    #start of the report 
    print(f"--- Begin report of {path} --- \n{count} words found in the document \n")
    for key, value in alphabet.items():
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")
    print("--- End of report ---")

main()
