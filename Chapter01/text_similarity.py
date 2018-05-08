import spacy

nlp = spacy.load("en_core_web_lg")


def text_similarity(inp_obj1, inp_obj2):
    return inp_obj1.similarity(inp_obj2)


def token_similarity(doc):
    for token1 in doc:
        for token2 in doc:
            print("Token 1: %s, Token 2: %s - Similarity: %f" % (token1.text, token2.text, token1.similarity(token2)))
            print("---")


if __name__ == "__main__":
    doc1 = nlp("Barack Obama was the 44th president of the United States of America.")
    doc2 = nlp("Donald Trump is the 45th president of the United States of America.")
    doc3 = nlp("SpaCy and NLTK are two popular NLP libraries in Python community.")
    print("Similarity between doc1 and doc2: ", text_similarity(doc1, doc2))
    print("Similarity between doc1 and doc3: ", text_similarity(doc1, doc3))

    doc4 = nlp("Apple orange cats dogs")
    token_similarity(doc4)

    print("Vector representation of Apple: ", doc4[0].vector)
