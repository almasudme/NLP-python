import nltk
from nltk.corpus import genesis
nltk.download('genesis')
nltk.download('punkt_tab')
print(genesis.fileids())

'''
The following example determines the average word length and average sentence length of each text collection present in genesis corpus.
The methods raw, words and sents used in code determine the total number of characters, words, and sentences present in a specific text collection.
'''
for fileid in genesis.fileids():
    n_chars = len(genesis.raw(fileid))
    n_words = len(genesis.words(fileid))
    n_sents = len(genesis.sents(fileid))
    print(int(n_chars/n_words), int(n_words/n_sents), fileid)


    '''
Suppose, you have three files c1.txt, c2.txt and c3.txt in /usr/home/dict path.
Creation of corpus wordlists corpus is shown in the following example.
from nltk.corpus import PlaintextCorpusReader
corpus_root = '/usr/share/dict'
wordlists = PlaintextCorpusReader(corpus_root, '.*')
wordlists.fileids()
['c1.txt',
 'c2.txt',
 'c3.txt']
    '''
