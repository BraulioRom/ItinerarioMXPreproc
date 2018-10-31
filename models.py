#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 17:42:36 2018

@author: braulinho
"""
import os
import time
import pandas as pd
from progress.bar import Bar
from sklearn.cluster import KMeans
from sklearn.externals import joblib
from sklearn.naive_bayes import BernoulliNB


def makeClassifier(fuente):
    #fuente = final
    data=[]
    bar = Bar('Clasificando lugares  ', max = len(fuente))
    for dat in fuente:
        data.append(dat['vector'])

    #empezamos separamos en elementos
    array= list(map(lambda x : x.split(','),data))
    
    df = pd.DataFrame(data=array, dtype = int)
    y = makeLabels(df)
        
    for i,elm in enumerate(fuente):
        elm['cluster']=str(y[i])
        bar.next()
        time.sleep(0.01)
    bar.finish()
    
    clf = BernoulliNB().fit(df,y)
    bar1 = Bar('Generando Modelo      ', max=100)
    for i in range(100):
        time.sleep(0.01)
        bar1.next()
    bar1.finish()
    
    cwd = os.getcwd()
    if os.path.isfile(cwd+'/clasificador.pkl'):
        os.remove(cwd+'/clasificador.pkl')

    joblib.dump(clf, cwd+'/clasificador.pkl') 

    return [fuente, cwd+'/clasificador.pkl']

    
def makeLabels(dataframe):
#    dataframe=df
    kmeans = KMeans(n_clusters=6, random_state=0).fit(dataframe)
    return kmeans.labels_