while True:
    inputs = input()
    if inputs == "0":
        break
    message = "yes" if inputs == inputs[::-1] else "no"
    print(message)
