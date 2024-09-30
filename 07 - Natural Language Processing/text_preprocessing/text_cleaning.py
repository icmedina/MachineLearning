#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 09:56:57 2021
TEXT CLEANING

@author: ice
"""
text = "finallllllly a it's you and me you're qqqqqqqqueeeeen awessssssssssssooooooooooooome greeeeeeeeeeeeeeeeeeeeaaaaaaaaaaaaaaaaaaaaaatttttttttttttt"

# remove multiple consecutive letters
def fix_multiple_letters(text):
    import re
    
    pattern = re.compile(r"(.)\1{2,}")
    text_output = pattern.sub(r"\1", text)
    # text_output = pattern.sub(r"\1\1", text)
    return text_output

# spell checker
def spell_checker (text):
    from textblob import TextBlob             # using textblob
    
    text_output = TextBlob(str(text)) 
    return str(text_output.correct())
    
# remove stop words using collections
def remove_stop_words(text):
    from nltk.corpus import stopwords
    from collections import Counter
    
    stop_words = stopwords.words('english')
    stopwords_dict = Counter(stop_words)
    text_output = ' '.join([word for word in text.split() if word not in stopwords_dict])
    return text_output

text = remove_stop_words(text)
text = fix_multiple_letters(text)
text = spell_checker(text)

print (text)













# =============================================================================
# Data Cleaning
# =============================================================================
def normalize(document):
    # import regular expression to remove unneccessary characters, tabs, newline etc.
    import re
    #document = re.sub(r'\\n', '', document)                 # Remove newline characters
    document = re.sub(r'-', '', document)                   # remove '-' from compound words
    document = re.sub(r"([^\x00-\x7F])+", " ", document)    # Remove nonstandard ascii characters
    document = re.sub(r'\W', ' ', document)                 # Remove all the special characters
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)     # remove all single characters
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)      # Remove single characters from the start
    document = re.sub(r'\d+', '', document)                 # Remove numbers
    document = re.sub(r'\s+', ' ', document, flags=re.I)    # Substituting multiple spaces with single space
    document = document.lower()                             # Converting to Lowercase
    
    return (document)





"""
Python metacharacters: . ^ $ * + ? { } [ ] \ | ( )


    

Unusual words

with 3 consecutive double letters
bookkeeper

English pangram is a sentence that contains all 26 letters of the English alphabet. 
The most well known English pangram is probably “The quick brown fox jumps over the lazy dog”. 
My favorite pangram is “Amazingly few discotheques provide jukeboxes.”

Which letters can be doubled?

The frequency of double letters in an English corpus The most common double letter 
is L, with LL accounting for 0.6% of all bigrams. Other common double-letter bigrams 
are SS, EE, OO, and TT. Some double letters did not appear in the corpus: 
    JJ, KK, QQ, VV, WW, and YY.
"""