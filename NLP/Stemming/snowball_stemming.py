from nltk import SnowballStemmer #type:ignore
snow=SnowballStemmer("english")

words=['running','runner','studies','happiness']

print('\n Snowball stemmer results:')
for w in words:
    print(w,"->",snow.stem(w))