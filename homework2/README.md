An automatic speech recognition system has provided two written sentences as possible interpretations to a speech input.
---
* S1: The president has relinquished his control of the company's board.
* S2: The chief executive officer said the last year revenue was good.

Using the *bigram language model* trained on Corpus A provided below, find out which of the two sentences is more probable. Compute the probability of each of the two sentences under the three following scenarios:

    a) Use the bigram model without smoothing.
    b) Use the bigram model with add-one smoothing
    c) Use the bigram model with Good-Turing discounting.

Assignment:
---
    1. Write a program to compute the bigrams for any given input.
    2. Apply your program to compute the bigrams you need for this homework. 
    3. Construct the tables with the bigram counts for the two sentences above.

For each of the three scenarios:

    4. Construct the table with the bigram probabilities for the sentences.
    5. Compute the total probabilities for each sentence S1 and S2.
