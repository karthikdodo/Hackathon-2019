import io
import numpy as np
import collections
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from colorama import init
from termcolor import colored
from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                           filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
fo=open(root.filename,encoding="utf8")
a=fo.read()
item=fo.read().split('.')
corpus=item
print(corpus)
stopwords = set(line.strip() for line in open('stopwords.txt'))
stopwords = stopwords.union(set(['mr','mrs','one','two','said']))
wordcount={}
for word in a.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
init()
"""n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))"""
print("The top three picks for the document")
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(3):

    print(colored(word,'green', 'on_red'))
    Tk(word)




fo.close()