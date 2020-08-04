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

def counter_words_fast(text):
    text = text.lower()
    skips = [",", ".", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")

    word_counts = Counter(text.split(" "))
    return word_counts


print(count_words(text1))
print(counter_words_fast(text1))