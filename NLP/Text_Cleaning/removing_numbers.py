import re
text='My age is 23 and i have 2 dogs'
clean_text=re.sub(r'\d+','',text)
print("Original Text:",text)
print("Cleaned Text:",clean_text)