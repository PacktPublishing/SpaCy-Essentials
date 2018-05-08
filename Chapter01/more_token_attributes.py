import spacy

nlp = spacy.load("en_core_web_sm")


def token_attributes(text):
    doc = nlp(text)
    for token in doc:
        print("Token: %s - Is Stop Word: %s, Is Punctuation: %s, Like URL: %s, Like Email: %s, Like Number: %s, "
              "Entity Type: %s" % (token.text, token.is_stop, token.is_punct, token.like_url, token.like_email,
                                   token.like_num, token.ent_type_))
        print("--")


if __name__ == "__main__":

    text = "Matthew Honnibal who can be contacted at honnibal@spacy.io, initially released SpaCy in 2015 which can " \
           "be forked from the following repo: https://github.com/explosion/spaCy."
    token_attributes(text)