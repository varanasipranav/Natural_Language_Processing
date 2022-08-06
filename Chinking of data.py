# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 21:29:37 2022

@author: Pranav Varanasi
"""

import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize
str=" Gal Gadot is an Israeli actress and model. At age 18, she was crowned Miss Israel 2004. She then served two years in the Israel Defense Forces as a combat fitness instructor, whereafter she began studying at IDC Herzliya while building her modeling and acting careers."
words=word_tokenize(str)
import nltk
nltk.download('averaged_perceptron_tagger')
str_tag=nltk.pos_tag(words)
print(str_tag)
grammer="""
        chunk:{<.*>+}
        }<JJ>{
        }<NN>{"""
chunk_parser=nltk.RegexpParser(grammer)
tree=chunk_parser.parse(str_tag)
tree.draw()