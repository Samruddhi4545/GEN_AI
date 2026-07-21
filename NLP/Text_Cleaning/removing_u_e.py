import re
text="""
visit https://openai.com
Contact us at abc@gmail.com
"""
#remove url
text=re.sub(r'https?://\S+|www\.\S+','',text)
#remove email
text=re.sub(r'\S+@\S+','',text)
print("Text:",text)