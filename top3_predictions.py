import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import string
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import asyncio
import os
from os import walk
import sys

    
dic = os.listdir()
dic.sort()
hey=[]

for i in dic:
    if i.startswith('trainingnews'):
        hey.append(i)
dic=hey
count=len(dic)

temp=news=pd.read_csv('trainingnews1.csv')

for i in range(2,count+1):
    temp=pd.read_csv('trainingnews'+str(i)+'.csv')
    news=pd.concat([news,temp],ignore_index=True)

news['TITLE'] = news.TITLE.map(lambda x: x.lower().translate(str.maketrans('','', string.punctuation)))
X_train=news['TITLE']
Y_train=news['CATEGORY']
count_vector = CountVectorizer(stop_words = 'english')
training_data = count_vector.fit_transform(X_train)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(training_data)
naive_bayes = MultinomialNB()
naive_bayes.fit(X_train_tfidf,Y_train)

while(True):
    print(news)
    print("Wanna predict more??? y->yes,n->no")
    ypu=input("Enter choice")
    if(ypu=='n'):
        sys.exit()
    tex=input("Enter Text ")
    text=[tex]
    testing_data = count_vector.transform(text)
    predictions = naive_bayes.predict_proba(testing_data)
    best_n = np.argsort(-predictions, axis=1)[:, :3]
    t=list(naive_bayes.classes_[best_n[0]])
    df2={'TITLE':tex, 'CATEGORY':t[0]}

    for i in t:
        print(i)

    count=len(dic)

    temp=temp.append(df2, ignore_index=True)
    if temp['TITLE'].count()<1184:
        temp.to_csv('trainingnews'+str(count)+'.csv',index=False)
    else:
        string='trainingnews'
        string=string+str(count+1)+".csv"
        dic.append(string)
        temp=temp[1183:]
        temp.to_csv(string,index=False)
