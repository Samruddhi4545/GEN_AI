import nltk #type:ignore
from nltk.tokenize import word_tokenize #type:ignore
#nltk.download('punkt')
#nltk.download('punkt_tab')

#Word tokenization using split()
text="My name😁 is1 nithya"
print(text.split())

#Word tokenizing using nltk word_tokenize()
text="Wow!! 🤩 I bought this smartphone for ₹29,999, and it's amazing! 📱 The battery lasts only 6hours. 😕Thanks @MobileHub! Visit https://www.mobilehub.com. I'd definitely buy again! #HappyCustomer"
print(word_tokenize(text))