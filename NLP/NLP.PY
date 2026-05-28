class TEXT_CLEANING:
    def __init__(self):
        self.user_prompt = input("Enter a prompt 😊✌️..")
    def text_cleaning(self):
        import spacy
        nlp = spacy.load('en_core_web_sm')
        docs = nlp(self.user_prompt)
        cleaned_tokens = [token.lemma_ for token in docs if not token.is_stop]
        return ' '.join(cleaned_tokens)
user1 = TEXT_CLEANING()
result = user1.text_cleaning()
print(result)
''' 
Enter a prompt 😊✌️.. what is machine learning ?
what is machine learning ? -> stopwords function -> what machine learning ?
->text cleaning => result

what be machine learn ?
'''