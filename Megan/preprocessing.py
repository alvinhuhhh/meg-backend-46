import html
import os
import re
import nltk
import string
import pickle
import json
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from pathlib import Path

###########
# Globals #
###########
entry_length = 30
padding_type = 'post'
oov_tok = '<OOV>'
CURR_PATH = os.path.dirname(os.path.abspath(__file__))

##################
# Load tokenizer #
##################
with open(os.path.join(CURR_PATH, 'tokenizers/tokenizer.pickle'), 'rb') as f:
    tokenizer = pickle.load(f)

#############
# Functions #
#############
def PreProcess(doc):
    """
    1. Removes usernames and weblinks
    2. Removes stopwords
    3. Stems words

    Input:
    doc(string)
    Output:
    request(Json)
    """
    doc.lower()
    doc = re.sub('@[^\s]+', '', doc)
    doc = re.sub('http://[^\s]+', '', doc)
    t = nltk.tokenize.word_tokenize(doc)

    result = ''
    stemmer = nltk.stem.PorterStemmer()
    for token in t:
        if token in string.punctuation:
            continue
        elif token in nltk.corpus.stopwords.words('english'):
            continue
        else:
            result += ' ' + stemmer.stem(token)

    # Pre-process
    pre = [result]
    tokenized = tokenizer.texts_to_sequences(pre)
    padded = pad_sequences(tokenized, maxlen=entry_length, padding=padding_type)

    # Parse into json
    request = {"instances": padded.tolist()}

    return request

def ProcessResult(JsonString):
    """
    Processes the JSON object from the machine learning server.

    Input: 
    JsonString(string)
    Output:
    integer(integer)
    """
    predictions = json.loads(JsonString)['predictions'][0]
    tensor = tf.math.argmax(predictions)
    integer = tensor.numpy()
    return integer

#########
# Debug #
#########
def main():
    text = 'I am feeling good.'
    print(PreProcess(text))
    return

if __name__ == "__main__":
    main()