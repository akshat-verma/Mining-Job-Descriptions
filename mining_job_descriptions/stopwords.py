'''
Created on Jul 24, 2015

@author: akshat
'''

def create_stopwords_list(file):
    with open(file) as f:
        words = f.readlines()
    return [word.strip() for word in words]


print(create_stopwords_list("stop-words.txt"))
