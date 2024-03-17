with open("books/frankenstein.txt") as f:
    file_contents = f.read()

def main():
    print(len(file_contents.split()))

main()