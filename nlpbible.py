# 101 - Tokenize the sentence

#Tokenizing is breaking a larger part of a sentence into smaller parts
#for a paragraph, sentences are tokens
#for a sentence, words are tokens
#Tokens are stored as list items and thus can be accessed via index items like list[0], list[1] etc

#step 1: Import Natural Language Tool Kit
import nltk
#step 2: From NLTK's Tokenizer tool, import sentence tokenizer and word tokenizer
from nltk.tokenize import sent_tokenize, word_tokenize
#step 3: Target Sentence stored in txt variable
txt="A real mathematician can mathematically mathematise mathematics in a mathematical mathematiculation. So if a mathematician can mathematise mathematics in a mathematical mathematiculation, why can't you mathematically mathematise mathematics in a mathematical mathematiculation like the mathematician who mathematically mathematises mathematics in a mathematical mathematiculation."
#step 4: tokenize the inputs as sentences
print(str(sent_tokenize(txt))+"\n")
#step 5: tokenize the inputs as words
print(word_tokenize(txt))
#step 6: store the sentence tokens in sent_tok variable
sent_tok=sent_tokenize(txt)
#step 7: write the output stored in sent_tok to "sentence_tokens.txt"
f=open("sentence_tokens.txt","w")
f.write(str(sent_tok))
f.close()
#step 8: store the word tokens in word_tok variable
word_tok=word_tokenize(txt)
#step 9: write the output stored in word_tok to "word_tokens.txt" as string
#closes the file after that
f=open("word_tokens.txt","w")
f.write(str(word_tok))
f.close()


# 102 - Remove Stop Words

#stop words are simply filler words (Words we stop on, in a sentence)
#these are useless words that can be removed

#step 1: From the NLTK corpus of words, import stopwords
from nltk.corpus import stopwords
#step 2: Create a variable stop_words & store the english stop words in that (Language is changeable)
stop_words=set(stopwords.words('english'))
#step 3: Create a variable filtered_sentences; Compare each w to each word in stop word ; store those words from w that dont match with stop_Words, into filtered_sentence
filtered_sentence=[w for w in word_tok if not w in stop_words]

#alternate for loop to the list comprehension loop used above
# filtered_sentence=[]
# for w in word_tok:
#     if w not in stop_words:
#         filtered_sentence.append(w)

#step 4: print those unmatched words (without stop words)
print(filtered_sentence)
#step 5: store them in stp_Wrds text file
f=open("stp_wrds.txt","w")
f.write(str(filtered_sentence))
f.close()


# 103 - Stemming Process

#The reason why we stem is to shorten the lookup, and normalize sentences.
#stemming is the process of normalizing the sentences by taking only the original form of the word 
#in a nutshell, stemming is the process of finding the word's absolute primary stem
#for example considering : I was taking a ride in the car || I was riding in the car : The content is the same except for "ride" tense || for a program it isn't absolutely necessary because it isn't efficient

#Step 1:Import Porterstemmer from NLTK.stem module
from nltk.stem import PorterStemmer
#Step 2:assign ps as variable that calls PorterStemmer function
ps=PorterStemmer()
#Step 3:pen a file called stemwrd.txt to write the output to it
f=open("stemwrd.txt",'w')

#Step 4:run a loop - For each word as w in word tokens,
#Step 5:create variable txt3 || call ps as an object to function stem() that takes each word as an argument and loops through it
#Step 6:stores the looped words in the file that was created before the loop
#Step 7:File open for writing before the loop because, when it's inside the loop it opens the file, prints one loop's output and closes | Similary continues and shows us only last output
for w in word_tok:
	txt3=w + " : " + ps.stem(w)
	print(txt3)
	f.write(txt3 + "\n")
#Step 8:closes the file after that
f.close()


# 104 - Parts of Speech Tagging
#as the name suggests, it involves tagging each word in a sentence with its associated Part of Speech

#Step 1:Use nltk module to call pos_tag function on word_tok thus tagging each word token with its associated word token and store it in pos_tags
#step 2: Writing the output to a text file for reference
pos_tags=nltk.pos_tag(word_tok)
print(pos_tags)
f=open("wordtokens_with_POS_tags.txt",'w')
f.write(str(pos_tags))
f.close()
