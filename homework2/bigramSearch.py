from collections import Counter
import pprint

#Split text at spaces and return a list of words
def splitAtSpaces(fileToSplit):
    listOfWords = fileToSplit.split()
    return listOfWords

#Split words in bigrams and return a list of bigrams
def wordsToBigrams(words):
    bigrams = [(words[element-1],words[element]) for element in range(1,(words.__len__()))]
    return bigrams

#Count the # of occurrences of bigrams and return a dictionary counting occurrences of bigrams
def countBigrams(bigrams):
    bigramOccurrences = Counter()
    for bigram in bigrams:
        bigramOccurrences[bigram] += 1
    return bigramOccurrences
#Count # of occurrences of words (or Unigrams) and return a dictionary containing the #'s
def countWords(words):
    wordOccurrences = Counter()
    for word in words:
        wordOccurrences[word] += 1
    return wordOccurrences

def bigOccurInSentence(sentence):
    #Split sentence at spaces
    words = splitAtSpaces(sentence)
    #Calculate bigrams
    return wordsToBigrams(words)

#Generate the bigram count table
def bigCountForTable(sentence):
    words = splitAtSpaces(sentence)
    totalSentenceBigrams = [(a,b) for b in words for a in words]
    print(totalSentenceBigrams)


if __name__ == '__main__':

    #Read corpus data in the variable corpusFile
    f = open('corpus.txt','r')
    corpusFile = f.read()

    #Split corpus file in a list 'words' at \s (i.e. spaces)
    words = splitAtSpaces(corpusFile)
    # print(words[33])

    #Count occurrences of words[i] in words
    wordOccurrences = countWords(words)
    # pprint.pprint(wordOccurrences)

    #Split words into constituent bigrams
    bigrams = wordsToBigrams(words)
    # print(bigrams)

    #Count the total number of each bigram
    bigramOccurrences = countBigrams(bigrams)
    # pprint.pprint(bigramOccurrences)

    #Calculate the values of N, V, c and c* & make all possible bigrams
    bigCountForTable("The president has relinquished his control of the company's board.")
    # print(bigramOccurrences[('the', "company's")])
    #Calculate probabilities
