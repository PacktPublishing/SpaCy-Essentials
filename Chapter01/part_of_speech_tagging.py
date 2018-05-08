import spacy

nlp = spacy.load("en_core_web_sm")


def pos_tagging(text):
    doc = nlp(text)
    for token in doc:
        print("Token: %s, Coarse-grained POS-Tag: %s" % (token.text, token.pos_))
        print("Token: %s, Fine-grained POS-Tag: %s" % (token.text, token.tag_))
        print("--")


if __name__ == "__main__":

    text = "Alexander Bell who was a Scottish scientist is credited with inventing the first practical telephone"
    pos_tagging(text)