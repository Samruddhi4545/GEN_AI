import nltk #type:ignore
from nltk.tokenize import sent_tokenize #type:ignore
#nltk.download('punkt')
#nltk.download('punkt_tab')

text="""Artifical intelligence is transformimg industries. It helps automate repetative tasks. Are you excited to learn NLP? let's get started! """
print(sent_tokenize(text))