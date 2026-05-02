first_word = input("Greeting: \n").strip().lower()[0:5]
if first_word =="hello":
    print("$0")
elif first_word[0]=="h":
    print("$20")
else:
    print("$100")