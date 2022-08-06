# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 21:46:19 2022

@author: Pranav Varanasi
"""
import nltk
nltk.download('maxent_ne_chunker')
import nltk
nltk.download('words')
  

import nltk 
from nltk.tokenize import word_tokenize
str="Gal Gadot is an Israeli actress and model. At age 18, she was crowned Miss Israel 2004. She then served two years in the Israel Defense Forces as a combat fitness instructor, whereafter she began studying at IDC Herzliya while building her modeling and acting careers."
words=word_tokenize(str)
word_tag=nltk.pos_tag(words)
tree=nltk.ne_chunk(word_tag)
tree.draw()
