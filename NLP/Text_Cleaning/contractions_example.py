import contractions #type:ignore
text="I'm learning NLP because it's amazing.I can't wait to build my project"
expanded_text=contractions.fix(text)
print("Original Text:",text)
print("Expanded Text:",expanded_text)