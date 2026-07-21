#libraries imported
import re
import nltk #type:ignore
import string
from nltk.corpus import stopwords #type:ignore
from nltk.tokenize import word_tokenize #type:ignore
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

#input text
text="""Hello!!! My name is Sam.
Visit https://openai.com
Email: sam@gmail.com
I have 2 laptops 😊.
"""

#lowercasing
text=text.lower()

#removing punctuation
print("test after lowering and before removing punctuation:\n",text)
translator=str.maketrans('','',string.punctuation)
clean_text=text.translate(translator)
print("original text:\n",text)
print("Without punctuation:",clean_text)

#removing numbers
cleaning_text=re.sub(r'\d+','',text)
print("text before removing numbers:\n",text)
print("text after removing numbers:\n",cleaning_text)

#removing email and url
print("Text before removing email id and url:\n",text)
text=re.sub(r'https?://\S+|www\.\S+','',text)
text=re.sub(r'\S+@\S+','',text)
print("Text after removing email id and url:\n",text)