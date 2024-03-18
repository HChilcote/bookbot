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
    #print(letter_count)
    return letter_count

def report_words():
    new_count = []
    letter_count = num_chars_string(file_contents)
    for i in letter_count:
        if i.isalpha():
            new_count.append([i, letter_count[i]])
    new_count.sort(reverse=True, key=lambda x: x[1])
    print(f'----Start Report----')
    for j in new_count:
        print(f"The '{j[0]}' character showed up {j[1]} times")
    print('-----End Report-----')

def main():
    print(len(file_contents.split()))
    num_chars_string(file_contents)
    report_words()

main()