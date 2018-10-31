#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 15:23:06 2018

@author: braulinho

nomas sirve para ver las caracteristicas que nos puedieran ayudar en los tipos

personal amigos y familiar
"""
import os
import json

cwd = os.getcwd()

trip = json.loads(open(cwd+'/datasets/tripadvisor.json',encoding='utf-8').read())
fb = json.loads(open(cwd+'/datasets/facebook.json',encoding='utf-8').read())

events=[]
for el in trip:
    if len(el['properties']['events'])>0:
        for a in el['properties']['events'][0].split(','):
            if a.strip() not in events:
                events.append(a.strip())
features=[]
for el in trip:
    if len(el['properties']['features'])>0:
        for a in el['properties']['features'][0].split(','):
            if a.strip() not in features:
                features.append(a.strip())
food=[]
for el in trip:
    if len(el['properties']['food'])>0:
        for a in el['properties']['food'][0].split(','):
            if a.strip() not in food:
                food.append(a.strip())
cuisines=[]
for el in trip:
    if len(el['properties']['cuisines'])>0:
        for a in el['properties']['cuisines'][0].split(','):
            if a.strip() not in cuisines:
                cuisines.append(a.strip())
face=[]
for f in fb:
    if len(f['category_list'])>0:
        for el in f['category_list']:
            if el['name'] not in face:
                face.append(el['name'])
                
print (events)
print('\n')
print (features)
print('\n')
print (food)
print('\n')
print (cuisines)
print('\n')
print (face)









