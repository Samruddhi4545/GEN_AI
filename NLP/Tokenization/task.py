import nltk #type:ignore
import spacy #type:ignore
from nltk.tokenize import sent_tokenize #type:ignore
from nltk.tokenize import word_tokenize #type:ignore

#char tokens
text="Before an AI model or Large Language Model (LLM) like GPT-4 can read text,😃 it needs to convert the text into numerical IDs. This is done by mapping each token to an integer using a predefined dictionary or vocabulary🙂"
char_tokens=list(text)
print("Char Tokens:\n",char_tokens)

#sentence tokens
print("Sentence tokens:\n",sent_tokenize(text))

#spacy tokens
nlp=spacy.load('en_core_web_sm')
doc=nlp(text)
tokens=[token.text for token in doc]
print("Spacy tokens:\n",tokens)

#split tokens
print("split tokens:\n",text.split())

#word tokens
print("word tokens:\n",word_tokenize(text))