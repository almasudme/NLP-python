import nltk
# nltk.download('brown')
# nltk.download('stopwords')


def access_cfd():
    from nltk.corpus import brown
    cfd = nltk.ConditionalFreqDist([
    (genre,word) 
    for genre in brown.categories()
    for word in brown.words(categories=genre)

    ])


    print(cfd.tabulate(
        conditions = ['government','news','lore'],
        samples = ['hardship','role','play'],
        cumulative= True
    ))

    print(cfd['news']['the'])

def compare_cfd():
    from nltk.corpus import names
    cfd2= nltk.ConditionalFreqDist([
        (fid.split('.')[0],name[-1]) 
        for fid in names.fileids()
        for name in names.words(fid)
    ])
    cfd2.tabulate(conditions=['male','female'],samples=['a','e'])

def handson():
    from nltk.corpus import brown
    from nltk.corpus import stopwords
    stops = [w.lower() for w in stopwords.words("english")]
    words = [w.lower() for w in brown.words() if w not in stops]
    cdev_cfd = cfdc
    



# access_cfd()
# compare_cfd()
handson()