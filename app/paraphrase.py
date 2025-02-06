import random

def paraphrase_text(text):
    words = text.split()
    random.shuffle(words)
    return " ".join(words)
