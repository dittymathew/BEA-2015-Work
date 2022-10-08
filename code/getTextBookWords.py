from pdftotxt import ConverttoTxt
from nltk.corpus import gutenberg,brown
from nltk.corpus import wordnet as wn
import os,re,nltk

c2txt =ConverttoTxt()
wnl = nltk.WordNetLemmatizer()

text_folder ='data/textcontent/'

text_words =[]
upto_cls =6
cls= ['class'+str(i+1)+'/' for i in range(upto_cls)]

for c in cls:
  for f in os.listdir(text_folder+c) :
    filen =text_folder+c+f
    con =c2txt.convert_pdf_to_txt(filen)
    con =re.sub('[^\x00-\x7F]+','', con.lower())
    con_words = re.sub('[\_\`\)\/\\\(\,!\.\:\;\'\"\?0-9]', '', con.lower()).split()
    corpus_words =set([wnl.lemmatize(w.lower()) for w in set(gutenberg.words()).union(set(brown.words()))])
    for w in con_words:
      w=wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(w.lower(),pos=wn.VERB),pos=wn.NOUN),wn.ADJ),wn.ADV) 
      if w in corpus_words and w not in text_words:
        text_words.append(w)
        print w


