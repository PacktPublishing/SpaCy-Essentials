import spacy

nlp = spacy.load("en_core_web_sm")


def noun_phrases(text):
    for np in nlp(text).noun_chunks:
        print("Noun Phrase: ", np.text)
        print("Start Offset of the Noun Phrase: ", np.start_char)
        print("End Offset of the Noun Phrase: ", np.end_char)
        print("--")


if __name__ == "__main__":
    
    text = "Barack Obama was the 44th president of the United States of America."
    noun_phrases(text)
