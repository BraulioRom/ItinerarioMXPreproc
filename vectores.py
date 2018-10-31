#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 23:10:17 2018

@author: braulinho
"""

trip=[
    "Latina",
    "Estadounidense",
    "Del Medio Oriente",
    "Mediterránea",
    "Internacional",
    "Mexicana",
    "Española",
    "Argentina",
    "Italiana",
    "Francesa",
    "De la India",
    "Libanesa",
    "Churrasquería",
    "Cafe",
    "Mariscos",
    "Sopas",
    "Apto para vegetarianos",
    "Pizzería",
    "Parrilla",
    "Comida para llevar",
    "Delicatessen",
    "Contemporánea",
    "Opciones veganas",
    "Bar",
    "Pub",
    "Vino y cerveza"
    ]

face=[
    {'Latina':[
            "Brazilian Restaurant",
            "Argentinian Restaurant",
            "Mexican Restaurant"]},
    {'Estadounidense':[
        "Tex-Mex Restaurant",
        "Barbecue Restaurant",
        "Southwestern Restaurant",
        "Burger Restaurant",
        "New American Restaurant",
        "American Restaurant"]},
    {'Del Medio Oriente':["Chinese Restaurant","Sushi Restaurant"]},
    {'Mediterránea':["Mediterranean Restaurant"]},
    {'Internacional':[
        "European Restaurant",
        "Spanish Restaurant",
        "Italian Restaurant",
        "Argentinian Restaurant",
        "Chinese Restaurant"]},
    {'Mexicana':["Mexican Restaurant"]},
    {'Española':["Spanish Restaurant"]},
    {'Argentina':["Argentinian Restaurant"]},
    {'Italiana':["Italian Restaurant"]},
    {'Francesa':[]},
    {'De la India':["North Indian Restaurant"]},
    {'Libanesa':["Lebanese Restaurant"]},
    {'Churrasquería':["Brazilian Restaurant"]},
    {'Cafe':["Coffee Shop","Cafeteria","Cafe"]},
    {'Mariscos':["Seafood Restaurant"]},
    {'Sopas':["Family Style Restaurant","Restaurant","Local Service"]},
    {'Apto para vegetarianos':["Health Food Restaurant"]},
    {'Pizzería':["Pizza Place"]},
    {'Parrilla':["Bar & Grill","Steakhouse"]},
    {'Comida para llevar':["Food Stand","Fast Food Restaurant"]},
    {'Delicatessen':["Bakery"]},
    {'Contemporánea':[]},
    {'Opciones veganas':["Health Food Restaurant"]},
    {'Bar':["Bar","Brewery","Beer Garden","Dance & Night Club","Dive Bar","Tapas Bar & Restaurant"]},
    {'Pub':["Pub","Jazz & Blues Club","Karaoke"]},
    {'Vino y cerveza':["Wine Bar"]}
    ]

def makeVector(propiedades,fuente):
    if fuente == 0:
        caracs=[]
        if len(propiedades['cuisines']) > 0:
            caracs = [a.strip() for a in propiedades['cuisines']]
        if len(propiedades['features']) > 0:
            caracs.extend([x.strip() for x in propiedades['features'][0].split(',')])
        if len(propiedades['events']) > 0:
            caracs.extend([y.strip() for y in propiedades['events'][0].split(',')])
        if len(propiedades['food']) > 0:
            caracs.extend([z.strip() for z in propiedades['food'][0].split(',')])
        vector=''
        for tr in trip:
            if tr in caracs:
                vector = vector+'1' if len(vector)==0 else vector+',1'
            else:
                vector = vector+'0' if len(vector)==0 else vector+',0'
    else:
        caracs=[]
        if len(propiedades) > 0:                
            caracs = [a['name'] for a in propiedades]
        vector=''
        for tr in face:
            array = list(tr.values())[0]
            if len(array) > 0:
                for el in array:        
                    if el in caracs:
                        vector = vector+'1' if len(vector)==0 else vector+',1'
                        break
                    else:
                        vector = vector+'0' if len(vector)==0 else vector+',0'
                        break
            else:
                vector = vector+'0' if len(vector)==0 else vector+',0'
    
    return vector