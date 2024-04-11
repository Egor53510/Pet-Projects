def generate_hashtag(s):
    return "".join("#" + "".join(s.strip().title().split())) if len("".join("#" + "".join(s.strip().title().split()))) <= 140 and len("".join("#" + "".join(s.strip().title().split()))) > 1 else False

print(generate_hashtag(''))
