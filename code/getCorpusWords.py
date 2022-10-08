from nltk.corpus import gutenberg,brown
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
import nltk,re

def extractDefn(word):
  synsets = wn.synsets(word)
  if synsets ==[]:
    return []
  defn = synsets[0].definition()
  defn = re.sub('[\`\)\\\(\,!\.\:\;\'\"\?0-9]', '', defn.lower())
  def_words =defn.split()
  new_defWords = [wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(w,pos=wn.VERB),pos=wn.NOUN),wn.ADJ),wn.ADV) for w in def_words if w not in stop]
  return new_defWords

def taggedWords(sents):
  tag_words=[]
  for s in sents:
    for w_tag in nltk.pos_tag(s):
 
      if w_tag[0] not in ['.',',','?','!',';',':']:
        tag_words.append(w_tag)
  return tag_words

def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']


def is_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']


def is_adverb(tag):
    return tag in ['RB', 'RBR', 'RBS']


def is_adjective(tag):
    return tag in ['JJ', 'JJR', 'JJS']


###Main

wnl = nltk.WordNetLemmatizer()
stop = stopwords.words('english')
corpus_words=[]

##Get Words from brown corpus
for (w,tag) in brown.tagged_words():  
  w=w.lower()
  if is_noun(tag):
    w_lemma = wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(w,pos=wn.NOUN),pos=wn.VERB),wn.ADJ),wn.ADV))
  elif is_verb(tag):
    w_lemma = wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(w,pos=wn.VERB),pos=wn.NOUN),wn.ADJ),wn.ADV))
  elif is_adverb(tag):
    w_lemma = wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(w,pos=wn.ADV),pos=wn.NOUN),wn.ADJ),wn.VERB))
  elif is_adjective(tag):
    w_lemma = wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(w,pos=wn.ADJ),pos=wn.NOUN),wn.VERB),wn.ADV))
  else:
    w_lemma = wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(wnl.lemmatize(w,pos=wn.VERB),pos=wn.NOUN),wn.ADJ),wn.ADV))
  if w_lemma not in corpus_words:
    corpus_words.append(w_lemma)

#Extract definition from Wordnet for corpus words
for w in corpus_words:
  w_defn =extractDefn(w)
  w_def_str =''.join(wd+',' for wd in w_defn).strip(',')
  if w_defn !=[]:
    print w+':'+w_def_str
