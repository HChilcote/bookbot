with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def num_chars_string(file_contents):
    letter_count = {}
    file_contents = file_contents.lower()
    for letter in file_contents:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    print(letter_count)
    return letter_count

def main():
    print(len(file_contents.split()))
    num_chars_string(file_contents)
    
main()