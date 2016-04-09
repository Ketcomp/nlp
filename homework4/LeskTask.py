__author__ = "Gaurav Ketkar"
__email__ = "gketkar08@gmail.com"

import string
from nltk.corpus import wordnet as wn

def printMeaning(valid, word, sense, maxCount):
    if valid == "Found":
       print("The word '" + word + "' has meaning :'" + sense + "' and count :" +str(maxCount))
       return
    elif valid =="Default":
        print("The word '" + word + "' has meaning :'" + sense +". Default meaning selected since results were inconclusive" )
        return
    elif valid =="Standard":
        print("The word '" + word + "' has no disambiguity")
        return

def findSense(sentence):
    for word in sentence.split(" "):
        # Strip word of any punctuations and make it lower case
        exclude = set(string.punctuation)
        word = ''.join(ch for ch in word if ch not in exclude)
        word.lower()
        # If word is a stop word, continue to next iteration.
        skip_words = ['a', 'an', 'the', 'this', 'that', 'and']
        if skip_words.__contains__(word):
            printMeaning("Standard", word, "", 0)
            continue

        # Get the context
        context = sentence.split(" ")
        if word in context:
            context.remove(word)

        # Initialize maxCount and sense of the word to default values.
        maxCount = 0
        count = 0
        sense = "Nothing makes sense"
        signature = []
        example_words = []
        definition_words = []

        # For every meaning of the word,
        for meaning in wn.synsets(word):
            # Generate 'signature' by adding words from definition and examples.
            for each_usage in meaning.examples():
                example_words += each_usage.split(" ")
            definition_words = meaning.definition().split(" ")
            signature = example_words + definition_words

            # How many times do the context words appear in the signature?
            for w in context:
                count += signature.count(w)
            # print(signature, context)
            # print("")

            # If count exceeds current maxCount then, update the sense of the word
            if count > maxCount:
                sense = meaning.definition()
                maxCount = count
            count = 0

        # If the count remained 0 for the word, pick the most common meaning from WordNet if it exists
        if sense == "Nothing makes sense":
            firstMeaning = wn.synsets(word)
            if len(firstMeaning) == 0: # This word does not exist in our dictionary
                printMeaning("Default", word, "but this word not found in our dictionary", 0)
                continue
            else:
                printMeaning("Default", word, firstMeaning[0].definition(), 0)
                continue

        # Print the calculated meaning of the word
        printMeaning("Found", word, sense, maxCount)

if __name__ == '__main__':
    sentence = input("Enter sentence: ")
    findSense(sentence)
