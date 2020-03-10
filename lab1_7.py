import nltk
from nltk.stem import WordNetLemmatizer
from nltk.util import ngrams
nltk.download('wordnet')
nltk.download('punkt')

#Reading data from the input file
input_file = open("./nlp_input.txt", "r").read()

#Tokenizing words in the input file
wTokens = nltk.word_tokenize(input_file)
print("Word Tokens: \n")
for token in wTokens:
    print(token)

#Lemmatizing each word in word tokens
lem = WordNetLemmatizer()
print("After Lemmatization: \n")
for token in wTokens:
    print(lem.lemmatize(token))

#Printing Triagrams of all the word tokens
trigrams = ngrams(wTokens, 3)
print("Trigrams: \n")
for t in trigrams:
    print(t)

#Printing Top-10 trigrams
wFrequency = nltk.FreqDist(ngrams(wTokens, 3))
mcommon = wFrequency.most_common(10)
print("Top-10 Trigrams:\n", mcommon)

#Performing sentence tokenization
sTokens = nltk.sent_tokenize(input_file)
Result = []
for token in sTokens:
    for a,b in mcommon:
        if a in ngrams(token.split(),3):
            print(a,token)
            Result.append(token)
            break

#Printing the concatenated Result
print("Concatenated Result: \n", Result)