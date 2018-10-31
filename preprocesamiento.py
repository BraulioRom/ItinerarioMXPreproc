#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 19:11:32 2018

@author: braulinho
"""
import os
import json 
import time     
import subprocess

from progress.bar import Bar
from pymongo import MongoClient
from estructuras import homologa
from models import makeClassifier

fuentes = ['tripadvisor.json','facebook.json']

def preproc():
    if subprocess.call("command -v mongo", shell=True) == 1:    
        print ('Se requiere tener instalado: \
               \n \t - MongoDB \
               \n \t - /data/db Directory \
               \nSee: MongoDB Docs. Installation.')
        exit()
    
    if not os.path.isdir('/data/db'):
        print ('Necesitas crear el directorio: \
               \n\t - /data/db \
               \nSee: MongoDB Docs. Instalattion.')
        exit()
        
    cwd = os.getcwd()

    #cargamos data 
    for i in Bar('\n\nCargando datos\t      ').iter(fuentes):
        if i == 'tripadvisor.json':    
            trip = json.loads(open(cwd+'/datasets/'+i,encoding='utf-8').read())
        else:
            fb = json.loads(open(cwd+'/datasets/'+i,encoding='utf-8').read())
        time.sleep(0.3)
        
    #homologamos data
    final=[]
    final=homologa(trip,0,final)
    viablesTrip =len(final)
    final=homologa(fb,1,final)
    viablesFb =len(final)-viablesTrip
    
    #generamos modelos
    dataClasificada, path = makeClassifier(final)

    
    #guardar data en mongo
    client = MongoClient('localhost', 27017)
    db = client['ItinerarioMX']['lugares']
    for doc in Bar('Guardando en BD       ').iter(final):
        result = db.insert_one(doc)

    #reporte
    print('\n\n\t\t-------- REPORTE --------\
          \n\t\t\tDatos:\
          \n\t\t\t\tDatos Facebook:    {} viables de {}\
          \n\t\t\t\tDatos Tripadvisor: {} viables de {}\
          \n\n\t\t\tModelo:\
          \n\t\t\t\tPath: {}\n\n'\
          .format(viablesFb,len(fb),viablesTrip,len(trip),path))


if __name__ == "__main__":
    preproc()