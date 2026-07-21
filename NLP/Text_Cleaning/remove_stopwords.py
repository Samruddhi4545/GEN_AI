import nltk #type:ignore
from nltk.corpus import stopwords #type:ignore
from nltk.tokenize import word_tokenize #type:ignore
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('stopwords')
text="This is the simple sentence for removing stopwords"
words=word_tokenize(text)
stop_words=set(stopwords.words('english'))
filtered_words=[word for word in words if word.lower() not in stop_words]
filtered_text=' '.join(filtered_words)
print("Original Text:",text)
print("Filtered Text:",filtered_text)