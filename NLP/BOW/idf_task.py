from sklearn.feature_extraction.text import TfidfVectorizer #type:ignore
text =["Before an AI model or Large Language Model (LLM) like GPT-4 can read text",
"😃 it needs to convert the text into numerical IDs."]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(text)
print("TF-IDF Matrix:")
print(tfidf_matrix)#sparse matrix
print("\n Tf-IDF values in Matrix Form:")
print(tfidf_matrix.toarray())#dense matrix