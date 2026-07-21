import string 
text="hello welcome to, NLP.How are you?"
translator=str.maketrans('','',string.punctuation)
clean_text=text.translate(translator)
print("original text",text)
print("Without punctuation:",clean_text)