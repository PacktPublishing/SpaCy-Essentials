import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')


def display_entities(text):
    doc = nlp(text)
    displacy.serve(doc, style='ent')


if __name__ == "__main__":

    text = "Barack Obama was the 44th president of the United States of America."
    display_entities(text)
