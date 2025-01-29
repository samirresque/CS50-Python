from random import randint
def main():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except:
            pass

    number = randint(1,level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                if guess < number:
                    print("Too small!")
                    pass
                elif guess > number:
                    print("Too large!")
                    pass
                elif guess == number:
                    print("Just right!")
                    break
        except:
            pass

if __name__ == "__main__":
    main()
