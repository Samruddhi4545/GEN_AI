import gensim.downloader as api #type:ignore
import numpy as np


model = api.load("glove-wiki-gigaword-50")

text = "Machine learning is amazing"

words=[word for word in text.lower().split() if word in model.key_to_index]

if words:
    vector = np.mean([model[word] for word in words], axis=0)
    print("Vector Shape:", vector.shape)
    print("Vector[first 20 dimensions]:", vector[:20])
else:
    print("No words from the text are in the model's vocabulary.")