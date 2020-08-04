from collections import Counter

text1 = "This is my test text. We're keeping this text short to keep things manageable"

def count_words(text):
    text = text.lower()
    skips = [",", ".", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")

    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def count_words_fast(text):
    text = text.lower()
    skips = [",", ".", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")

    word_counts = Counter(text.split(" "))
    return word_counts

def read_book(title_path):
    """
    read a book and return it as a string
    """
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text


text = read_book("./English/shakespeare/Romeo and Juliet.txt")
print(len(text))