# -*- coding: utf-8 -*-
#import regexp
import re
"""
Created on Mon Nov 25 14:03:40 2019

@author: student
"""

# rt - read text
with open('C:\\Users\\student\\artykul.txt', encoding='utf-8') as f:
    article = f.read()

#
article = re.sub(r'[\W\d]', ' ', article)    

all_words = article.split()

print(all_words)

polish = {}

with open('C:\\Users\\student\\PoliMorf-0.6.7.tab', encoding='utf-8') as f:
    for linia in f:
        tokens_in_line = linia.split()
        polish[tokens_in_line[0].lower()] = tokens_in_line[1].lower()
        

all_words_normalized = []        
word_count = {}

for word in all_words:
    if len(word) >6:
        word_lower = word.lower()
        normalized = polish.get(word_lower, word_lower);
        word_count[normalized] = word_count.get(normalized, 0) + 1    
        
print('\n\n ========= \n\n')  
print(word_count)        



#prosciej
#collections.Counter(all_words).most_common(10)
