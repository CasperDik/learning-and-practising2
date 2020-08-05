import os
import pandas as pd
import numpy as np
from collections import Counter

def count_words_fast(text):
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"', "\n", "!", "?", "(", ")"]
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts

def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

hamlets = pd.read_csv("hamlet.csv", index_col=0)

language, text = hamlets.iloc[0]
counted_text = count_words_fast(text)

data = pd.DataFrame(columns=("word", "count", "length", "frequency"))
keys = list(counted_text.keys())
values = list(counted_text.values())

for i in range(len(keys)):
    if values[i] > 10:
        frequency = "frequent"
    elif values[i] <= 10 and values[i] > 1:
        frequency = "infrequent"
    else:
        frequency = "unique"

    data.loc[i] = keys[i], values[i], len(keys[i]), frequency

data = data.sort_values(by=["count"], ascending=False)
print(data.loc[data["word"]=="hamlet"])
print(data[data["frequency"] == "unique"].count())


subset = pd.DataFrame(columns=("language", "frequency", "mean_word_length", "num_words"))

freq = ["frequent", "infrequent", "unique"]

mean = [data[data["frequency"]==f].mean().get("length") for f in freq]
num_word = [data[data["frequency"]==f].count().get("length") for f in freq]

for j in range(len(freq)):
    subset.loc[j] = language, freq[j], mean[j], num_word[j]


def summarize_text(language, text):
    counted_text = count_words_fast(text)

    data = pd.DataFrame({
        "word": list(counted_text.keys()),
        "count": list(counted_text.values())
    })

    data.loc[data["count"] > 10, "frequency"] = "frequent"
    data.loc[data["count"] <= 10, "frequency"] = "infrequent"
    data.loc[data["count"] == 1, "frequency"] = "unique"

    data["length"] = data["word"].apply(len)

    sub_data = pd.DataFrame({
        "language": language,
        "frequency": ["frequent", "infrequent", "unique"],
        "mean_word_length": data.groupby(by="frequency")["length"].mean(),
        "num_words": data.groupby(by="frequency").size()
    })

    return (sub_data)


for i in range(3):
    language, text = hamlets.iloc[i]
    summarize_text(language, text)