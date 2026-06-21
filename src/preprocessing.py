import re
import string
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer

ps=PorterStemmer()

def preprocess(text):
    #lowercaing
    text=str(text).lower()

    #remove html tags

    text=BeautifulSoup(text,"html.parser").get_text()

    #removing punctuation tags
    text=text.translate(str.maketrans("","",string.punctuation))

    #remove extra spaces

    text=re.sub(r'\s'," ",text).strip()

    #stemming
    words=text.split()
    words=[ps.stem(word) for word in words]

    return " ".join(words)
