from nltk import PorterStemmer #type:ignore
porter= PorterStemmer()

words=['running','runner','studies','happiness']

print('\n porter stemmer results:')
for w in words:
    print(w,"->",porter.stem(w))