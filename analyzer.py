#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 01:24:03 2018

@author: braulinho
"""
import indicoio
import googlemaps
from functools import reduce

#mia indicoio.config.api_key = 'd7d752ee875e2f203e94d456872fd0f8'
indicoio.config.api_key = '5e1084f6c5ca1e2f892e44c4616be528' #alex

gmaps = googlemaps.Client(key='AIzaSyB8_PtzyaFQXdplUhz_N8rWVBRBN6QRgww')

def sentimentAnalyzer(comentarios,fuente):
    data = []
    values = []
    if fuente == 0:
        for comentario in comentarios:
            if comentario['review'] is not None:
                data.append(comentario['review'])
        values = indicoio.sentiment(data) if len(data) > 0 else [0]
    else:
        for comentario in comentarios:
            if 'message' in comentario:
                data.append(comentario['message'])
        values = indicoio.sentiment(data) if len(data) > 0 else [0]

    val = reduce(lambda x , y : x + y, values)
    return val/len(values)

def locationAnalyzer(location):
    direccion=''
    if location['street'] is not None:
        direccion=location['street']
    if location['barrio'] is not None:
        direccion+=', '+location['barrio']
    if location['locality'] is not None:
        direccion+=', '+location['locality']
    if location['country'] is not None:
        direccion+=', '+location['country']
    geocode_result = gmaps.geocode(direccion)
    payload = geocode_result[0]['geometry']['location'] if not None else {}
    return payload