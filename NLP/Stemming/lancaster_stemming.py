from nltk.stem import LancasterStemmer #type:ignore
lancaster=LancasterStemmer()

words=['running','runner','studies','happiness']

print('\n lancaster stemmer results:')
for w in words:
    print(w,"->",lancaster.stem(w))