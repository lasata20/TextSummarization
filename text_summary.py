import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text = """As designers, we are frequently and incorrectly reminded that our job is to “make things pretty.
 We are indeed designers — not artists — and there is no place for formalism in good design.
  Web design has a function, and that function is to communicate the message for which the Web page was conceived. 
The medium is not the message.Never is this principle more pertinent than when dealing with type, 
the bread and butter of Web-borne communication. A well-set paragraph of text is not supposed to wow the reader; 
the wowing should be left to the idea or observation for which the paragraph is a vehicle. In fact, the perfect paragraph is unassuming to the point of near invisibility. 
That is not to say that the appearance of your text should have no appeal at all. On the contrary: well-balanced, comfortably read typography is a thing of beauty; 
it’s just not the arresting sort of beauty that might distract you from reading."""


def summarizer(rawdocs):

    stopwords = list(STOP_WORDS)
    # print(stopwords)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    # print(doc)
    tokens = [token.text for token in doc]
    # print(tokens)
    word_freq = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1

    # print(word_freq)

    max_freq = max(word_freq.values())
    # print(max_freq)

    for word in word_freq.keys():
        word_freq[word] = word_freq[word]/max_freq

    # print(word_freq)

    sent_tokens = [sent for sent in doc.sents]
    # print(sent_tokens)

    sent_scores = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]

    # print(sent_scores)

    select_len = int(len(sent_tokens)*0.3)
    # print(select_len)

    summary = nlargest(select_len, sent_scores, key=sent_scores.get)
    # print(summary)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    # print(text)
    # print(summary)

    # print("Length of original text", len(text.split(' ')))
    # print("Length of summary text", len(summary.split(' ')))

    return summary, doc, len(rawdocs.split(' ')), len(summary.split(' '))
