#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 23:15:28 2018

@author: braulinho
"""
from progress.bar import Bar
import string
import unicodedata
from salidas import planes
from vectores import makeVector
from categorias import getCategories
from analyzer import sentimentAnalyzer , locationAnalyzer

def homologa(data, fuente, recipiente):
    if fuente == 0:
        for element in Bar('Trabajando TripAdvisor').iter(data):
            re = len(element['reviews'])
            cu = len(element['properties']['cuisines'])
            fe = len(element['properties']['features'])
            ev = len(element['properties']['events'])
            fo = len(element['properties']['food'])            
            if re > 2 and (cu > 0 or fe > 0 or ev > 0 or fo > 0): 
                obj={}
                obj['name'] = normalizaTexto(element['name'])                
                obj['img'] = element['img']
                if len (element['properties']['schedule']) > 0:
                    obj['schedule']= geSchedule(element['properties']['schedule'])                    
                if element['properties']['description'] is not None:
                    obj['description']= element['properties']['description']
                obj['reviews'] = len(element['reviews'])
                obj['vector'] = makeVector(element['properties'],0)
                obj['plan']=planes(element['properties'])
                obj['categoria']=getCategories(element['properties'])
                obj['ranking'] = sentimentAnalyzer(element['reviews'],0)
                obj['location'] = locationAnalyzer(element['location'])
                recipiente.append(obj)
    else:
        for element in Bar('Trabajando Facebook   ').iter(data):
            re = len(element['visitor_posts']['data']) if 'visitor_posts' in element else 0
            fe = len(element['category_list'])
            loc = 'location' in element            
            if re > 2 and fe > 0 and loc: 
                obj={}
                obj['name'] = normalizaTexto(element['name'])
                obj['img'] = [element['img']] if len(element['img'])> 0 else []
                if 'hours' in element:
                    obj['schedule'] = getSchedule(element['hours'])                         
                if 'about' in element:
                    obj['description']= element['about']
                obj['reviews'] = re
                obj['vector'] = makeVector(element['category_list'],1)
                obj['plan']=['amigos','personal']
                obj['categoria']=getCategories(element)
                obj['ranking'] = sentimentAnalyzer(element['visitor_posts']['data'],1)
                obj['location'] = {'lat':element['location']['latitude'], \
                                   'lng':element['location']['longitude']}
                recipiente.append(obj)       
    return recipiente

def normalizaTexto(cadena):
    signos=''.join(c for c in cadena.lower() if c not in string.punctuation)
    return unicodedata.normalize('NFKD', signos)

def geSchedule(schedule):
    payload={}
    for el in schedule:
        payload[normalizaTexto(el['day'])]=el['hours']
    return payload
    
def getSchedule(schedule):
    payload = {}
    if len (schedule) > 0:
        if 'fri_1_open' in schedule:
           payload['viernes'] = schedule['fri_1_open']\
              +' - '+schedule['fri_1_close']
        if 'sat_1_open' in schedule:
           payload['sabado']= schedule['sat_1_open']\
              +' - '+schedule['sat_1_close']
        if 'sun_1_open' in schedule:
           payload['domingo']= schedule['sun_1_open']\
              +' - '+schedule['sun_1_close']
        if 'mon_1_open' in schedule:
           payload['lunes']= schedule['mon_1_open']\
              +' - '+schedule['mon_1_close']
        if 'tue_1_open' in schedule:
           payload['martes']= schedule['tue_1_open']\
              +' - '+schedule['tue_1_close']
        if 'wed_1_open' in schedule:
           payload['miercoles']= schedule['wed_1_open']\
              +' - '+schedule['wed_1_close']
        if 'thu_1_open' in schedule:
           payload['jueves']= schedule['thu_1_open']\
              +' - '+schedule['thu_1_close']   
    return payload             