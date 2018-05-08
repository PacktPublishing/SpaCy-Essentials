import spacy

nlp = spacy.load('en_core_web_sm')


def split_into_sentences(input_text):
    for i, sentence in enumerate(nlp(input_text).sents):
        print("Sentence %d: %s" % (i, sentence.text))
        print("Start Offset %d, End Offset %d" % (sentence.start, sentence.end))
        print("---")


if __name__ == "__main__":

    text = """SpaCy is an open-source software library that is published and distributed under MIT license, and is 
            developed for performing simple to advanced Natural Language Processing (N.L.P) tasks such as tokenization,
             part-of-speech tagging, named entity recognition, text classification, and calculating semantic 
             similarities between text, lemmatization, dependency parsing, among others. It was originally developed 
             by Matthew Honnibal and is still maintained by him along with Ines Montani. SpaCy is written using Python 
             and Cython. Under the hood it uses Thinc, a machine learning library written and maintained by the 
             creators of SpaCy. Thinc is built ground up for efficient CPU usage and optimized for developing code and 
             models related to N.L.P and deep learning on text. At the time of writing of this book SpaCy offers the 
             fastest syntactic parser in the world. It also offers state-of-the-art statistical and neural network 
             models for different languages such as English, German, Spanish, Portuguese, French, Italian and Dutch. 
             Due to its large open source community, there is a continuous ongoing development of statistical models on 
             various other languages including low-resource languages such as Hindi, Marathi, and many more."""

    split_into_sentences(text)
