# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 21:52:39 2022

@author: Pranav Varanasi
"""
import nltk
from nltk.tokenize import word_tokenize

def extract_ne(quote): 
    
    words = word_tokenize(quote)
    tags = nltk.pos_tag(words)
    tree = nltk.ne_chunk(tags, binary=True)
    return set(
        " ".join(i[0] for i in t)
           for t in tree
        if hasattr(t, "label") and t.label() == "NE"
    )
str="Gal Gadot is an Israeli actress and model. At age 18, she was crowned Miss Israel 2004. She then served two years in the Israel Defense Forces as a combat fitness instructor, whereafter she began studying at IDC Herzliya while building her modeling and acting careers."
print(extract_ne(str))    
   