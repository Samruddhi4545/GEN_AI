import spacy #type:ignore
nlp=spacy.load('en_core_web_sm') 

doc=nlp("""Wow!! 🤩 I bought this smartphone for ₹29,999, and it's amazing! 📱 The battery lasts only 6hours. 😕Thanks @MobileHub! Visit https://www.mobilehub.com. I'd definitely buy again! #HappyCustomer""")
tokens=[token.text for token in doc]
print(tokens)
