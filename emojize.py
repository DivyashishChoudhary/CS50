import emoji

def main():
    user_emoji = input("Input: ")
    print(f"Output: {emoji.emojize(user_emoji,language = 'alias')}")


if __name__ == "__main__":
    main()