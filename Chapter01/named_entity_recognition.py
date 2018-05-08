import spacy

nlp = spacy.load("en_core_web_sm")


def extract_entities(text):
    for entity in nlp(text).ents:
        print("Entity: ", entity.text)
        print("Entity Type: %s | %s" % (entity.label_, spacy.explain(entity.label_)))
        print("Start Offset of the Entity: ", entity.start_char)
        print("End Offset of the Entity: ", entity.end_char)
        print("--")


if __name__ == "__main__":
    text = "Barack Obama was the 44th president of the United States of America."
    extract_entities(text)
