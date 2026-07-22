from transformers import GPT2Tokenizer #type:ignore

#bert tokenizer

text="NLP preprocessing transformers unstructured textual data effectively"

#gpt2 is the model that can do tokenization
gpt2_tok=GPT2Tokenizer.from_pretrained('gpt2')
gpt2_tokens=gpt2_tok.tokenize(text)
print("\n GPT2_tokens:",gpt2_tokens)
print("GPT IDs:",gpt2_tok.encode(text))

#convert all the text to number
print('vocab sizes of gpt2:',gpt2_tok.vocab_size)