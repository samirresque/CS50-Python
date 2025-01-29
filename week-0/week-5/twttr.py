def main():
    word = input("Enter word: ")
    print(shorten(word))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    for letter in word:
        if letter.lower() in vowels:
            word = word.replace(letter, "")
    return word

if __name__ == "__main__":
    main()
