def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    character_list = create_list(num_characters)
    print(f" --- Begin report of {book_path} ---\n{num_words} words found in the document")
    for i in character_list:
        print(f" The '{i['character']}' character was found {i['num']} times")

def get_num_words(text):
    words = text.split()
    return len(words)
    
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
        
def get_num_characters(text):
    num_count = {}
    for c in text:
        lowered = c.lower()
        if lowered in num_count:
            num_count[lowered] += 1
        else:
            num_count[lowered] = 1
    return num_count

def create_list(num_characters):
    new_list = []
    for c in num_characters:
        if c.isalpha():
            new_list.append(dict(character = c, num = num_characters[c]))
    new_list.sort(reverse=True, key=sort_on)
    return new_list

def sort_on(dict):
    return dict["num"]

main()