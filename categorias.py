#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 23:38:57 2018

@author: braulinho
"""
import os
import json

cwd = os.getcwd()

restaurante=['Comida local','Romántico','Vistas','Comida para llevar','Meseros',
             'Bufé','Italiana','Mexicana','Libanesa','Churrasquería','Española',
             'Apto para vegetarianos','Argentina', 'Internacional','Francesa',
             'Comida rápida','De la India','Mariscos','Mediterránea',
             'Tex-Mex Restaurant', 'Mexican Restaurant', 'Family Style Restaurant',
             'Locality', 'Seafood Restaurant', 'European Restaurant', 
             'Argentinian Restaurant', 'Italian Restaurant', 'Health Food Restaurant', 
             'North Indian Restaurant','Lebanese Restaurant', 'Restaurant',
             'Fast Food Restaurant','Spanish Restaurant','Food & Beverage Company',
             'Food','Barbecue Restaurant', 'Pizza Place','Steakhouse', 
             'Southwestern Restaurant', 'Chinese Restaurant', 'Sushi Restaurant', 
             'Buffet Restaurant','Food Stand','Arabian Restaurant',
             'Brazilian Restaurant','Mediterranean Restaurant',
             'Breakfast & Brunch Restaurant','Local Business','American Restaurant',
             'Burger Restaurant', 'New American Restaurant' 
             ]

bares=['Sirve alcohol','Bar completo','Vino y cerveza','Bar con música en vivo',
       'Bar','Bar & Grill','Brewery','Beer Garden','Dance & Night Club',
       'Dive Bar','Pub','Wine Bar','Tapas Bar & Restaurant','Lounge',
       'Performance & Event Venue','Jazz & Blues Club','Live Music Venue',
       'Gastropub','Gay Bar','Karaoke']

cafe=['Café','Coffee Shop','Cafeteria','Cafe','Bakery']

trip = json.loads(open(cwd+'/datasets/tripadvisor.json',encoding='utf-8').read())
fb = json.loads(open(cwd+'/datasets/facebook.json',encoding='utf-8').read())

def getCategories(data):
    caracs=[]
    salida=[]
    if ('cuisines' in data) and (len(data['cuisines']) > 0):
        caracs = [a.strip() for a in data['cuisines']]
        
    if ('features' in data) and (len(data['features']) > 0):
        caracs.extend([x.strip() for x in data['features'][0].split(',')])
        
    if ('events' in data) and (len(data['events']) > 0):
        caracs.extend([y.strip() for y in data['events'][0].split(',')])
        
    if ('category_list' in data) and (len(data['category_list']) > 0):
        for el in data['category_list']:
            caracs.append(el['name'])
            
    for c in caracs:
        if c in restaurante:
            if 'restaurante' not in salida:
                salida.append('restaurante')
        if c in bares:
            if 'bar' not in salida:
                salida.append('bar')
        if c in cafe:
            if 'cafe' not in salida:
                salida.append('cafe')
    return salida