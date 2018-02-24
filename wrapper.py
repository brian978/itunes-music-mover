def prompt(text, default=""):
    user_input = raw_input(text)
    if 0 == len(user_input):
        user_input = default

    return user_input
