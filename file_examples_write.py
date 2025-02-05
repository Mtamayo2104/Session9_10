# lets create a virtual diary
with open("diary.text", "a") as fp:
    while True:
        text = input("How do yo feel today? (type q to quit):")
        if text == "q":
            break
        fp.write(f"{text}\n")

