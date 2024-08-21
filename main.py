def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = word_count(text)
    char_dict = char_count(text)
    list = []
    for letter in char_dict:
        if letter.isalpha():
            temp_dict = {}
            temp_dict["letter"] = letter
            temp_dict["count"] = char_dict[letter]
            list.append(temp_dict.copy())
    report(num_words, list, book_path)
    
def sort_on(dict):
    return dict["count"]
    
def report(words, chars, path):
    print(f"--Begin report of {path}--")
    print(f"{words} words found in document")
    print("")
    chars.sort(reverse=True, key=sort_on)
    for entry in chars:
        x = entry["letter"]
        y = entry["count"]
        print(f"The '{x}' character was found {y} times")
    print("--End report--")
    
def char_count(string):
    low_text = string.lower()
    counts = {}
    for character in low_text:
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1
    return counts

def get_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
        

def word_count(string):
    words = string.split()
    return len(words)



main()