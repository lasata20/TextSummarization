# coding = utf8
import numpy as np
from Summarizer import tokenizer
from Summarizer import ranker


def get_summary_from_text_file(rawtext):
    #
    # Reading text files (sample text file, word endings file and stopwords file)
    #
    text = rawtext
    stop_words = open(
        "C:/Users/lasat/TextSummarization/Summarizer/stopwords.txt", 'r', encoding="utf-8").read()
    word_endings = open(
        "C:/Users/lasat/TextSummarization/Summarizer/word_endings.txt", 'r', encoding='utf-8').read()
    valid_characters = tokenizer.get_valid_chars()
    # print(stop_words.split("\n"))
    # print(text)
    #
    # Remove useless characters from the sentence
    #
    text = tokenizer.remove_useless_characters(text, valid_characters)
    print(text)
    #
    # Split the sentence into array of words and patagraph in its array. (as Array of Array of the words)
    #
    sentences = tokenizer.get_sentences_as_arr(text)
    words_arr = tokenizer.get_words_as_arr(sentences)
    #
    # Remove the stop words from the array
    #
    words_arr = tokenizer.remove_stop_words_and_filter_word_arr(
        words_arr, word_endings, stop_words,)
    # print(words_arr)

    #
    # remove empty sentences and lone word sentences and update sentences accordingly
    #
    sentences, words_arr = tokenizer.remove_empty_sentences(
        sentences, words_arr)
    #
    # Tokenize the words and sentences into numbers
    #
    tokens, token_dict = tokenizer.tokenize(words_arr)
    #
    # Create a association matrix
    #
    association_matrix, counter_vector = ranker.create_association_matrix(
        tokens, No_of_unique_chars=len(token_dict))
    #
    # Calculate influence of each word on the paragraph
    #
    word_influence_vector = ranker.calculate_word_ranks(
        association_matrix, counter_vector)
    #
    # Based in the word importance ranking, calculate teh sentence importance ranking.
    #
    sentence_influence = ranker.calculate_sentence_influence(
        tokens, word_influence_vector)
    #
    # sort sentences based on its influence
    #
    # sorted_sentences = tokenizer.sort_sentences_with_influence(sentences,sentence_influence)
    #
    # Get first n sentences from the given text as summarized text.
    #
    summary_sentences = ranker.get_n_influencial_sentence(
        sentences, sentence_influence, n=np.ceil(len(sentences)*0.33))
    #
    # Combine all sentences as a single paragraph
    #
    summarized_text = ranker.get_summarized_text(summary_sentences)

    # print(summarized_text)

    # open('D:\Programming\Projects\major_project\Codes\Backend\Output\\output.txt', 'w',encoding="utf-8").write(summarized_text)

    return summarized_text
