import math
import pprint
from collections import Counter


# Split text at spaces and return a list of words
def splitAtSpaces(fileToSplit) -> list:
    listOfWords = fileToSplit.split()
    return listOfWords

# Group words into bigrams and return a list of those bigrams
def wordsToBigrams(words) -> list:
    bigrams = [(words[element - 1], words[element]) for element in range(1, (words.__len__()))]
    return bigrams

# Tally the # of occurrences of bigrams and return a dictionary counting occurrences of bigrams
def countBigrams(bigrams) -> dict:
    bigramOccurrences = Counter()
    for bigram in bigrams:
        bigramOccurrences[bigram] += 1
    return bigramOccurrences

# How many times have the bigrams in the given sentences appeared in the corpus?
def sentenceBigramsCounts(sentenceBigrams, bigramOccurances):
    result = {}
    for b in range(sentenceBigrams.__len__()):
        result.update({sentenceBigrams[b]: bigramOccurrences[sentenceBigrams[b]]})
    return result

# Tally # of occurrences of words (or Unigrams) and return a dictionary containing the #'s
def countWords(words):
    vocabulary = Counter()
    for word in words:
        vocabulary[word] += 1
    vocabularySize = vocabulary.__len__()
    # pprint.pprint(vocabulary)
    # print(vocabularySize)
    return vocabulary, vocabularySize

# Generate the bigram count table for sentence1 and sentence2
def bigramCountTable(sentence1, sentence2, bigrams):
    words1 = splitAtSpaces(sentence1)
    totalSentenceBigrams1 = [(a, b) for b in words1 for a in words1]
    countOfBigrams1 = []
    # How many times do the Bigrams in the given sentence appear in the corpus?
    for i in range(0, 99):
        countOfBigrams1.append((totalSentenceBigrams1[i], bigrams.count(totalSentenceBigrams1[i])))

    words2 = splitAtSpaces(sentence2)
    totalSentenceBigrams2 = [(a, b) for b in words2 for a in words2]
    countOfBigrams2 = []
    # How many times do the Bigrams in the given sentence appear in the corpus?
    for i in range(0, 99):
        countOfBigrams2.append((totalSentenceBigrams2[i], bigrams.count(totalSentenceBigrams2[i])))

    # Sort the results according to the first word in the first tuple. So we have all tuples starting in
    # 'The' first like (('The'. 'president'), 0)....and so on.
    first = sorted(countOfBigrams1, key=lambda x: x[0][0])
    second = sorted(countOfBigrams2, key=lambda x: x[0][0])
    # Write data to text files for easy evaluation
    f = open('s1Tables.txt', 'w')
    g = open('s2Tables.txt', 'w')

    f.write(str(first))
    g.write(str(second))

    f.close()
    g.close()

# Case 1: No Smoothing. Calculate the probabilities of the sentences.
def noSmoothing(bigTallyInFirst, bigTallyInSecond, vocabulary, bigramOccurrences):
    print("For the case 1 : No smoothing applied")
    print("*************************************")
    # Initialize probabilities to 0
    sentence1Prob, sentence2Prob = 0, 0
    # Sentence 1
    # Sentence 2

# Case 2 : Add one smoothing. Calculate Add-one smoothing
def addOneSmoothing(bigramsInFirst, bigramsInSecond, vocabulary, bigramOccurances):
    print("For add-one smoothing:")
    print("**********************")
    # Initialize probabilities to 0
    sentence1Prob, sentence2Prob = 0, 0
    # Sentence1
    # Sentence2

if __name__ == '__main__':
    # Read corpus data in the variable corpusFile
    f = open('corpus.txt', 'r')
    corpusFile = f.read()

    # Split corpus file in a list 'words' at \s (i.e. spaces)
    words = splitAtSpaces(corpusFile)
    # pprint.pprint(words)

    # Form bigrams from all the 'words'
    bigrams = wordsToBigrams(words)
    # pprint.pprint(bigrams)

    # Tally the bigrams in the corpus
    bigramOccurrences = countBigrams(bigrams)
    # pprint.pprint(bigramOccurrences)

    # Vocabulary and Vocabulary size : Tally occurrence of words[i] in 'words'
    vocabulary, vocabularySize = countWords(words)
    # pprint.pprint(vocabulary[','])

    # Count the bigrams for the Bigram Count table for the given sentences.
    first = "The president has relinquished his control of the company's board."
    second = "The chief executive officer said the last year revenue was good."
    bigramCountTable(first, second, bigrams)

    # Form bigrams for the 2 sentences - returns a dictionary of bigrams and their counts in the corpus.
    words_to_bigrams = wordsToBigrams(splitAtSpaces(first))
    bigTallyInFirst = sentenceBigramsCounts(words_to_bigrams, bigramOccurrences)

    words_to_bigrams2 = wordsToBigrams(splitAtSpaces(second))
    bigTallyInSecond = sentenceBigramsCounts(words_to_bigrams2, bigramOccurrences)

    # Calculate the answers
    noSmoothing(bigTallyInFirst, bigTallyInSecond, vocabulary, bigramOccurrences)
    # addOneSmoothing(bigramsInFirst, bigramsInSecond, vocabulary)
    # print("Probabilities of sentence one")
